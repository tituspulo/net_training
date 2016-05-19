import requests
import json


def get_aut_ticket(ip,user,pwd):

    r_json = {
        "username" : user,
        "password" : pwd
    }

    url = "https://"+ip+"/api/v1/ticket"
    headers = {'content-type' : 'application/json'}


    response = requests.post(url=url, data=json.dumps(r_json), headers=headers, verify=False)
    return response.json() ["response"]["serviceTicket"]





