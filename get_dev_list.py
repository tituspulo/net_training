from get_ticket import *
from tabulate import tabulate
import requests
import urllib3
import sys

urllib3.disable_warnings()

ticket = get_aut_ticket()

headers = {'X-Auth-Token' : ticket}

url = "https://"+controller+"/api/"+version+"/network-device"
device = []

try:
    resp = requests.get(url, headers=headers, verify=False)
    status = resp.status_code
    print ("Status: ", status)

    response_json = resp.json()
    device = response_json["response"]

except:
    print ("Something went wrong with get")
    sys.exit()

if status != 200:
    print ("Somenthing went wrong", status)
    print ("Response: ", resp.text)
    sys.exit()

if device != []:
    device_list = []
    for i in device:
        device_list.append([i["hostname"], i["managementIpAddress"], i["type"], i["id"]])
else:
    print("No device!")

print(tabulate(device_list,headers=['hostname', 'ip', 'type', 'id'], tablefmt="rst"))


