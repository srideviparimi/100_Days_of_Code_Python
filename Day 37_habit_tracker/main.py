import requests
from datetime import datetime as dt
import os
from dotenv import load_dotenv
load_dotenv()
USERNAME=os.getenv("USERNAME")
TOKEN=os.getenv("TOKEN")
pixela_url="https://pixe.la/v1/users"
params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
response=requests.post(url=pixela_url,json=params)
#print(response.text)
#user name is created
graph_endpoint=f"{pixela_url}/{USERNAME}/graphs"
GRAPH_ID="graph1"
graph_params={
    "id":GRAPH_ID,
    "name":USERNAME,
    "unit":"minutes",
    "type":"int",
    "color":"ajisai"
}
headers={
    "X-USER-TOKEN":TOKEN
}
#requests.post(url=graph_endpoint,json=graph_params,headers=headers)
#successfully created a graph
#now posting the pixel to the graph
date=dt.now()
today=date.strftime("%Y%m%d")
pixel_endpoint=f"{pixela_url}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_params={
    "date":today,
    "quantity":"50"
}

#response=requests.post(url=pixel_endpoint,json=pixel_params,headers=headers)
#print(response.text)
put_params={
    "quantity":"35"
}
put_endpoint=f"{pixela_url}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
put_response=requests.put(url=put_endpoint,json=put_params,headers=headers)
print(put_response.text)

delete_response=requests.delete(url=put_endpoint,headers=headers)
print(delete_response)
#you can see the result in the browser using the endpoint of
#https://pixe.la/v1/users/{USERNAME}/graphs/{graph_id}.html