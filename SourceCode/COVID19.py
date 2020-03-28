# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 19:52:06 2020

@author: Malay
"""
import http.client
# import requests
import json
import pandas as pd 


conn = http.client.HTTPSConnection("covid-193.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "8cd8a8ba13mshf5068b192883d64p12cdb3jsn0bf8df5217b3"
    }

conn.request("GET", "/statistics", headers=headers)

res = conn.getresponse()

data = res.read()

json_data = json.loads(data)
json_output= json.dumps(json_data, indent=2, sort_keys=True)

#print (json.dumps(json_data, indent=2, sort_keys=True))

with open("Ponga_pandit.json", "w") as outfile: 
    outfile.write(json_output)
    
pd.read_json('Ponga_pandit.json').to_csv('output.csv')

#print ("JSON created successfully")


#print("API output obtained  for PONGA PONDIT")

