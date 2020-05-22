from django.utils import timezone
from django.db import models


class Stock(models.Model): 
    code = models.IntegerField(primary_key=True)  #종목코드0
    name= models.IntegerField(null=False)  # 종목명1
    time= models.IntegerField(null=False)  # 시간4
    cprice= models.IntegerField(null=False) # 종가11
    diff= models.IntegerField(null=False)  # 대비12
    open= models.IntegerField(null=False)  # 시가13
    high= models.IntegerField(null=False)  # 고가14
    low= models.IntegerField(null=False)   # 저가15
    offer = models.IntegerField(null=False)  #매도호가16
    bid = models.IntegerField(null=False)   #매수호가17
    vol= models.IntegerField(null=False)   #거래량18
    vol_value= models.IntegerField(null=False)  #거래대금19
