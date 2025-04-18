from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name=driver.find_element(By.NAME,"fName")
f_name.send_keys("Sridevi")
l_name=driver.find_element(By.NAME,"lName")
l_name.send_keys("Parimi")
email=driver.find_element(By.NAME,"email")
email.send_keys("sri@gmail.com")
button=driver.find_element(By.TAG_NAME,"button")
button.click()