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


class User(models.Model):
    user_code = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100,null=False)
    account_no=models.IntegerField(null=False)
    account_bank=models.CharField(max_length=45,null=False)
    wallet = models.BigIntegerField(null=False,default=0)
    class Meta:
        db_table='user'

class Stock_Market(models.Model):
    market_code= models.AutoField(primary_key=True)
    stock_name=models.CharField(max_length=45,null=False)
    stock_code=models.CharField(max_length=45,null=False)
    status=models.IntegerField(null=False)
    market=models.IntegerField(null=False)

    class Meta:
        db_table="stock_market"

class Algorithm(models.Model):
    algo_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        db_table="Algorithm"

class log(models.Model):
    log_code=models.AutoField(primary_key=True)
    user_pk=models.ForeignKey('User',on_delete=models.CASCADE,related_name='log_fk1')
    timestamp=models.DateTimeField()
    buysell=models.IntegerField(null=False)
    stock_pk=models.ForeignKey('Stock',on_delete=models.CASCADE,related_name="log_fk2")
    assets=models.BigIntegerField()
    balance=models.BigIntegerField()
    
    class Meta:
        db_table="log"


class user_algo(models.Model):
    useralgo_code = models.AutoField(primary_key=True)
    user_pk=models.ForeignKey('User',on_delete=models.CASCADE,related_name='useralgo_fk1')
    algo_pk=models.ForeignKey('Algorithm',on_delete=models.CASCADE,related_name='useralgo_fk2')
    var1=models.FloatField()
    var2=models.FloatField()
    var3=models.FloatField()
    var4=models.IntegerField()
    var5=models.IntegerField()

