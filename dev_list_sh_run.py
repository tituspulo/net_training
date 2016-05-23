from get_ticket import *
import requests
import urllib3
import sys
from tabulate import tabulate



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
    print ("Something went wrong", status)
    print ("Response: ", resp.text)
    sys.exit()

if device != []:
    device_list = []
    device_sh_list = []

    for i in device:
        device_list.append([i["hostname"], i["managementIpAddress"], i["type"], i["id"]])
        device_sh_list.append([i["hostname"], i["managementIpAddress"], i["type"]])

    print(tabulate(device_sh_list,headers=['hostname', 'ip', 'type'], tablefmt='rst'))

    select = True
    net_id = ""

    while select:
            user_input = input("Enter IP or Hostname:")
            user_input = user_input.replace(" ", "")
            if user_input.lower() == 'exit':
                sys.exit()
            for i in device_list:
                if user_input in i:
                    net_id = i[3]
                    select = False
                    break
            if net_id == "":
                print("No device found")

    url = "https://"+controller+"/api/v1/network_device/"+net_id+"/config"
    resp = requests.get(url=url,headers=headers,verify=False)
    status = resp.status_code
    print ("Status: ", status)

    try:
        response_json = json.loads(resp.text)
        print (response_json["response"])
    except:
        if status == 204:
            print("no content")
        else:
            print("Something wrong! \n")
            print ("Response:", json.dumps(response_json, indent=4))

else:
    print("No network device at all!")


