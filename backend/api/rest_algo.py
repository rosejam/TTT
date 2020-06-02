from django.http import HttpResponse
import json
from api.algorithm.rebalancing import rebalance
import datetime

def rebalancing(request):
    def post():
        received_json_data=json.loads(request.body)
        period=received_json_data['period']
        endMonth=received_json_data['endMonth']
        endYear=received_json_data['endYear']
        assets=received_json_data['initAmount']
        rebalancefreq=received_json_data['rebalancing']
        startMonth=received_json_data['startMonth']
        startYear=received_json_data['startYear']
        stocks=received_json_data['stocks']
        stock_list=[{},{},{}]
        for i in range(0,len(stocks)):
            stockname=stocks[i]['stock'].split('[')[0]
            stock_list[0][stockname]=stocks[i]['portfolio1']
            stock_list[1][stockname]=stocks[i]['portfolio2']
            stock_list[2][stockname]=stocks[i]['portfolio3']
        ret = []
        if(period=='M'):
            if(rebalancefreq==-1):
                ret.append(rebalance(stock_list[0], datetime.datetime(startYear,startMonth,1),datetime.datetime(endYear,endMonth,1),assets))
                ret.append(rebalance(stock_list[1], datetime.datetime(startYear,startMonth,1),datetime.datetime(endYear,endMonth,1),assets))
                ret.append(rebalance(stock_list[2], datetime.datetime(startYear,startMonth,1),datetime.datetime(endYear,endMonth,1),assets))
                print(ret)
                return HttpResponse(ret);

        else:
            pass

    if request.method=="POST":
        return post()
    else:
        return HttpResponse(status=405)

# def rebalance(stock_list, s_date, e_date,assets):
        

