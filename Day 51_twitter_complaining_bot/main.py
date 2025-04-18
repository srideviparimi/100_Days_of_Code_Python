from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
import time
class InternetSpeedTwitterBot:
    def __init__(self,UP,DOWN):
        self.chrome_options=webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach",True)
        self.driver=webdriver.Chrome(options=self.chrome_options)
        self.up=0
        self.down=0
    def get_internet_speed(self,url):
        self.driver.get(url)
        time.sleep(3)
        go=self.driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[1]/a/span[4]')
        go.click()
        '''the website is checking the speed now which may take upto 60 seconds, so I am 
        sleeping for 60 seconds'''
        time.sleep(60)
        self.down=WebDriverWait(self.driver,30).until(
            EC.presence_of_element_located(By.XPATH,
                                           value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        )

        self.up=WebDriverWait(self.driver,30).until(
            EC.presence_of_element_located(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        )
        print(f"down :{self.down}")
        print(f"up: {self.up}")


    def tweet_to_provider(self,UP,DOWN,EMAIL,PASSWORD):
        try:
            self.driver.get("https://x.com/?lang=en")
            #signing up with x account
            x_signin=WebDriverWait(self.driver,5).until(
                EC.presence_of_element_located(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a')
            )
            x_signin.click()
            #wait for 5 sec and fillout the form to signin
            time.sleep(5)
            email=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
            email.send_keys(EMAIL)
            next_btn=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
            next_btn.click()
            password=self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
            password.send_keys(PASSWORD)
            #compose a tweet
            time.sleep(5)
            tweet_compose = self.driver.find_element(By.XPATH,
                                                     value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
            tweet_button = self.driver.find_element(By.XPATH,
                                                   value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')

            tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {DOWN}down/{UP}up?"
            tweet_compose.send_keys(tweet)
            time.sleep(3)
            tweet_button.click()

        except NoSuchElementException:
            print("some element is missing")

        finally:
            self.driver.quit()


if __name__ == '__main__':
    load_dotenv()
    UP=os.getenv("PROMISED_UP")
    DOWN=os.getenv("PROMISED_DOWN")
    URL=os.getenv("TEST_URL")
    EMAIL=os.getenv("TWITTER_EMAIL")
    PASSWORD=os.getenv("TWITTER_PASSWORD")
    speed_bot=InternetSpeedTwitterBot(UP=UP,DOWN=DOWN)
    #now call the get internet speed method
    speed_bot.get_internet_speed(URL)
    #now call the tweet to provider method to tweet with the promised speeds
    speed_bot.tweet_to_provider(UP=UP,DOWN=DOWN,EMAIL=EMAIL,PASSWORD=PASSWORD)







