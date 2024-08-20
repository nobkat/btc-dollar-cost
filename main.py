import os
import argparse

from dotenv import load_dotenv

from bitflyer import Bitflyerorder
from line import LINE_message

load_dotenv()

perser = argparse.ArgumentParser()
perser.add_argument("yen_amount", type=int, help="取引量[JPY]")
args = perser.parse_args()

yen_amount = args.yen_amount

bitflyer = Bitflyerorder(
    os.environ["BITFLYER_API_KEY"], os.environ["BITFLYER_API_SECRET"]
)

jpy_balance = int(bitflyer.get_jpy_balance())
btc_price = bitflyer.get_btc_price()
btc_amount = round(yen_amount / btc_price, 8)

LINE_message(
    f""""BTCを{btc_amount}購入します。
BTCの価格:{btc_price}円
日本円残高:{jpy_balance}円
https://github.com/nobkat/btc-dollar-cost/settings/secrets/actions で実行しています。"""
)

# bitflyer.market_order("BUY", 0.001)
