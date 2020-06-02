import os
import pandas as pd
import requests
import pymysql
import json
import time
from datetime import datetime
import threading
import time

list_url= "http://15.165.21.105:5000/stockcodes?market=kospi"

base_url= "http://15.165.21.105:5000/stockcandles?code="
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
    market='1' #코스피는 1
    print('current   ',code)
    print('name   ',name)
    stock_url = base_url+code+"&date_from=20000101"
    
    stock_result = requests.get(stock_url).json()
    current = stock_result[0]
    print(current)
    startdate=str(current['date'])
    sql = "insert into api_stockinfo(code, name, market, startdate) values('"+code+"','"+name+"',"+market+","+startdate+")"
    print(sql)
    cur.execute(sql) 
    conn.commit() 

list_url= "http://15.165.21.105:5000/stockcodes?market=kosdaq"

list_result = requests.get(list_url).json()
# print(list_result.keys())
list_key = list_result.keys()
print(list_key)
for i in  enumerate(list_key):

    code = i[1] # 현재 종목 코드
    name  = str(list_result[code]['종목명'])
    market='2' #코스닥 2
    print('current   ',code)
    print('name   ',name)
    print('i    ',i)
    stock_url = base_url+code+"&date_from=20000101"
    print(stock_url)
    
    stock_result = requests.get(stock_url).json()
    current = stock_result[0]
    # print(current)
    startdate=str(current['date'])
    sql = "insert into api_stockinfo(code, name, market, startdate) values('"+code+"','"+name+"',"+market+","+startdate+")"
    print(sql)
    cur.execute(sql) 
    conn.commit() 