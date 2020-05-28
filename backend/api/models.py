from django.utils import timezone
from django.db import models


class Stock(models.Model): 
    code = models.IntegerField(primary_key=True)  #종목코드
    name= models.IntegerField(null=False)  # 종목명
    market = models.IntegerField(null=False)  # 코스피코스닥구분
    date= models.IntegerField(null=False)  # 날짜
    diff= models.IntegerField(null=False)  # 전일대비 등락
    diffratio = models.FloatField(max_length=20, null=True) #전일대비 등락비율
    diffsign = models.CharField(max_length=10, null=True) #대비부호

    open= models.IntegerField(null=False)  # 시가
    close= models.IntegerField(null=False) # 종가
    high= models.IntegerField(null=False)  # 고가
    low= models.IntegerField(null=False)   # 저가
    average= models.IntegerField(null=False)   # 평군(?)가격 = 거래대금/거래량

