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
            if(stocks[i]['stock'] is None):
                continue
            stockcode=stocks[i]['stock']
            stock_list[0][stockcode]=int(stocks[i]['portfolio1'])
            stock_list[1][stockcode]=int(stocks[i]['portfolio2'])
            stock_list[2][stockcode]=int(stocks[i]['portfolio3'])
        ret = []
        if(period=='M'):
            ret=rebalance(stock_list, startYear*10000+startMonth*100+1,endYear*10000+endMonth*100+31,assets,rebalancefreq)
            return HttpResponse(ret);
        else:
            ret=rebalance(stock_list, startYear*10000+101,endYear*10000+1231,assets,rebalancefreq)
            return HttpResponse(ret);

    if request.method=="POST":
        return post()
    else:
        return HttpResponse(status=405)

# def rebalance(stock_list, s_date, e_date,assets):
        

