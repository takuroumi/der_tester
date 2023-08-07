import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = os.environ['TARGET_URL']

payload = {
  "requests": [
    {
      "command": [
        {
        "command_type": "character",
        "command_code": "get_property_value",
        "command_value": "operationMode"#"instantaneousElectricPower"#"chargingElectricPower"#"remainingCapacity3"#"targetTemperature"#"operationMode"#"operationStatus=ON"
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

response = requests.request("POST", url, headers=headers, json=payload)

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