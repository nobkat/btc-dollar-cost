import os
import requests
from dotenv import load_dotenv

load_dotenv()


# LINE Notifyのアクセストークンを定義
token = os.environ["LINE_NOTIFY_TOKEN"]


# LINEメッセージ送信の関数
def LINE_message(msg):
    # APIエンドポイントのURLを定義
    url = "https://notify-api.line.me/api/notify"
    # HTTPリクエストヘッダーの設定
    headers = {"Authorization": "Bearer " + token}
    # 送信するメッセージの設定
    message = msg
    # ペイロードの設定
    payload = {"message": message}
    # POSTリクエストの使用
    r = requests.post(url, headers=headers, params=payload)


if __name__ == "__main__":
    # 関数の呼び出し
    LINE_message("通知だよ!")
