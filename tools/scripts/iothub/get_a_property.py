# 遠方操作でDER機器の状態確認（GET）
# - 引数
#   - なし
# - 動作
#   1. 指定のプロパティのGETを実施
# - 出力
#   - GET の結果をコンソールへ表示する

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
        "command_value": "operationMote" #蓄電池の運転モード
        }
      ],
      #######
      # 遠方操作対象のDER機器を指定してください（DRIVER_ID, R_EDGE_ID, THINGS_UUID）
      #######
      "driver_id": os.environ['DRIVER_ID'], 
      "r_edge_id": os.environ['R_EDGE_ID'],
      "thing_uuid": os.environ['THING_UUID_BT']
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