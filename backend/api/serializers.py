from api.models import Stock, User, Stock_Market, log, Algorithm, user_algo
from rest_framework import serializers


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # fields=('user_code','email','account_no','account_bank')


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock_Market
        fields = "__all__"


class logSerializer(serializers.ModelSerializer):
    class Meta:
        model = log
        fields = "__all__"


class AlgorithmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Algorithm
        fields = "__all__"

class userAlgoSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_algo
        fields = "__all__"