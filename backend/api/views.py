from api import models, serializers
from rest_framework import viewsets
from rest_framework.response import Response
from drf_yasg import openapi
from rest_framework.pagination import PageNumberPagination

'''
class SmallPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50
'''

class UserViewSet(viewsets.ModelViewSet):
    queryset=models.User.objects.all()
    serializer_class = serializers.UserSerializer

    '''
    def list(self, request, *args, **kwargs):
        queryset = models.User.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        # print(serializer)
        return super().list(request, *args, **kwargs)
    '''


class MarketViewSet(viewsets.ModelViewSet):
    queryset=models.Stock_Market.objects.all()
    serializer_class = serializers.MarketSerializer

    '''
    param_Market_hint=openapi.Parameter(
        'Market',
        openapi.IN_QUERY,
        description="this is a description of Market",
        type=openapi.TYPE_STRING
    )
    '''


class logViewSet(viewsets.ModelViewSet):
    queryset=models.log.objects.all()
    serializer_class = serializers.logSerializer
