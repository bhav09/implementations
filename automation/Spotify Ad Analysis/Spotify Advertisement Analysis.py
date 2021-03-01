#dependencies
from selenium import webdriver #pip install selenium
import time #inbuilt
import os #inbuilt


#credentials
id = os.environ.get('Email') #if you are using for personal use, you can remove the os.environ.get.get() and write your own email id
password = os.environ.get('Password') #same is for password

driver = webdriver.Chrome('chromedriver.exe') #download the webdriver according
driver.get('https://accounts.spotify.com/en/login?continue=https://open.spotify.com/collection/tracks')
#driver.get('https://open.spotify.com/collection/tracks')

#delay of 2 seconds
time.sleep(2)

#username
login_id = driver.find_element_by_xpath('//input[@ng-model="form.username"]')
login_id.send_keys(id)

#password
login_pass = driver.find_element_by_xpath('//input[@ng-model="form.password"]')
login_pass.send_keys(password)

#button
login_button = driver.find_element_by_xpath('//button[@id="login-button"]')
login_button.click()

#delay of 12 seconds;;;; you can vary this value as per your internet connectivity.
time.sleep(12)

#play button
play_button = driver.find_element_by_xpath('//button[@data-testid="play-button"]')
driver.execute_script("arguments[0].click();", play_button) #skips the exception and lets you play the song.

#print(play_button.text)

time.sleep(5) #delay of 5 seconds

#static declarations
flag = 0
ad_time = 0
start_time,end_time = 0,0
play_time = 3  #3seconds is the default experimental value.
ad_detail = 'Advertisement'

while play_time < 3600: #here 3600 seconds is the seconds for which I want to run the loop.
#while True:
    try:
        start_iter = time.time()
        now_playing = driver.find_element_by_xpath('//div[@aria-label="Now playing: Advertisement by Spotify"]')
        #print(now_playing.text)
        if flag == 0 and ad_detail in now_playing.text:
            #print('Condition 1')
            flag = 1
            time_1 = time.time()
        elif flag == 1 and ad_detail in now_playing.text:
            #print('Condition 2')
            time_2 = time.time()
            time_diff = time_2-time_1
            ad_time += time_diff
            time_1 = time_2
        elif ad_detail not in now_playing.text:
            flag = 0
        if ad_time != 0:
            #print('Advertisement has been playing for:',ad_time,' Seconds')
            pass
    except:
        pass
    end_iter = time.time()
    play_time += (end_iter - start_iter)
    print('Play Time:',play_time)

print('Total Play Time:',play_time,' seconds.')
print('Song played for:', play_time-ad_time,' seconds.')
print('Advertisement played for ',ad_time,' seconds.')
driver.quit() #will close the automated spotify window