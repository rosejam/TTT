from api.models import Stock,StockInfo
from rest_framework import serializers


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = [
            "code",
            "name",
            "market",
            "date",
            "diff",
            "diffratio",
            "open", 
            "close",
            "high",
            "low",
            "average"

        ]

class StockInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockInfo
        fields = [
            "code",
            "name",
            "market",
            "startdate",
        ]
