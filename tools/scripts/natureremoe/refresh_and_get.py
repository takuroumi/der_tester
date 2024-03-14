# 遠方操作でDER機器のプロパティの最新値を取得し、状態確認（refresh & GET）
# - 引数
#   - なし
# - 動作
#   1. GETを実施
#   2. refresh POSTを実施
#   3. GETを実施
# - 出力
#   - GET の結果をコンソールへ表示する

import requests
import json
import os
from dotenv import load_dotenv
import time

load_dotenv()

get_url = os.environ['TARGET_URL']+os.environ['EL_APPRIANCES'] #"https://api.nature.global/1/" + "echonetlite/appliances"
refresh_url = os.environ['TARGET_URL']+os.environ['EL_APPRIANCES'] #"https://api.nature.global/1/" + "echonetlite/appliances/ のちほど文字列を足す
refresh_target_epc = "epc=a0,a4"

get_headers = {
  "Content-type": "application/json",
  "Authorization": "Bearer "+os.environ['ACCESS_TOKEN'],
}

refresh_headers = {
  "Content-type": "application/json",
  "Authorization": "Bearer "+os.environ['ACCESS_TOKEN'],
#   "epc": "a0,a4" #カンマ区切りで指定
}

refresh_data = {
    "epc": "a0" #複数指定したい場合は、カンマ区切りで指定
}

# get1
print("GET1")

try:
    response_get1 = requests.request("GET", get_url, headers=get_headers, timeout=10)
    # print(response_get1.text)
    jsonData = response_get1.json()

    #appliances には Nature Remo E へ登録した家電の一覧が配列で返されるため、番号の確認が必要
    get1 = {
    'id': jsonData["appliances"][2]["id"],
    'name': jsonData["appliances"][2]["nickname"],
    'type': jsonData["appliances"][2]["type"],
    'propertioes': jsonData["appliances"][2]["properties"]
    }

    print(get1)

    refresh_url += "/"+get1["id"]+os.environ['SET_EPC']+' '+os.environ['HTTP'] #"https://api.nature.global/1/echonetlite/appliances" + "/$uuid/refresh"+ " HTTP/1.1"
    # print(refresh_url)

except TimeoutError:
    print("get1 is timed out")
    pass

time.sleep(5)

# refresh
print("REFRESH")

try:
    # response_refresh = requests.request("POST", refresh_url, headers=refresh_headers, timeout=10)
    response_refresh = requests.post(refresh_url, headers=refresh_headers, data=refresh_data, timeout=10)
    jsonData = response_refresh.json()

    print(jsonData)

except TimeoutError:
    print("refresh is timed out")
    pass

time.sleep(5)

# get2
print("GET2")

try:
    response_get2 = requests.request("GET", get_url, headers=get_headers, timeout=10)
    jsonData = response_get2.json()

    #appliances には Nature Remo E へ登録した家電の一覧が配列で返されるため、番号の確認が必要
    get2 = {
    'id': jsonData["appliances"][2]["id"],
    'name': jsonData["appliances"][2]["nickname"],
    'type': jsonData["appliances"][2]["type"],
    'propertioes': jsonData["appliances"][2]["properties"]
    }

    print(get2)

except TimeoutError:
    print("get2 is timed out")
    pass
