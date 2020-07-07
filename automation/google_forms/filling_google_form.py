from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

#driver = webdriver.Chrome(ChromeDriverManager().install())
#webdriver = webdriver.Chrome('https://www.google.com/')
#https://docs.google.com/forms/d/e/1FAIpQLScEisDvLpMWSXQI8r4r-beJ7kjbEgKzGFFFjtf7Hfp815VLTw/viewform
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"))
driver.get('https://docs.google.com/forms/d/e/1FAIpQLScEisDvLpMWSXQI8r4r-beJ7kjbEgKzGFFFjtf7Hfp815VLTw/viewform')

name_of = input('Enter name:')
email_id = input('Enter Email id:')
contact = input('Enter contact Details:')
college = input('College Name:')
expectations = 'That is going to be a great one !'

print('Name:',name_of)
print('Email id:',email_id)
print('Contact is:',contact)
print('College:',college)

name = driver.find_element_by_xpath('//input[@aria-describedby = "i2 i3"]')
name.send_keys(name_of)

email = driver.find_element_by_xpath('//input[@type = "email"]')
email.send_keys(email_id)

contact_details = driver.find_element_by_xpath('//input[@aria-describedby = "i10 i11"]')
contact_details.send_keys(contact)

univ_name = driver.find_element_by_xpath('//input[@aria-describedby = "i14 i15"]')
univ_name.send_keys(college)

expectations_from = driver.find_element_by_xpath('//textarea[@aria-describedby = "i18 i19"]')
expectations_from.send_keys(expectations)

submit = driver.find_element_by_class_name('appsMaterialWizButtonPaperbuttonContent')
submit.click()


