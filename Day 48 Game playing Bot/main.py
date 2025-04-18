from selenium import webdriver
from selenium.webdriver.common.by import By
#selenium driver is a bridge between the chrome browser and python code
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
ul_items=driver.find_elements(By.XPATH,'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li')
dict_of_events={}
no=0
for element in ul_items:
    date=element.find_element(By.TAG_NAME,"time").text
    event_name=element.find_element(By.TAG_NAME,"a").text
    el={"time":date,"name":event_name}
    dict_of_events[no]=el
    no+=1
print(dict_of_events)
driver.close()


