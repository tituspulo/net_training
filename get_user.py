from get_ticket import *
import requests
import json
import urllib3

urllib3.disable_warnings()

ticket = get_aut_ticket()

headers = {'X-Auth-Token' : ticket}

url = "https://"+controller+"/api/"+version+"/user"

r = requests.get(url=url, headers=headers, verify=False)

response_json = r.json()

print("Status: ", r.status_code)

print(json.dumps(response_json,indent=4))

for item in response_json["response"]:
    for item1 in item["authorization"]:
        print ("User %s, role is the %s."%(item["username"],(item1["role"])[5:]))