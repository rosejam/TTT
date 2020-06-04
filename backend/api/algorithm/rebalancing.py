from django.db import connection
import datetime
import pymysql
from dateutil.relativedelta import relativedelta


temp_db = pymysql.connect(
        user='ttt', 
        passwd='a105A!)%', 
        host='3.34.96.193', 
        db='TTT',
        port=3306)


def getHypenDate(int_date):
    mm=str(int(int_date%10000/100))
    if len(mm)==1:
        mm="0"+mm
    dd=str(int_date%100)
    if len(dd)==1:
        dd="0"+dd
    tempdate=str(int(int_date/10000))+"-"+mm+"-"+dd
    return tempdate

def rebalance(stock_list, s_date, e_date,assets,freq):
    #cursor=connection.cursor()
    cursor=temp_db.cursor()
    rret=0;
    ret=[]
    '''
    for idx, key in enumerate(stock_list[0].keys()):
        if(idx==0):
            query_string="select code,startdate from api_stockinfo where code='"+key+"'"
        else:
            query_string=query_string+" or code='"+key+"'"
    
    s_dict={}
    cursor.execute(query_string)
    ss_date=cursor.fetchall()
    for tdate in ss_date:
        if(tdate[1]>s_date):
            s_dict[tdate[0]]=tdate[1]
        else:
            s_dict[tdate[0]]=s_date
    '''
    print(stock_list)
    for idx, stock in enumerate(stock_list[0].keys()):
        if(idx==0):
            query_string="select code, date, close from api_stock where code='"+stock+"'"
        else:
            query_string=query_string+" or code='"+stock+"'"
    cursor.execute(query_string)
    stock_data=cursor.fetchall()
    
    s_idx={}
    for idx, data in enumerate(stock_data):
        if not data[0] in s_idx:
            s_idx[data[0]]=idx
    
    subYear=int(e_date/10000)-int(s_date/10000)
    subMonth=int(e_date%10000/100)-int(s_date%10000/100)
    subDay=e_date%100-s_date%100
    if subDay<0:
        subMonth=subMonth-1
    if subMonth<0:
        subYear=subYear-1
        subMonth=subMonth+12
    subMonth=subMonth+subYear*12
    
    if freq==-1:
        for i, stocks in enumerate(stock_list):
            rret={}
            tempdate=getHypenDate(s_date)
            rret[tempdate]=assets
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
                        sub_asset=stock_amount*item[2]
                        flag=False
                    else:
                        rret[tempdate]=rret[tempdate]-sub_asset+stock_amount*item[2]

            tempdate=getHypenDate(e_date)
            if len(rret)==1:
                rret[tempdate]=assets        
            ret.append(rret)
    else:
        for i, stocks in enumerate(stock_list):
            rret={}
            tempdate=getHypenDate(s_date)
            rret[tempdate]=assets
            drebal_date=datetime.datetime.strptime(str(s_date),"%Y%m%d").date()
            cp_idx=s_idx.copy()
            cp_sdate=s_date
            cp_asset=assets
            ccp_asset=assets
            for j in range(int(subMonth/freq)+1):
                drebal_date=drebal_date+relativedelta(months=freq)
                rebal_date=min(int(drebal_date.strftime("%Y%m%d")),e_date)
                for key,value in stocks.items():
                    if(value==0):
                        continue
                    stock_asset=assets*value/100
                    flag=True
                    sub_asset=0
                    for item in stock_data[cp_idx[key]:]:
                        if item[0]!=key:
                            break
                        if item[1]<cp_sdate:
                            cp_idx[key]+=1
                            continue
                        if item[1]>rebal_date:
                            break
                        cp_idx[key]+=1
                        tempdate=getHypenDate(item[1])
                        rret[tempdate]=cp_asset
                        if flag:
                            stock_amount=int(stock_asset/item[2])
                            sub_asset=stock_amount*item[2]
                            flag=False
                        else:
                            rret[tempdate]=rret[tempdate]-sub_asset+stock_amount*item[2]
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
    print(rebalance([{'A000080': 100}],20081201,20100307,100000,3))