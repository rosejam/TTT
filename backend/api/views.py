from api import models, serializers
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination


class SmallPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StoreSerializer
    pagination_class = SmallPagination

    def get_queryset(self):
        email = self.request.query_params.get("email", "")
        queryset = (
            models.Store.objects.all().filter(store_email__contains=email).order_by("id")
        )
        return queryset

