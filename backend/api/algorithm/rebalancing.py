from django.db import connection
import datetime
import pymysql


temp_db = pymysql.connect(
        user='ttt', 
        passwd='a105A!)%', 
        host='3.34.96.193', 
        db='TTT',
        port=3306)




def rebalance(stock_list, s_date, e_date,assets,freq):
    # cursor=connection.cursor()
    cursor=temp_db.cursor()
    rret=0;
    for key,values in stock_list[0].items():
        query_string="select code,startdate from api_stockinfo;"
        print(query_string)
    
    cursor.execute(query_string)
    ss_date=cursor.fetchall()
    print(ss_date)
    if ss_date>s_date:
        s_date=ss_date
    s_year=s_date.year
    s_month=s_date.month
    s_day=s_date.day
    e_year=e_date.year
    e_month=e_date.month
    e_day=e_date.day
    '''
    cnt=0
    for i in range(s_year,e_year+1):
        for j in range(1,13):
            if(i==s_year and j<s_month):
                continue
            if(i==e_year and j>e_month):
                continue
            cnt+=1
    ret=[0]*cnt
    '''
    ret={}
    for key, value in stock_list.items():
        stock_asset=(assets*value/100)
        query_string="select close from api_stock where name='"+key+"' and date like '"+s_date.strftime('%Y%m')+"%' order by date desc limit 1;"
        cursor.execute(query_string)
        rows=cursor.fetchall()

        stock=int(stock_asset/rows[0][0])
        rret=stock_asset-stock*rows[0][0]
        idx=0;
        for i in range(s_year,e_year+1):
            for j in range(1,13):
                if(i==s_year and j<s_month):
                    continue
                if(i==e_year and j>e_month):
                    continue
                yy=str(i)
                mm=str(j)
                if(len(mm)==1):
                    mm='0'+mm
                dd=yy+"-"+mm+"-"+"01"
                query_string2="select close from api_stock where name='"+key+"' and date like '"+yy+mm+"%' order by date desc limit 1;"
                print(query_string2)
                cursor.execute(query_string2)
                rows=cursor.fetchall()
                if(dd in ret):
                    ret[dd]+=rret+rows[0][0]*stock
                else:
                    ret[dd]=rret+rows[0][0]*stock

        

    return ret
        
# query 문 넣고 확인해보기!
    

if __name__=="__main__":
    print(rebalance([{"A000020":50, "A000040":50}],datetime.date(2015,1,7),datetime.date(2015,10,7),100000,6))