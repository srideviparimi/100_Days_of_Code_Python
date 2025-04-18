import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#getting environment variables
load_dotenv()
EMAIL=os.getenv("EMAIL")
PASSWORD=os.getenv("PASSWORD")
#chrome options and chrome driver setup
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
#getting access to the page using URL
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4211945212&f_AL=true&f_TPR=r86400&geoId=104769905&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&spellCorrectionEnabled=true")
#selecting sign in button
time.sleep(2)
sign_in_button=driver.find_element(By.XPATH,'//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in_button.click()
#fill the form and submit
time.sleep(2)
user=driver.find_element(By.CSS_SELECTOR,"#base-sign-in-modal_session_key")
user.send_keys(EMAIL)
password=driver.find_element(By.CSS_SELECTOR,"#base-sign-in-modal_session_password")
password.send_keys(PASSWORD)
submit=driver.find_element(By.CSS_SELECTOR,"#base-sign-in-modal > div > section > div > div > form > div.flex.justify-between.sign-in-form__footer--full-width > button")
submit.click()

#easy apply to job
time.sleep(2)
easy_apply_button=driver.find_element(By.XPATH,'//*[@id="jobs-apply-button-id"]')
easy_apply_button.click()

#next button click
time.sleep(2)
next_btn=driver.find_element(By.CSS_SELECTOR,'#ember349 > span')
next_btn.click()

#second time click
next_btn.click()

#additional questions
q_1=driver.find_element(By.XPATH,'//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4211945212-16790660090-numeric"]')
q_1.send_keys("1")
q_2=driver.find_element(By.XPATH,'//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4211945212-16790660058-numeric"]')
q_2.send_keys("1")
q_3=driver.find_element(By.XPATH,'//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4211945212-16790660082-numeric"]')
q_3.send_keys("1")
btn=driver.find_element(By.XPATH,'//*[@id="ember359"]/span').click()
