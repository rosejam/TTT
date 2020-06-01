import os
import pandas as pd
import requests
import pymysql
import json
import time
from datetime import datetime
import threading

list_url= "http://15.165.21.105:5000/stockcodes?market=kospi"

base_url= "http://15.165.21.105:5000/stockcandles?code=" # 035420&date_from=20000101 "
conn = pymysql.connect(host="3.34.96.193", user="ttt", password="a105A!)%",
                       db="TTT", charset="utf8")  # 1. DB 연결
cur = conn.cursor() # 2. 커서 생성 (트럭, 연결로프)


list_result = requests.get(list_url).json()
# print(list_result.keys())
list_key = list_result.keys()
print(list_key)
for i in  enumerate(list_key):

    code = i[1] # 현재 종목 코드
    name  = str(list_result[code]['종목명'])
    market='1'
    print('i[0]   ',i[0])
    print('current   ',code)
    print('name   ',name)
    
    stock_url = base_url+code+"&date_from=20000101"
    print(stock_url)
    
    # stock_result = requests.get(stock_url).json()
    # for j in  enumerate(stock_result):
    #     current = j[1]
    #     date=str(current['date'])
    #     diff=str(current['diff'])
    #     diffratio=str(current['diffratio'])
    #     open=str(current['open'])
    #     close=str(current['close'])
    #     high=str(current['high'])
    #     low=str(current['low'])
    #     average=str(current['average'])
    #     sql = "insert into api_stock(code, name, market, date, diff, diffratio, open, close, high, low, average) values('"+code+"','"+name+"',"+market+","+date+","+diff+","+diffratio+","+open+","+close+","+high+","+low+","+average+")"
    #     # print(sql)
    #     cur.execute(sql) 
    # conn.commit() 
