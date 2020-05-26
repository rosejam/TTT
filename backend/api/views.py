from api import models, serializers
from rest_framework import viewsets
from rest_framework.response import Response
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

    def list(self, request, *args, **kwargs):
        param_userpk=request.query_params.get('pk')
        if param_userpk:
            queryset = models.User.objects.filter(type_int__gt=1)
            queryset = self.paginate_queryset(queryset)
            serializer = self.get_serializer(queryset, many=True)
            return self.get_paginated_response(serializer.data)
        return super().list(request, *args, **kwargs)