#dependencies
#pip install selenium
from selenium import webdriver

#pip install plyer
from plyer import notification
import time

def openbrowser():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://www.google.com/')
    return driver

def tracker():
    driver = openbrowser()
    time_spent = 600
    while True:
        url = driver.current_url
        url = url[8:]
        url = url.split('.')
        # urls to track
        track_platforms = ['youtube', 'linkedin']
        if url[1] in track_platforms:
            #delay of time in seconds
            time.sleep(10)
            notification.notify(
                title=f'CUSTOM NOTIFICATION',
                message=f'You have spent {time_spent/60} mintures on {url[1].capitalize()}!',
                app_icon='clock.ico',
                timeout=5
            )
            time_spent += 600

if __name__ == '__main__':
    #calling the function
    tracker()

