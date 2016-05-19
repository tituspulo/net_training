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
print (ticket_json["response"]["serviceTicket"])