# -*- coding: utf-8 -*-

import pandas as pd

from constants import MarketType, OrderType

STOCK_COLS = [
    'code', 'name', 'market', 'chg_price', 'chg_rate',
    'price', 'volume', 'score', 'signal'
]

HOLDING_COLS = [
    'code', 'name', 'market', 'amount', 'eval_price', 'eval_rate'
]

OUTSTANDING_COLS = [
    'code', 'name', 'market', 'mode', 'price', 'amount', 'status'
]

HANDLED_COLS = [
    'code', 'name', 'market', 'amount', 'price'
]

_CHART_COLS = [
    'date', 'time', 'price', 'high', 'low', 'volume', 'sign', 'bbu2', 'bbu1', 'ma20', 'bbl1', 'bbl2', 'vol_ma20'
]

CHART_COLS = [
    'date', 'time', 'open', 'high', 'low', 'close', 'volume', 'sign'
]

OFFER_BID_COLS = [
    'offer', 'offer1', 'offer2', 'offer3', 'offer4', 'offer5', 'offer6', 'offer7', 'offer8', 'offer9', 'offer10',
    'bid', 'bid1', 'bid2', 'bid3', 'bid4', 'bid5', 'bid6', 'bid7', 'bid8', 'bid9', 'bid10'
]

ACCOUNT = [
    'eval_price', 'eval_diff', 'exe_diff'
]

def convert_index(index):
    converted_index = {}
    converted_index['type']

def convert_stocks_t1442(stocks):
    converted_stocks = pd.DataFrame(columns=STOCK_COLS)
    converted_stocks['code'] = stocks['shcode']
    converted_stocks['name'] = stocks['hname']
    converted_stocks['market'] = stocks['market']
    converted_stocks['chg_price'] = stocks['change'].astype(float)
    converted_stocks['chg_rate'] = stocks['diff'].astype(float)
    converted_stocks['price'] = stocks['close'].astype(float)
    converted_stocks['volume'] = stocks['volume'].astype(int)
    converted_stocks['score'] = converted_stocks['chg_rate'] * converted_stocks['volume']
    if 'signal' in stocks:
        converted_stocks['signal'] = stocks['signal']
    return converted_stocks

def convert_stocks_t1101(stocks):
    converted_stocks = pd.DataFrame(columns=STOCK_COLS+OFFER_BID_COLS)
    converted_stocks['code'] = stocks['shcode']
    converted_stocks['name'] = stocks['hname']
    converted_stocks['chg_price'] = stocks['change'].astype(float)
    converted_stocks['chg_rate'] = stocks['diff'].astype(float)
    converted_stocks['price'] = stocks['price'].astype(float)
    converted_stocks['volume'] = stocks['volume'].astype(int)
    converted_stocks['score'] = converted_stocks['chg_rate'] * converted_stocks['volume']
    converted_stocks['offer'] = stocks['offer'].astype(int)
    converted_stocks['offer1'] = stocks['offerrem1'].astype(int)
    converted_stocks['offer2'] = stocks['offerrem2'].astype(int)
    converted_stocks['offer3'] = stocks['offerrem3'].astype(int)
    converted_stocks['offer4'] = stocks['offerrem4'].astype(int)
    converted_stocks['offer5'] = stocks['offerrem5'].astype(int)
    converted_stocks['offer6'] = stocks['offerrem6'].astype(int)
    converted_stocks['offer7'] = stocks['offerrem7'].astype(int)
    converted_stocks['offer8'] = stocks['offerrem8'].astype(int)
    converted_stocks['offer9'] = stocks['offerrem9'].astype(int)
    converted_stocks['offer10'] = stocks['offerrem10'].astype(int)
    converted_stocks['bid'] = stocks['bid'].astype(int)
    converted_stocks['bid1'] = stocks['bidrem1'].astype(int)
    converted_stocks['bid2'] = stocks['bidrem2'].astype(int)
    converted_stocks['bid3'] = stocks['bidrem3'].astype(int)
    converted_stocks['bid4'] = stocks['bidrem4'].astype(int)
    converted_stocks['bid5'] = stocks['bidrem5'].astype(int)
    converted_stocks['bid6'] = stocks['bidrem6'].astype(int)
    converted_stocks['bid7'] = stocks['bidrem7'].astype(int)
    converted_stocks['bid8'] = stocks['bidrem8'].astype(int)
    converted_stocks['bid9'] = stocks['bidrem9'].astype(int)
    converted_stocks['bid10'] = stocks['bidrem10'].astype(int)
    if 'signal' in stocks:
        converted_stocks['signal'] = stocks['signal']
    return converted_stocks

def convert_stocks_t1102(stocks):
    converted_stocks = pd.DataFrame(columns=STOCK_COLS)
    converted_stocks['code'] = stocks['shcode']
    converted_stocks['name'] = stocks['hname']
    converted_stocks['chg_price'] = stocks['change'].astype(float)
    converted_stocks['chg_rate'] = stocks['diff'].astype(float)
    converted_stocks['price'] = stocks['price'].astype(float)
    converted_stocks['volume'] = stocks['volume'].astype(int)
    converted_stocks['score'] = converted_stocks['chg_rate'] * converted_stocks['volume']
    if 'signal' in stocks:
        converted_stocks['signal'] = stocks['signal']
    return converted_stocks

