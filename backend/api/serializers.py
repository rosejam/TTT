from api.models import Stock, User, Stock_Market, log
from rest_framework import serializers


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class StockMarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock_Market
        fields = "__all__"


class logSerializer(serializers.ModelSerializer):
    class Meta:
        model = log
        fields = "__all__"
