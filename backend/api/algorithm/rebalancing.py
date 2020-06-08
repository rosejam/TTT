from django.db import connection
import datetime
#import pymysql
from dateutil.relativedelta import relativedelta
import math

# 디버깅용 pymysql db
'''
temp_db = pymysql.connect(
        user='ttt', 
        passwd='a105A!)%', 
        host='3.34.96.193', 
        db='TTT',
        port=3306)
'''

# 리턴할때 사용할 date type '%Y-%m-%d' 형식
def getHypenDate(int_date):
    mm=str(int(int_date%10000/100))
    if len(mm)==1:
        mm="0"+mm
    dd=str(int_date%100)
    if len(dd)==1:
        dd="0"+dd
    retDate=str(int(int_date/10000))+"-"+mm+"-"+dd
    return retDate

def rebalance(stock_list, s_date, e_date,assets,freq,buy_fee,sell_fee):
    cursor=connection.cursor()
    
    # 디버깅용 pymysql connection
    #cursor=temp_db.cursor()

    rret=0;
    ret=[]
    print(stock_list)
    for idx, stock in enumerate(stock_list[0].keys()):
        if(idx==0):
            query_string="select code, date, close from api_stock where code='"+stock+"'"
        else:
            query_string=query_string+" or code='"+stock+"'"
    cursor.execute(query_string)
    stock_data=cursor.fetchall()
    
    # 데이터가 tuple 형태로 code, date 순으로 정렬해서 들어오기 때문에 빠르게 실행하기 위해
    # 각 code의 시작 index를 저장해둠
    s_idx={}
    for idx, data in enumerate(stock_data):
        if not data[0] in s_idx:
            s_idx[data[0]]=idx



    if freq==-1:
        # 리밸런싱이 없는 경우
        for i, stocks in enumerate(stock_list):
            rret={}
            # 도중에 상장되는 주식을 위해 시작 날짜에 시작 자산 금액을 저장
            str_s_date=getHypenDate(s_date)
            rret[str_s_date]=assets
            for key, value in stocks.items():
                if(value==0):
                    continue
                stock_asset=assets*value/100
                flag=True
                sub_asset=0
                for item in stock_data[s_idx[key]:]:
                    if item[0]!=key:
                        break
                    if item[1]<s_date:
                        continue
                    if item[1]>e_date:
                        break

                    tempdate=getHypenDate(item[1])
                    rret[tempdate]=assets
                    if flag:
                        stock_amount=int(stock_asset/item[2])
                        sub_asset=math.ceil(stock_amount*item[2]*(1+buy_fee/100))
                        flag=False
                    else:
                        rret[tempdate]=rret[tempdate]-sub_asset+stock_amount*item[2]

            tempdate=getHypenDate(e_date)
            if len(rret)==1:
                rret[tempdate]=assets        
            ret.append(rret)
    else:
        # 월수를 기준으로 리밸런싱을 해주기 때문에 월수 차이를 계산함
        subYear=int(e_date/10000)-int(s_date/10000)
        subMonth=int(e_date%10000/100)-int(s_date%10000/100)
        subDay=e_date%100-s_date%100
        if subDay<0:
            subMonth=subMonth-1
        if subMonth<0:
            subYear=subYear-1
            subMonth=subMonth+12
        subMonth=subMonth+subYear*12

        for i, stocks in enumerate(stock_list):
            rret={}
            stock_amount={}
            str_s_date=getHypenDate(s_date)
            rret[str_s_date]=assets
            drebal_date=datetime.datetime.strptime(str(s_date),"%Y%m%d").date()
            cp_idx=s_idx.copy()
            cp_sdate=s_date
            # 계산한 마지막 날짜의 자산 크기를 ccp_asset에 저장(리밸런스 할때의 자산 크기를 활용하기 위함 rebal_date와 비교하지 않는 이유는 rebal_date가 주식 거래가 없는 날일수도 있기 때문)
            # 리밸런스 할때마다 ccp_asset을 cp_asset에 저장
            # cp_asset을 이용하여 자산 크기 계산
            cp_asset=assets
            ccp_asset=assets
            for j in range(int(subMonth/freq)+1):
                #drebal_date datetime 형식으로 작성한 rebalancing 날짜에 rebalancing 주기만큼 개월수를 더함(개월수 계산을 편하게 하기 위해 datetime을 이용함)
                drebal_date=drebal_date+relativedelta(months=freq)
                rebal_date=min(int(drebal_date.strftime("%Y%m%d")),e_date)
                for key,value in stocks.items():
                    if(value==0):
                        continue
                    stock_asset=assets*value/100
                    # flag 변수를 이용하여 리밸런스 주기중 첫날만 주식을 구매하고 팔게 지정
                    flag=True
                    sub_asset=0
                    for item in stock_data[cp_idx[key]:]:
                        if item[0]!=key:
                            break
                        if item[1]<cp_sdate:
                            #cp_idx를 변경하여 중복된 데이터를 확인하는 것을 방지
                            cp_idx[key]+=1
                            continue
                        if item[1]>rebal_date:
                            break
                        cp_idx[key]+=1
                        tempdate=getHypenDate(item[1])
                        rret[tempdate]=cp_asset
                        if flag:
                            past_amount=0
                            if item[0] in stock_amount:
                                past_amount=stock_amount[item[0]]
                            stock_amount[item[0]]=int(stock_asset/item[2])
                            sub_asset=stock_amount[item[0]]*item[2]
                            # 주식 산거 차이만큼 사고 팔았을때의 수수료 계산
                            if past_amount>stock_amount[item[0]]:
                                sub_asset+=math.ceil(sell_fee*(past_amount-stock_amount[item[0]])*item[2]/100)
                            else:
                                sub_asset+=math.ceil(buy_fee*(stock_amount[item[0]]-past_amount)*item[2]/100)
                            flag=False
                        else:
                            rret[tempdate]=rret[tempdate]-sub_asset+stock_amount[item[0]]*item[2]
                            ccp_asset=rret[tempdate]
                            
                cp_asset=ccp_asset
                cp_sdate=rebal_date

            tempdate=getHypenDate(e_date)
            if len(rret)==1:
                rret[tempdate]=assets
 
            ret.append(rret)
    return ret
        
# query 문 넣고 확인해보기!
    

if __name__=="__main__":
    print(rebalance([{'A000040': 100}],20000101,20201231,10000000,3,0.015,0.015))