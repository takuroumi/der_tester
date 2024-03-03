# 遠方操作でDER機器の状態確認（GET）
# - 引数
#   - なし
# - 動作
#   1. GETを実施
# - 出力
#   - GET の結果をコンソールへ表示する

import requests
import json
import os
from dotenv import load_dotenv
import time

load_dotenv()

url = os.environ['TARGET_URL']+os.environ['EL_APPRIANCES'] #"https://api.nature.global/1/" + "echonetlite/appliances"

headers = {
  "Content-type": "application/json",
  "Authorization": "Bearer "+os.environ['ACCESS_TOKEN'],
}

try:
    response_get1 = requests.request("GET", url, headers=headers, timeout=10)
    # print(response_get1.text)
    jsonData = response_get1.json()

    #appliances には Nature Remo E へ登録した家電の一覧が配列で返されるため、番号の確認が必要
    get1 = {
    'name': jsonData["appliances"][0]["nickname"],
    'type': jsonData["appliances"][0]["type"],
    'propertioes': jsonData["appliances"][0]["properties"]
    }

    print(get1)

except TimeoutError:
    print("get1 is timed out")
    pass