# 設定温度を変更して状態確認（SET＆GETの繰り返し）
# - 引数
#   - SET内容（EPC、値）
#   - GET間隔（秒数）
# - 動作
#   1. 引数のSET内容の事前GETを実施
#   2. 引数のSET内容をもとにSET信号を送信
#   3. 引数の間隔だけWAITしたあとに、GET信号を送信
# - 出力
#   - SET前後のGET結果を比較した結果を表示する
#   - 状況変化が発生していたらＯＫ，変わっていなかったらＮＧ？
#     - 表現の仕方は考える

import requests
import json
import os
from dotenv import load_dotenv
import time, datetime
import threading

load_dotenv()

url = os.environ['TARGET_URL']
i = 0

payload0 = {
  "requests": [
    {
      "command": [
        {
        "command_type": "character",
        "command_code": "get_property_value",
        "command_value": "targetTemperature"
        }
      ],
      "driver_id": os.environ['DRIVER_ID'],
      "r_edge_id": os.environ['R_EDGE_ID'],
      "thing_uuid": os.environ['THING_UUID_2F_S']
    }
  ]
}

payload1 = {
  "requests": [
    {
      "command": [
        {
        "command_type": "character",
        "command_code": "set_property_value",
        "command_value": "targetTemperature=25"
        }
      ],
      "driver_id": os.environ['DRIVER_ID'],
      "r_edge_id": os.environ['R_EDGE_ID'],
      "thing_uuid": os.environ['THING_UUID_2F_S']
    }
  ]
}

targetTemperatures = {
    "0": 17,
    "1": 17.5,
    "2": 18,
    "3": 18.5,
    "4": 19,
    "5": 20,
    "6": 21,
    "7": 22,
    "8": 23,
    "9": 24,
    "10": 25,
    "11": 26,
    "12": 27,
    "13": 28,
    "14": 29,
    "15": 30,
    "16": 31,
    "17": 31.5,
    "18": 32,
    "19": 32.5,
    "20": 33
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
    global i
    print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y/%m/%d %H:%M:%S'))
    # global payload1
    
    # print(payload1['requests'][0]['command'][0]['command_value'])
    payload1['requests'][0]['command'][0]['command_value']= "targetTemperature=" + str(targetTemperatures[str(i)])
    print(i)
    i+=1

    getRequest(payload0)

    time.sleep(5)

    getRequest(payload1)

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

scheduler(10, getRequests, True)
