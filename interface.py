from get_ticket import *
from tabulate import tabulate
import urllib3

urllib3.disable_warnings()

ticket = get_aut_ticket()
headers = {"X-Auth-Token" : ticket}

url = "https://"+controller+"/api/"+version+"/network-device"
device = []

try:
    resp = requests.get(url = url, headers = headers, verify = False)
    status = resp.status_code
    print ("Status: ", status)
    data = resp.json()
    device = data["response"]

except:
    print ("cannot get device info.")

if status != 200:
    print("Response status is %s, something wrong."%status)
    print(data.text)

if device != []:
    select = True
    while select:
        user_input = raw_input("Please enter: \n 1 - get a list of interfaces of device \n 2 - get config of device \n Enter your selection: ")
        user_input = user_input.replace(" ","")
        if user_input.lower == 'exit':
            sys.exit()
        if user_input == '1' or user_input == '2':
            select = False
        else:
            print("Sorry, wrong selection, please enter 1 or 2, or exit to escape")

    device_list = []
    device_show_list = []

    for item in device:
        device_list.append([item["hostname"], item["managementIpAddress"], item["type"], item["instanceUuid"]])
        device_show_list.append([item["hostname"], item["managementIpAddress"], item["type"]])

    print(tabulate(device_show_list, headers=['hostname', 'IP', 'Model'], tablefmt='rst'))

    net_id = ""
    select = True
    while select:
        if user_input == '1':
            sec_input = raw_input("Enter device IP or hostname to show interface info:")
        else:
            sec_input = raw_input("Enter device IP or hostname to show config:")
        sec_input = sec_input.replace(" ","")
        if sec_input.lower() == 'exit':
            sys.exit()
        for item in device_list:
            if sec_input in item:
                net_id = item[3]
                select = False
                break
        if net_id == "":
            print("No IP or hostname found")

    if user_input == '1':
        url = "https://"+controller+"/api/"+version+"/interface/network-device/"+net_id
    else:
        url = "https://"+controller+"/api/"+version+"/network-device/"+net_id+"/config"

    response = requests.get(url=url, headers=headers, verify=False)
    status = response.status_code
    print("Status:", status)

    try:
        data = response.json()
        if user_input == '1':
            print (json.dumps(data))
        if user_input == '2':
            print (data["response"].replace("\r\n","\n"))
    except:
        if status == 204:
            print ("No content")
        else:
            print ("Something wrong in selection")
            print ("Response:\n", json.dumps(data,indent=4))

else:
    print("No network device found")




