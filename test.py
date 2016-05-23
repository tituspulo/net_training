from get_ticket import *
import requests
import urllib3
import json

urllib3.disable_warnings()

ticket = get_aut_ticket()
headers = {'X-Auth-Token' : ticket}

net_id = 'ed95de0f-88fc-4c53-8cb8-4965fa04f0d2'
url = "https://"+controller+"/api/v1/network-device/"+net_id+"/config"
resp = requests.get(url=url,headers=headers,verify=False)
status = resp.status_code
data = resp.json()
print ("Status: ", status)
print (data["response"])