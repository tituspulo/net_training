import requests
import json
import urllib3

urllib3.disable_warnings()

controller = "sandboxapic.cisco.com:9443"
username = "admin"
password = "C!sc0123"
version = "v1"

r_json = {
    "username" : username,
    "password" : password
}

post_url = "https://"+controller+"/api/"+version+"/ticket"
headers = {'content-type' : 'application/json'}

resp = requests.post(url=post_url, data=json.dumps(r_json), headers=headers, verify=False)

ticket_json = resp.json()
ticket = (ticket_json["response"]["serviceTicket"])

headers = {'X-Auth-Token' : ticket}

url = "https://"+controller+"/api/"+version+"/user"

r = requests.get(url=url, headers=headers, verify=False)

response_json = r.json()

print("Status: ", r.status_code)

print(json.dumps(response_json,indent=4),'\n')

for item in response_json["response"]:
    for item1 in item["authorization"]:
        print("Role user is the ", (item["username"],(item1["role"])[5:]))