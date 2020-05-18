#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The server program that provides RESTful API
"""

import tornado
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop

import json
import pandas as pd
import sys
import time

from kiwoom import Kiwoom, logger
from PyQt5.QtWidgets import QApplication

SLEEP_TIME = 0.1


class PriceHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.event = None

    def wait_response(self, price):
        self.event.set()

    def post(self):
        """
        request data must contain
        "code": symbol (aka code) of the stock
        """
        data = tornado.escape.json_decode(self.request.body)

        code = data["code"]
        hts.dict_stock[code] = {}

        # Make request
        hts.kiwoom_TR_OPT10001_주식기본정보요청(code)

        # Wait for response
        while not hts.dict_stock[code]:
            time.sleep(SLEEP_TIME)

        result = hts.dict_stock[code]

        odata = {
            "name": result["종목명"],
            "price": int(result["현재가"]),
            "volume": int(result["거래량"])
        }
        logger.debug("Response to client:")
        logger.debug(str(odata))
        self.write(odata)


class OrderHandler(RequestHandler):
    request_no = 0

    def post(self):
        """
        request data must hold the following:
        qty : pos number for buy, neg number for sell
        price : limit order price. Don't care if pre/market order.
        code : code of the stock
        type : {limit, market, premarket}
        accno : account number of this transaction
        """
        data = tornado.escape.json_decode(self.request.body)
        logger.debug("OrderHandler: incoming")
        logger.debug(data)

        # data must hold
        qty = data['qty']
        assert qty != 0
        nOrderType = 1 if qty > 0 else 2 # 1=buy, 2=sell
        qty = abs(qty)

        code = data['code']

        sHogaGb = "00"
        if data['type'] == "limit":
            sHogaGb = "00"
        elif data['type'] == "market":
            sHogaGb = "03"
        elif data['type'] == "premarket":
            sHogaGb = "61"
        else:
            assert 0, "Wrong type of order from client"

        price = 0
        if data['type'] == "limit":
            price = data['price']

        rq_name = "RQ_" + str(OrderHandler.request_no)
        OrderHandler.request_no += 1

        hts.kiwoom_SendOrder(
            rq_name,
            "8949", # dummy
            data['accno'],
            nOrderType,
            code,
            qty,
            price,
            sHogaGb,
            "" # original order number to cancel or correct.
        )
        logger.debug("Order sent.")


class BalanceHandler(RequestHandler):
    def post(self):
        """
        Request data must contain
        accno : account number the transaction will happen
        """
        data = tornado.escape.json_decode(self.request.body)
        logger.debug("BalanceHandler: incoming")
        logger.debug(data)

        hts.int_주문가능금액 = None
        result = hts.kiwoom_TR_OPW00001_예수금상세현황요청(data["accno"])
        while not hts.int_주문가능금액:
            time.sleep(SLEEP_TIME)
        cash = hts.int_주문가능금액

        hts.dict_holding = None
        hts.kiwoom_TR_OPT10085_계좌수익률요청(data["accno"])
        while hts.dict_holding is None:
            time.sleep(SLEEP_TIME)

        result = {}
        for code, info in hts.dict_holding.items():
            result[code] = int(info["보유수량"])
        result["cash"] = cash

        logger.debug("Response to client:")
        logger.debug(str(result))
        self.write(json.dumps(result))


def make_app():
    urls = [
        ("/price", PriceHandler),
        ("/order", OrderHandler),
        ("/balance", BalanceHandler),
    ]
    # Autoreload seems troublesome.
    return Application(urls, debug=True, autoreload=False)


def shutdown():
    # It seems there's no logout so... nothing here.
    pass


#
# Shared variables
#
app = QApplication(sys.argv)
hts = Kiwoom()

if __name__ == "__main__":
    # login
    if hts.kiwoom_GetConnectState() != 0:
        logger.debug('Connection failed')
        sys.exit()

    logger.debug('로그인 시도')
    res = hts.kiwoom_CommConnect()
    if res.get('result') != 0:
        logger.debug('Login failed')
        sys.exit()

    # To see list of your accounts...
    if True:
        accounts = hts.kiwoom_GetAccList()
        logger.debug("Your accounts:")
        for acc in accounts:
            logger.debug(acc)

    port = 5000
    tornado_app = make_app()
    tornado_app.listen(port)
    #tornado.autoreload.add_reload_hook(shutdown)
    logger.debug('RESTful api server started at port {}'.format(port))

    #try:
    #    IOLoop.instance().start()
    #except KeyboardInterrupt:
    #    shutdown()
    # Nothing to do for shutdown so... commenting out.

    IOLoop.instance().start()
