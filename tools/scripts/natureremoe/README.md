# script - Nature Remo E API
Nature Remo E API を実行し、DER動作確認を実施するツールです

## 事前準備

1. Python 3 のインストール。ver 3.10.6 にて動作確認済みです。
2. APIアクセスキーの取得（利用するAPIの管理者へお問い合わせください）
3. .env の設定
4. 本ツールの実行
  - `tools/scripts` から必要なバッチファイルを実行してください 

## APIアクセスキーの取得

Nature Remo Cloud API のアクセスキーを取得し、.env に設定してください。

（個人利用向け：GETのAPIのみ利用可能です。ECHONET Lite の SET をしたい場合は Nature株式会社へお問い合わせください）
https://www.home.nature.global/

## .env の設定

Nature Remo Cloud API のアクセスキー や、Nature Remo E における DER のID情報等を指定するための .env ファイルを /tools/scripts/natureremoe/ 配下に作成してください。

### 例
以下を指定してください
```
TARGET_URL='https://api.nature.global/1/' #APIのエンドポイントURL
APPRIANCES="appliances"
DEVICES="devices"
EL_APPRIANCES="echonetlite/appliances"
API_KEY='' #Nature Remo Cloud API の APIキー
```

## 本ツールの実行
2024年3月3日現在で用意されているツールは以下のとおりです

- get_a_property.py
  - 現在のDER機器の状態を取得する
