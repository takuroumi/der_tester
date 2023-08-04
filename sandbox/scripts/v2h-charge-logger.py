import requests
import json
import os
from dotenv import load_dotenv
import time, datetime
import threading

load_dotenv()

url = os.environ['TARGET_URL']

payload0 = {
  "requests": [
    {
      "command": [
        {
        "command_type": "character",
        "command_code": "get_property_value",
        "command_value": "operationMode"#"chargingElectricPower"#"remainingCapacity3"#"targetTemperature"#"operationMode"#"operationStatus=ON"
        }
      ],
      "driver_id": os.environ['DRIVER_ID'],
      "r_edge_id": os.environ['R_EDGE_ID'],
      "thing_uuid": os.environ['THING_UUID']
    }
  ]
}


payload1 = {
  "requests": [
    {
      "command": [
        {
        "command_type": "character",
        "command_code": "get_property_value",
        "command_value": "instantaneousElectricPower"#"chargingElectricPower"#"remainingCapacity3"#"targetTemperature"#"operationMode"#"operationStatus=ON"
        }
      ],
      "driver_id": os.environ['DRIVER_ID'],
      "r_edge_id": os.environ['R_EDGE_ID'],
      "thing_uuid": os.environ['THING_UUID']
    }
  ]
}

payload2 = {
  "requests": [
    {
      "command": [
        {
        "command_type": "character",
        "command_code": "get_property_value",
        "command_value": "remainingCapacity3"#"targetTemperature"#"operationMode"#"operationStatus=ON"
        }
      ],
      "driver_id": os.environ['DRIVER_ID'],
      "r_edge_id": os.environ['R_EDGE_ID'],
      "thing_uuid": os.environ['THING_UUID']
    }
  ]
}


headers = {
  "Content-type": "application/json",
  "Authorization": "Bearer "+os.environ['ACCESS_TOKEN'],
  "X-IOT-API-KEY": os.environ['API_KEY']
}

def getRequest(pl):
    response = requests.request("POST", url, headers=headers, json=pl)

    # print(response.text)
    jsonData = response.json()

    jsonDict = {
    'command_code': jsonData['results'][0]["command"][0]["command_code"],
    'command_value': jsonData['results'][0]["command"][0]["command_value"],
    'response_result': jsonData['results'][0]["command"][0]["response"][0]["response_result"],
    'response_value': jsonData['results'][0]["command"][0]["response"][0]["response_value"]
    }

    print(jsonDict["command_code"]  + " (" + jsonDict["command_value"] + ") " + 
    jsonDict["response_result"] + " (" + jsonDict["response_value"] + ")")


def getRequests():

    print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y/%m/%d %H:%M:%S'))

    getRequest(payload0)

    time.sleep(5)

    getRequest(payload1)

    time.sleep(5)

    getRequest(payload2)

def scheduler(interval, f, wait = True):
    base_time = time.time()
    next_time = 0
    while True:
        t = threading.Thread(target = f)
        t.start()
        if wait:
            t.join()
        next_time = ((base_time - time.time()) % interval) or interval
        time.sleep(next_time)

scheduler(60, getRequests, True)