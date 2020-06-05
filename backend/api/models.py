from django.utils import timezone
from django.db import models


class Stock(models.Model): 
    code = models.CharField(max_length=30, null=False)  #종목코드
    name= models.CharField(max_length=100, null=False, default="")   # 종목명
    market = models.IntegerField(null=False, default=0)  # 코스피코스닥구분 1:코스피 , 2:코스닥
    date= models.IntegerField(null=False, default=0)  # 날짜
    diff= models.IntegerField(null=False, default=0)  # 전일대비 등락
    diffratio = models.FloatField(max_length=20, default=0) #전일대비 등락비율

    open= models.IntegerField(null=False, default=0)  # 시가
    close= models.IntegerField(null=False, default=0) # 종가
    high= models.IntegerField(null=False, default=0)  # 고가
    low= models.IntegerField(null=False, default=0)   # 저가
    average= models.IntegerField(null=False, default=0)   # 평균(?)가격 = 거래대금/거래량


class StockInfo(models.Model): 
    code = models.CharField(max_length=30, null=False)  #종목코드
    name= models.CharField(max_length=100, null=False, default="")   # 종목명
    market = models.IntegerField(null=False, default=0)  # 코스피코스닥구분 1:코스피 , 2:코스닥
    startdate= models.IntegerField(null=False, default=0)  # 날짜

class Portfolio(models.Model):
    uid = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)
    startMonth= models.IntegerField(null=True, default=0) 
    startYear= models.IntegerField(null=False, default=0) 
    endMonth= models.IntegerField(null=False, default=0) 
    endYear= models.IntegerField(null=False, default=0) 
    initAmount = models.CharField(max_length=30, null=False) 
    period = models.CharField(max_length=30, null=False)
    rebalancing= models.IntegerField(null=False, default=0) 
    stock = models.CharField(max_length=300, null=False) 
    portfolio1 = models.CharField(max_length=300, null=False)
    portfolio2 = models.CharField(max_length=300, null=False)
    portfolio3 = models.CharField(max_length=300, null=False)