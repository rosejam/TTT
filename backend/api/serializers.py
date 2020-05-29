from api.models import Stock
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
            "diffration",
            "open", 
            "close",
            "high",
            "low",
            "average"

        ]