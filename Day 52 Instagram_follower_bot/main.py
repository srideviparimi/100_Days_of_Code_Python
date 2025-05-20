from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from dotenv import load_dotenv
import os
import time
#got all the environment constants
load_dotenv()
USERNAME=os.getenv("USERNAME")
PASSWORD=os.getenv("PASSWORD")
SIMILAR_ACC=os.getenv("SIMILAR_ACCOUNT")

class InstaFollower:
    def __init__(self):
    #driver object is ready
        self.chrome_options=webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach",True)
        self.driver=webdriver.Chrome(options=self.chrome_options)
    def login(self):
        # get the instagram page
        self.driver.get("https://www.instagram.com/accounts/login/")

        #check if cookies are present
        self.decline_cookies=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
        )
        if self.decline_cookies:
            self.decline_cookies[0].click()
        #get the credentials
        self.user = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        self.password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        self.login_btn = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]')
        # add the credentials
        self.user.send_keys(USERNAME)
        self.password.send_keys(PASSWORD)
        self.login_btn.send_keys(Keys.ENTER)
        try:
            #if there is a login prompt to save your information then we ignore it
            self.login_prompt=WebDriverWait(self.driver,5).until(
                EC.presence_of_element_located(By.XPATH,"//div[contains(text(), 'Not now')]")
            )
            if self.login_prompt:
                self.login_prompt.click()
            #if there is any notifications prompt
            self.notification=WebDriverWait(self.driver,5).until(
                EC.presence_of_element_located(By.XPATH,"// button[contains(text(), 'Not Now')]")
            )
            if self.notification:
                self.notification.click()
        except NoSuchElementException:
            pass


    def find_followers(self):
        self.driver.get(f'https://www.instagram.com/{SIMILAR_ACC}/followers')
        self.modal=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        )
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop=arguments[0].scrollHeight",self.modal)
            time.sleep(2)

    def follow(self):
        self.all_btns=self.driver.find_elements(By.CSS_SELECTOR,'._aano button')
        for button in self.all_btns:
            try:
                button.click()
                time.sleep(1.1)
            except ElementClickInterceptedException:
                cancel_btn=self.driver.find_element(By.XPATH,'//button[contains(text(),"Cancel")]')
                cancel_btn.click()


