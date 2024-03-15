# V2H の運転モードの切り替えをした際の、ICT応答と機器の現在状態を確認する
# - 実行時引数
#   - なし
# - 動作
#   1. コード中で指定された運転モードについて、あらかじめ GET をする
#   2. コード中で指定された運転モードへ、SET をする
#   3. 20秒間WAITしたあとに、再度 GET をして SET 結果を確認する
# - 出力
#   - GET, SETの状態出力

import requests
import json
import os
from dotenv import load_dotenv
import time
# import sys

load_dotenv()

url = os.environ['TARGET_URL']

payload_get = {
  "requests": [
    {
      "command": [
        {
        "command_type": "character",
        "command_code": "get_property_value",
        "command_value": "operationMode"
        }
      ],
      "driver_id": os.environ['DRIVER_ID'],
      "r_edge_id": os.environ['R_EDGE_ID'],
      "thing_uuid": os.environ['THING_UUID']
    }
  ]
}

payload_set = {
  "requests": [
    {
      "command": [
        {
        "command_type": "character",
        "command_code": "set_property_value",
        "command_value": "operationMode=charge" # ここを変更してください（charge, discharge, idle, standby）
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

try:
    response_get1 = requests.request("POST", url, headers=headers, json=payload_get, timeout=10)
    print(response_get1.text)
    jsonData = response_get1.json()

    get1 = {
    'command_code': jsonData['results'][0]["command"][0]["command_code"],
    'command_value': jsonData['results'][0]["command"][0]["command_value"],
    'response_result': jsonData['results'][0]["command"][0]["response"][0]["response_result"],
    'response_value': jsonData['results'][0]["command"][0]["response"][0]["response_value"]
    }

    print(get1["command_code"]  + " (" + get1["command_value"] + ") ..." + 
    get1["response_result"] + " (" + get1["response_value"] + ")")

except TimeoutError:
    print("get1 is timed out")
    pass

try:
    response_set = requests.request("POST", url, headers=headers, json=payload_set, timeout=20)
    # print(response_set.text)
    jsonData = response_set.json()

    set1 = {
    'command_code': jsonData['results'][0]["command"][0]["command_code"],
    'command_value': jsonData['results'][0]["command"][0]["command_value"],
    'response_result': jsonData['results'][0]["command"][0]["response"][0]["response_result"],
    'response_value': jsonData['results'][0]["command"][0]["response"][0]["response_value"]
    }

    print(set1["command_code"]  + " (" + set1["command_value"] + ") ..." + 
    set1["response_result"] + " (" + set1["response_value"] + ")")

except TimeoutError:
    print("set is timed out")
    pass

print("wait 20 seconds ...)")
time.sleep(20)

try:
    response_get2 = requests.request("POST", url, headers=headers, json=payload_get, timeout=5)
    jsonData = response_get2.json()

    get2 = {
    'command_code': jsonData['results'][0]["command"][0]["command_code"],
    'command_value': jsonData['results'][0]["command"][0]["command_value"],
    'response_result': jsonData['results'][0]["command"][0]["response"][0]["response_result"],
    'response_value': jsonData['results'][0]["command"][0]["response"][0]["response_value"]
    }

    print(get2["command_code"]  + " (" + get2["command_value"] + ") ..." + 
    get2["response_result"] + " (" + get2["response_value"] + ")")
except TimeoutError:
    print("get2 is timed out")
    pass

print("Please check the value is set as set by set_property_value")
