# script - IoT-HUB 
IoT-HUB API を実行し、DER動作確認を実施するツールです

## 事前準備

1. Python 3 のインストール。ver 3.10.6 にて動作確認済みです。
2. APIアクセスキーの取得（利用するAPIの管理者へお問い合わせください）
3. .env の設定
3. 本ツールの実行
  - `tools/scripts` から必要なバッチファイルを実行してください 

## APIアクセスキーの取得

IoT-HUB API のアクセスキーを取得し、.env に設定してください。


## .env の設定

IoT-HUB API のアクセスキー や、IoT-HUB における DER のID情報等を指定するための .env ファイルを /tools/scripts/iothub/ 配下に作成してください。

### 例
TARGET_URL='' #APIのエンドポイントURL
DRIVER_ID='' #IoT-HUB ドライバーのID
R_EDGE_ID='' #IoT-HUB エッジのID
THING_UUID='' #IoT-HUB の各DER機器のUUID
THING_UUID_1F_T=''
THING_UUID_2F_S=''
API_KEY='' #IoT-HUB の APIキー
ACCESS_TOKEN='' #IoT-HUB API実行のためのアクセストークン

## 本ツールの実行
2023年11月27日現在で用意されているツールは以下のとおりです

- aircon-ref-temp-checker.py
  - エアコンの設定温度を変更して状態取得（SET＆GETの繰り返し）し、設定可能なエアコン温度を確認する
- v2h-charge-logger.py
  - V2H の運転モード・充電電力・SOCを定期取得し、DERの操作に対する状態変化を確認する
- v2h-operation-mode-checker.py
  - V2H の運転モードの切り替えをした際の、ICT応答と機器の現在状態を確認する
- set_and_get.py
  - 遠方操作でDER機器をSETした項目の状態確認
