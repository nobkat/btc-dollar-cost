import pybitflyer


class Bitflyerorder:
    # 現物の場合: "BTC_JPY" / 先物の場合: "FX_BTC_JPY"
    code = "BTC_JPY"

    def __init__(self, api_key, api_secret):
        #
        self.public_api = pybitflyer.API()
        self.api = pybitflyer.API(api_key, api_secret)
        self.product_code = self.code

    def get_btc_balance(self):
        """
        残高取得関数
        """
        balance = self.api.getbalance(product_code=self.product_code)
        for b in balance:
            if b["currency_code"] == "BTC":
                return b["amount"]

    def get_jpy_balance(self):
        """
        残高取得関数
        """
        balance = self.api.getbalance(product_code=self.product_code)
        for b in balance:
            if b["currency_code"] == "JPY":
                return b["amount"]

    def get_btc_price(self):
        """
        板情報取得関数
        """
        tick = self.api.ticker(product_code=self.product_code)
        return tick["ltp"]

    def market_order(self, side, size, time_to_expire=1):
        """
        成行注文関数
        :param side: 売買方向
        :param size: 取引量
        :param time_to_expire:注文寿命
        """
        res = self.api.sendchildorder(
            product_code=self.product_code,
            child_order_type="MARKET",
            minute_to_expire=time_to_expire,
            side=side,
            size=size,
            price=0,
        )
        if "error_message" in res:
            raise Exception(res["error_message"])

    def limit_order(self, side, price, size, time_to_expire=1):
        """
        指値注文関数
        :param side: 売買方向
        :param price: 価格
        :param size: 取引量
        :param time_to_expire:注文寿命
        """

        res = self.api.sendchildorder(
            product_code=self.product_code,
            child_order_type="LIMIT",
            minute_to_expire=time_to_expire,
            side=side,
            size=size,
            price=price,
        )

    def cancel_order(self):
        """
        注文取消関数
        """
        self.api.cancelallchildorders(product_code=self.product_code)
