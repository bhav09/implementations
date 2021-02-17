from selenium import webdriver
import time
import os
import platform
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# credentials
id = os.environ.get('Email')
password = os.environ.get('Password')

folder_name = 'Job Details'
if not os.path.exists(f'C:/Users/91884/PycharmProjects/JD Scrapper/' + folder_name):
    os.mkdir(f'C:/Users/91884/PycharmProjects/JD Scrapper/' + folder_name)
path = 'C:/Users/91884/PycharmProjects/JD Scrapper/' + folder_name

# NewLogic to automatically pull WebDriver as per choice mentioned
driver = webdriver
browser = "CHROME"
if browser == "CHROME":
    print("Chrome Browser selected")
    globals()['driver'] = webdriver.Chrome(ChromeDriverManager().install())

elif browser == "EDGE":
    print("Edge Browser selected")

    globals()['driver'] = webdriver.Edge(EdgeChromiumDriverManager().install())
else:
    print("Invalid browser selected")

driver.get(
    'https://www.linkedin.com/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fin%2Fbhavishya-pandit%2F&fromSignIn=true&trk=public_authwall_profile-login-link')
time.sleep(2)  # delay of two seconds so as to let the site load the elements completely

# Entering username
username = driver.find_elements_by_xpath('//div[@class = "form__input--floating mt-24"]')
userid = driver.find_element_by_xpath('//input[@id= "username"]')
userid.send_keys(id)

# Entering password
login_password = driver.find_element_by_xpath('//input[@id= "password"]')
login_password.send_keys(password)

# clicking the signin button autonomously
signin_button = driver.find_element_by_xpath(
    '//button[@class="btn__primary--large from__button--floating"]')
signin_button.click()

# fetching current url
current_url = driver.current_url
job_url = 'https://www.linkedin.com/jobs/search/?currentJobId='

# infinite loop to track the activity of the user, continously.
while True:
    if current_url != driver.current_url:
        current_url = driver.current_url
        print(current_url)
        count = 0
    if job_url in current_url:
        try:
            if driver.find_element_by_xpath(
                    '//span[@class="artdeco-inline-feedback__message"]'):  # shows that you have applied
                count += 1
                if count == 1:
                    job_title = driver.find_element_by_class_name(
                        'jobs-details-top-card__job-title').text  # job title
                    company_name = driver.find_element_by_class_name(
                        'jobs-details-top-card__company-info')  # Name of the comapny
                    job_desc = driver.find_element_by_class_name(
                        'jobs-description-content__text').text  # job description
                    print(job_title, '-', company_name)
                    print(job_desc)
                    f = open(f'Job Details/{job_title}_{company_name}.txt', 'a')
                    f.writelines(job_desc)
                    # f.write('Hello')
                    f.close()
        except Exception:  # to get rid of head ache
            pass
