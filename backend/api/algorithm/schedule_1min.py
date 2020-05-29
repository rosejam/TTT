import os
import pandas as pd
import requests
import pymysql
import json
import time
from datetime import datetime
import threading

server_url= "http://15.165.21.105:5000/stockcodes?market=kospi"
conn = pymysql.connect(host="3.34.96.193", user="ttt", password="a105A!)%",
                       db="TTT", charset="utf8")  # 1. DB 연결
cur = conn.cursor() # 2. 커서 생성 (트럭, 연결로프)
end = False
today = datetime.today().strftime("%Y-%m-%d ")
def execute_func(second=10.0):
    now = datetime.today().strftime("%H%M")
    if int(now)>1532:
        print("끝!")
        return   
    threading.Timer(second, execute_func,[second]).start()
    print(datetime.today())
    global end
    result = requests.get(server_url).json()
    tablename = 'A005930'
    closeprice=result['A005930']['현재가']
    date=today+now[0:2]+":"+now[2:4]+":00" 
    # for tablename in result_key:
    sql = "insert into "+tablename+"(date,close) values('"+date+"',"+str(closeprice)+") "
    cur.execute(sql)
    conn.commit()

execute_func(60.0)

# today = datetime.today().strftime("%Y-%m-%d")


