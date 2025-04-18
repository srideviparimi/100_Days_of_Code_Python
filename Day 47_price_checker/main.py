import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
my_email=os.getenv("MY_EMAIL")
password=os.getenv("PASSWORD")
#get the data from the site
#url="https://appbrewery.github.io/instant_pot/"

url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
headers={
    "Accept-Language":"en-US",
    "User-Agent":'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36'
}
response=requests.get(url=url,headers=headers)
response.raise_for_status()
#create a soup objects and find the required element
soup=BeautifulSoup(response.text,"lxml")
result=soup.find(name="span", class_="aok-offscreen")
#got the price
price=result.getText().split("$")[1]
try:
    price=float(price)
except:
    price=float(price.split(" ")[0])

res=soup.find(name="span",class_="aok-offscreen")
print(res)
name=res.getText()
target_price=100.00



if price<target_price:
    message = f"Subject:Low Price Alert!! \n\n Great offer ! Your favorite {name} is available only for ${price}. Check it out at \n\n{url}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,
                            msg=message.encode("utf-8"))
        print("done")


