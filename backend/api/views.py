from api import models, serializers
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination


class SmallPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


class StockViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StockSerializer
    pagination_class = SmallPagination

    def get_queryset(self):
        queryset = models.Stock.objects.all()
        
        return queryset

