from api import models, serializers
from algorithm import kiwoom_login
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination


class SmallPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


class Kiwoomlogin(viewsets.ModelViewSet):
   
    def get_queryset(self):
        return queryset


