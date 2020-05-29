from django.http import HttpResponse
import json
from api.algorithm.rebalancing import rebalance

def rebalancing(request):
    def post():
        dump_json_data=json.dumps(request.POST)
        received_json_data=json.loads(dump_json_data)
        #for key, value in received_json_data:
        s_date=received_json_data['s_date']
        del received_json_data['s_date']
        e_date=received_json_data['e_date']
        del received_json_data['e_date']
        rebal_freq = received_json_data['rebal_freq']
        del received_json_data['rebal_freq']

        

