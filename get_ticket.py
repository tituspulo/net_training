import requests
import json
import sys
import urllib3
from tabulate import tabulate

urllib3.disable_warnings()


controller = "sandboxapic.cisco.com:9443"
username = "admin"
password = "C!sc0123"
version = "v1"

def get_aut_ticket(ip=controller,user=username,pwd=password):

    global version

    r_json = {
        "username" : user,
        "password" : pwd
    }

    url = "https://"+ip+"/api"+version+"/ticket"
    headers = {'content-type' : 'application/json'}

    try:
        response = requests.post(url=url, data=json.dumps(r_json), headers=headers, verify=False)
        return response.json() ["response"]["serviceTicket"]

    except:
        print("Status: ", response.status_code)
        print("Response: ", response.text)
        sys.exit()



