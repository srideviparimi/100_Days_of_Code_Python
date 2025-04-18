from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
#driver is created
chrome_options=webdriver.ChromeOptions
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
#get the tinder page
driver.get("http://www.tinder.com")

#get login button
time.sleep(2)
login_button=driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

#facebook login
time.sleep(2)
fb_login_driver=driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login_driver.click()

#a new window is opened , we can get the windows from the method window_handles
base_window=driver.window_handles[0]
fb_window=driver.window_handles[1]

#we switch to fb window and fill out the form to login
driver.switch_to(fb_window)
print(driver.title)#shows the title of window in which the driver is currently on

#settings
allow_location=driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location.click()

notification=driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notification.click()

cookies=driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

#tinder for free tier only allows 100 clicks per day
for n in range(100):
    time.sleep(1)
    try:
        like_button = driver.find_element(By.XPATH, value=
        '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except NoSuchElementException:
        time.sleep(2)
driver.quit()