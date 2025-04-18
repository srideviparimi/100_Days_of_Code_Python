from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#initial setup
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
# get the cookie element and click on it
cookie=driver.find_element(By.ID,"cookie")
now_time=time.time()
close_time=time.time()+15
end=time.time()+(10*60)
item_id_list=["buyCursor","buyGrandma","buyFactory","buyMine","buyShipment",
"buyAlchemy lab","buyPortal","buyTime machine"]
points_dict={}
run=True
while run:
   cookie.click()

   #for every 5 seconds it checks for money
   if now_time>close_time:
       money=int(driver.find_element(By.ID,"money").text.replace(",",""))
       for item_id in item_id_list:
           item=driver.find_element(By.ID,item_id)
           points=int(item.text.split("-")[1].split("\n")[0].strip().replace(",",""))
           if points<money:
               points_dict[item_id]=points
       #points_dict have the all the possible options to click with the money
       if points_dict!={}:
           max_key = max(points_dict, key=points_dict.get)
           max_element=driver.find_element(By.ID,max_key)
           max_element.click()
           cookie.click()
       close_time=time.time()+ 15
   now_time = time.time()
   if now_time > end:
       run=False
       print(driver.find_element(By.ID,"cps").text)
       break


#breaks the loop after 5 min

driver.close()

print("done")