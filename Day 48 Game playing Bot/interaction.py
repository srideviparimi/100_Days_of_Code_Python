from selenium import webdriver
from selenium.webdriver.common.by import By
#create chrome options
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
#create a driver obj
driver=webdriver.Chrome(options=chrome_options)
#open the url using get()
driver.get("https://en.wikipedia.org/wiki/Main_Page")
#now do scraping
article_count=driver.find_element(By.CSS_SELECTOR,"#articlecount > ul > li:nth-child(2) > a:nth-child(1)")
article_count.click()
