import os
from dotenv import load_dotenv
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from crewai import Agent, Task, Crew, LLM

# Load environment variables
load_dotenv()

# Initialize API keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
GEMINI=os.getenv("GEMINI")

# Initialize LLM
llm = ChatGroq(
    model="llama-3.2-1b-preview",
    temperature=0,
    max_tokens=500,
    timeout=None,
    max_retries=2,
)

crew_llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=GEMINI,
    max_tokens=500,
    temperature=0.7
)

def check_local_knowledge(query, context):
    """Router function to determine if we can answer from local knowledge"""
    prompt = '''Role: Question-Answering Assistant
Task: Determine whether the system can answer the user's question based on the provided text.
Instructions:
    - Analyze the text and identify if it contains the necessary information to answer the user's question.
    - Provide a clear and concise response indicating whether the system can answer the question or not.
    - Your response should include only a single word. Nothing else, no other text, information, header/footer. 

Output Format:
    - Answer: Yes/No

Study the below examples and based on that, respond to the last question. 
Examples:
    Input: 
        Text: The capital of France is Paris.
        User Question: What is the capital of France?
    Expected Output:
        Answer: Yes
    Input: 
        Text: The population of the United States is over 330 million.
        User Question: What is the population of China?
    Expected Output:
        Answer: No
    Input:
        User Question: {query}
        Text: {text}
'''
    
    formatted_prompt = prompt.format(text=context, query=query)
    response = llm.invoke(formatted_prompt)
    return response.content.strip().lower() == "yes"

def setup_web_scraping_agent():
    """Setup the web scraping agent and related components"""
    search_tool = SerperDevTool()  # Tool for performing web searches
    scrape_website = ScrapeWebsiteTool()  # Tool for extracting data from websites
    
    # Define the web search agent
    web_search_agent = Agent(
        role="Expert Web Search Agent",
        goal="Identify and retrieve relevant web data for user queries",
        backstory="An expert in identifying valuable web sources for the user's needs",
        allow_delegation=False,
        verbose=True,
        llm=crew_llm
    )
    
    # Define the web scraping agent
    web_scraper_agent = Agent(
        role="Expert Web Scraper Agent",
        goal="Extract and analyze content from specific web pages identified by the search agent",
        backstory="A highly skilled web scraper, capable of analyzing and summarizing website content accurately",
        allow_delegation=False,
        verbose=True,
        llm=crew_llm
    )
    
    # Define the web search task
    search_task = Task(
        description=(
            "Identify the most relevant web page or article for the topic: '{topic}'. "
            "Use all available tools to search for and provide a link to a web page "
            "that contains valuable information about the topic. Keep your response concise."
        ),
        expected_output=(
            "A concise summary of the most relevant web page or article for '{topic}', "
            "including the link to the source and key points from the content."
        ),
        tools=[search_tool],
        agent=web_search_agent,
    )
    
    # Define the web scraping task
    scraping_task = Task(
        description=(
            "Extract and analyze data from the given web page or website. Focus on the key sections "
            "that provide insights into the topic: '{topic}'. Use all available tools to retrieve the content, "
            "and summarize the key findings in a concise manner."
        ),
        expected_output=(
            "A detailed summary of the content from the given web page or website, highlighting the key insights "
            "and explaining their relevance to the topic: '{topic}'. Ensure clarity and conciseness."
        ),
        tools=[scrape_website],
        agent=web_scraper_agent,
    )
    
    # Define the crew to manage agents and tasks
    crew = Crew(
        agents=[web_search_agent, web_scraper_agent],
        tasks=[search_task, scraping_task],
        verbose=1,
        memory=False,
    )
    return crew


def get_web_content(query):
    """Get content from web scraping"""
    crew = setup_web_scraping_agent()
    result = crew.kickoff(inputs={"topic": query})
    return result.raw

def setup_vector_db(pdf_path):
    """Setup vector database from PDF"""
    # Load and chunk PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=50
    )
    chunks = text_splitter.split_documents(documents)
    
    # Create vector database
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )
    vector_db = FAISS.from_documents(chunks, embeddings)
    
    return vector_db

def get_local_content(vector_db, query):
    """Get content from vector database"""
    docs = vector_db.similarity_search(query, k=5)
    return " ".join([doc.page_content for doc in docs])

def generate_final_answer(context, query):
    """Generate final answer using LLM"""
    messages = [
        (
            "system",
            "You are a helpful assistant. Use the provided context to answer the query accurately.",
        ),
        ("system", f"Context: {context}"),
        ("human", query),
    ]
    response = llm.invoke(messages)
    return response.content

def process_query(query, vector_db, local_context):
    """Main function to process user query"""
    print(f"Processing query: {query}")
    
    # Step 1: Check if we can answer from local knowledge
    can_answer_locally = check_local_knowledge(query, local_context)
    print(f"Can answer locally: {can_answer_locally}")
    
    # Step 2: Get context either from local DB or web
    if can_answer_locally:
        context = get_local_content(vector_db, query)
        print("Retrieved context from local documents")
    else:
        context = get_web_content(query)
        print("Retrieved context from web scraping")
    
    # Step 3: Generate final answer
    answer = generate_final_answer(context, query)
    return answer

def main():
    # Setup
    pdf_path = "genai-principles.pdf"  # Replace with your PDF path
    
    # Initialize vector database
    print("Setting up vector database...")
    vector_db = setup_vector_db(pdf_path)
    
    # Get initial context from PDF for routing
    local_context = get_local_content(vector_db, "")
    
    # Example usage
    query = "What is Agentic RAG?"
    result = process_query(query, vector_db, local_context)
    print("\nFinal Answer:")
    print(result)

if __name__ == "__main__":
    main()
