## Note: These are very basic prompts and setups to get you started. For advanced features, error handling, and customization — refer to the official documentation of each tool.

# 1. SEO Data Tool (LangChain Example)
from langchain.tools import DuckDuckGoSearchResults
search = DuckDuckGoSearchResults()
results = search.run("latest SEO strategies 2024")

# 2. Cassandra Database Toolkit (CrewAI Example)
from crewai_tools import CassandraToolkit
cassandra_tool = CassandraToolkit(contact_points=["127.0.0.1"], keyspace="mykeyspace")
result = cassandra_tool.run("SELECT * FROM users LIMIT 5;")

# 3. YouTube Transcript Loader (LlamaIndex)
from llama_index.readers.youtube_transcript import YoutubeTranscriptReader
loader = YoutubeTranscriptReader()
documents = loader.load_data(ytlinks=["https://www.youtube.com/watch?v=i3OYlaoj-BM"])

# 4. CodeDocSearch (LangChain + Custom Retriever)
from langchain.document_loaders import TextLoader
loader = TextLoader("docs/")
docs = loader.load()
# Process with custom retriever or vector store...

# 5. Alpha Vantage Financial Tool (CrewAI)
from crewai_tools import AlphaVantageTool
av_tool = AlphaVantageTool(api_key="your_api_key")
data = av_tool.run("AAPL")

# 6. OpenWeatherMap Tool (LlamaIndex)
from llama_index.tools.weather import OpenWeatherMapToolSpec
tool_spec = OpenWeatherMapToolSpec(key="your-api-key")
agent = OpenAIAgent.from_tools(tool_spec.to_tool_list())
agent.chat("Weather in Tokyo?")

# 7. Code Interpreter (CrewAI)
from crewai_tools import CodeInterpreterTool
code_tool = CodeInterpreterTool()
output = code_tool.run("print('Hello from AI')")

# 8. AWS Lambda Kit (CrewAI)
from crewai_tools import AWSLambdaTool
lambda_tool = AWSLambdaTool(function_name="myLambdaFunction", region="us-west-2")
result = lambda_tool.run(payload={"key": "value"})

# 9. Composio Tool (CrewAI)
from crewai_tools import ComposioTool
composio = ComposioTool(api_key="your_api_key")
response = composio.run("send_email", params={"to": "test@example.com", "body": "Hello"})

# 10. CSV Search Tool (CrewAI)
from crewai_tools import CSVSearchTool
csv_tool = CSVSearchTool(file_path="data.csv")
results = csv_tool.run("Find all rows where status == 'active'")

# 11. Browser Loader (LlamaIndex)
from llama_index.readers.web import SimpleWebPageReader
reader = SimpleWebPageReader()
documents = reader.load_data(["https://example.com"])

# 12. Google Books Tool (LangChain)
from langchain.tools.google_books import GoogleBooksAPIWrapper
books_tool = GoogleBooksAPIWrapper()
books_tool.run("machine learning for beginners")

# 13. DALL·E / Vision Tool (CrewAI)
from crewai_tools import DalleTool
vision_tool = DalleTool(api_key="your_openai_api_key")
image_url = vision_tool.run("an astronaut riding a horse in space")

# 14. Shopify Tool (LlamaIndex)
from llama_index.tools.shopify import ShopifyToolSpec
shopify_tool = ShopifyToolSpec("your-store.myshopify.com", "2023-04", "your-api-key")
tools = shopify_tool.to_tool_list()

# 15. Whisper Reader (LlamaIndex)
from llama_index.readers.whisper import WhisperReader
reader = WhisperReader(model="whisper-1", api_key="your-api-key")
documents = reader.load_data("path/to/audio.mp3")


