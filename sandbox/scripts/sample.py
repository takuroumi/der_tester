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
        "command_code": "set_property_value",
        "command_value": "operationStatus=OFF"
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

print(response.text)