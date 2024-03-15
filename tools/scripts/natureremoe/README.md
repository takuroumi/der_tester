# script - Nature Remo E API
Nature Remo E API を実行し、DER動作確認を実施するツールです

## Nature Remo E について
「Nature Remo E（ネイチャーリモイー）」は、コンセントに挿すだけで安価で手軽に導入できるスマホHEMSです。電力の消費状況や電力料金の目安、太陽光発電設備の発電・売電状況、蓄電池の充電量・放電量をリアルタイムにスマートフォンの「Nature Remoアプリ」で確認でき、外出先から蓄電池やV2Hのコントロールも可能です。また、スマートリモコン 「Nature Remo」シリーズ（別売）と組み合わせて使用することで、電力使用量に合わせた家電の自動制御が可能になります。なお、「Nature Remo E」は、通信プロトコル「ECHONET Lite」で機器と通信します。
詳細は Nature株式会社 のWebページをご確認ください。

Nature Remo E ： https://shop.nature.global/products/nature-remo-e-1
Nature Remo E API : https://developer.nature.global/docs/nature-remo-e-api-specification/

## 事前準備

1. Python 3 のインストール。ver 3.10.6 にて動作確認済みです。
2. APIアクセスキーの取得
3. .env の設定
4. 本ツールの実行
  - `tools/scripts` から必要なバッチファイルを実行してください 

## APIアクセスキーの取得

Nature Remo Cloud API のアクセスキーを取得し、.env に設定してください。

個人利用向け：ECHONET Lite のGETのAPIは、個人利用可能です。以下Webサイトから認可を行い、アクセストークンを取得してください。
https://www.home.nature.global/

ECHONET Lite の SET をしたい場合は別途 Nature株式会社からの許可が必要です。Nature株式会社へお問い合わせください
https://nature.global/business/

## .env の設定

Nature Remo Cloud API のアクセスキー や、Nature Remo E における DER のID情報等を指定するための .env ファイルを `/tools/scripts/natureremoe/` 配下に作成してください。

### 例
以下を指定してください
```
TARGET_URL='https://api.nature.global/1/' #APIのエンドポイントURL
APPRIANCES="appliances"
DEVICES="devices"
EL_APPRIANCES="echonetlite/appliances"
SET_EPC="/refresh HTTP/1.1"
API_KEY='' #Nature Remo Cloud API の APIキー
```

## 本ツールの実行
2024年3月3日現在で用意されているツールは以下のとおりです

- get_a_property.py
  - 現在のDER機器の状態を取得する
- refresh_and_get.py
  - HEMSから現在のDER機器の最新値の状態を取得してサーバーへ送信、その最新値を取得する