def convert_outstanding_t0425(outstandings):
    converted_outstandings = pd.DataFrame(columns=OUTSTANDING_COLS)
    converted_outstandings['code'] = outstandings['expcode']
    converted_outstandings['mode'] = OrderType.SELL if outstandings['medosu'].str == '매도' else OrderType.BUY
    converted_outstandings['price'] = outstandings['price'].astype(float)
    converted_outstandings['amount'] = outstandings['qty'].astype(int)
    converted_outstandings['status'] = outstandings['status']
    return converted_outstandings

def convert_holdings_CSPAQ12300(holdings):
    converted_holdings = pd.DataFrame(columns=HOLDING_COLS)
    converted_holdings['code'] = holdings['IsuNo'].str[1:]
    converted_holdings['name'] = holdings['IsuNm']
    converted_holdings['market'] = holdings['RegMktCode']
    converted_holdings['amount'] = holdings['SellAbleQty'].astype(int)
    converted_holdings['eval_price'] = holdings['EvalPnl'].astype(float)
    converted_holdings['eval_rate'] = holdings['PnlRat'].astype(float)*100
    converted_holdings.loc[converted_holdings['market']=='10', 'market'] = MarketType.KOSPI
    converted_holdings.loc[converted_holdings['market']=='20', 'market'] = MarketType.KOSDAQ
    return converted_holdings

def convert_holdings_t0424(holdings):
    converted_holdings = pd.DataFrame(columns=HOLDING_COLS)
    converted_holdings['code'] = holdings['expcode']
    converted_holdings['name'] = holdings['hname']
    converted_holdings['market'] = holdings['marketgb']
    converted_holdings['amount'] = holdings['mdposqt'].astype(int)
    converted_holdings['eval_price'] = holdings['appamt'].astype(float)
    converted_holdings['eval_rate'] = holdings['dtsunik'].astype(float)*100
    converted_holdings.loc[converted_holdings['market']=='2', 'market'] = MarketType.KOSDAQ
    converted_holdings.loc[converted_holdings['market']=='3', 'market'] = MarketType.KOSPI
    return converted_holdings

def convert_handled_stocks_CSPAQ13700(stocks):
    converted_handled_stocks = pd.DataFrame(columns=HANDLED_COLS)
    converted_handled_stocks['code'] = stocks['IsuNo'].str[1:]
    converted_handled_stocks['name'] = stocks['IsuNm']
    converted_handled_stocks['market'] = stocks['OrdMktCode']
    converted_handled_stocks['amount'] = stocks['ExecQty'].astype(int)
    converted_handled_stocks['price'] = stocks['ExecPrc'].astype(float)
    converted_handled_stocks.loc[converted_handled_stocks['market']=='10', 'market'] = MarketType.KOSPI
    converted_handled_stocks.loc[converted_handled_stocks['market']=='20', 'market'] = MarketType.KOSDAQ
    return converted_handled_stocks

def convert_chart(chart):
    converted_handled_stocks = pd.DataFrame(columns=CHART_COLS)
    converted_handled_stocks['date'] = chart['date']
    if 'time' in chart:
        converted_handled_stocks['time'] = chart['time']
    converted_handled_stocks['open'] = chart['open'].astype(float)
    converted_handled_stocks['close'] = chart['close'].astype(float)
    converted_handled_stocks['high'] = chart['high'].astype(float)
    converted_handled_stocks['low'] = chart['low'].astype(float)
    converted_handled_stocks['volume'] = chart['jdiff_vol'].astype(int)
    if 'sign' in chart:
        converted_handled_stocks['sign'] = chart['sign']
    return converted_handled_stocks

def _convert_chart(chart):
    converted_handled_stocks = pd.DataFrame(columns=CHART_COLS)
    converted_handled_stocks['date'] = chart['date']
    if 'time' in chart:
        converted_handled_stocks['time'] = chart['time']
    converted_handled_stocks['open'] = chart['open'].astype(float)
    converted_handled_stocks['price'] = chart['close'].astype(float)
    converted_handled_stocks['high'] = chart['high'].astype(float)
    converted_handled_stocks['low'] = chart['low'].astype(float)
    converted_handled_stocks['volume'] = chart['jdiff_vol'].astype(int)
    if 'sign' in chart:
        converted_handled_stocks['sign'] = chart['sign']
    converted_handled_stocks['bbu2'] = chart['bbu2']
    converted_handled_stocks['bbu1'] = chart['bbu1']
    converted_handled_stocks['ma20'] = chart['ma20']
    converted_handled_stocks['bbl1'] = chart['bbl1']
    converted_handled_stocks['bbl2'] = chart['bbl2']
    converted_handled_stocks['vol_ma20'] = chart['vol_ma20']
    return converted_handled_stocks

