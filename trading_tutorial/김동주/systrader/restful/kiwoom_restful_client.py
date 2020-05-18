"""
Make request to restful API of Xing bridge server
"""
import os
import pandas as pd
import requests


class KiwoomRestAPI:
    def __init__(self, server_url):
        self.server_url = server_url # e.g., http://192.168.0.33:5000
        self.price_url = os.path.join(server_url, "price") # e.g., http://192.168.0.33:5000/price
        self.order_url = os.path.join(server_url, "order")
        self.balance_url = os.path.join(server_url, "balance")

    def get_price(self, code):
        """
        code: symbol, in string. e.g., "233740".
        """
        data = {
            "code": shcode
        }
        resp = requests.post(self.price_url, json=data)
        #print("get_price:", shcode)
        #print(resp.status_code)
        #print(resp.json())
        return resp.json()

    def market_order(self, accno, code, qty, premarket=False):
        """
        accno: string of account number to run transaction on.
        code: (str) Symbol for buying the stock.
        qty: quantity. If below 0, it is a sell order.
        """
        if qty == 0:
            return # Nothing to do.

        ty = "premarket" if premarket else "market"
        data = {
            "qty": qty,
            "price": 0,
            "code": code,
            "type": ty,
            "accno": accno,
        }
        requests.post(self.order_url, json=data)

    def limit_order(self, accno, code, qty, price):
        """
        accno: string of account number to run transaction on.
        code: (str) Symbol for buying the stock.
        qty: quantity. If below 0, it is a sell order.
        price: price of the limit order
        """
        if qty == 0:
            return # Nothing to do.

        data = {
            "qty": qty,
            "price": price,
            "code": code,
            "type": "limit",
            "accno": accno,
        }
        requests.post(self.order_url, json=data)

    def balance(self, accno):
        """
        accno: string of account number to run transaction on.
        Returns: a dict containing item and quantity. For example,

        result = {
            "cash": 1000000,
            "233740": 1
        }
        """
        data = {
            "accno": accno
        }
        resp = requests.post(self.balance_url, json=data)
        result = resp.json()

        # You get '0' as count for things you sold. Remove them.
        to_del = []
        for key, val in result.items():
            if val == 0:
                to_del.append(key)
        for key in to_del:
            del result[key]
        return result


if __name__ == "__main__":
    import json
    with open(os.path.expanduser("~/.kiwoom.json")) as f:
        args = json.load(f)
    server_url = args["server_url"]
    account_num = args["account_num"]

    ex = KiwoomRestAPI(server_url)
    #ex.market_order(account_num, "233740", 10)
    #ex.limit_order(account_num, "233740", -5, 13000)
    balance = ex.balance(account_num)
    print(balance)
