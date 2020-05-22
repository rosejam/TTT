from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from api import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api import rest_user
from django.urls import path
router = DefaultRouter(trailing_slash=False)(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('user/getallusers',rest_user.all_users,name="getAllUsers"),
    path('user/getuser/<email>',rest_user.specific_user,name="getSpecificUser"),
    path('user/adduser',rest_user.all_users,name="addSpecificUser"),
    path('user/updateuser/<email>',rest_user.specific_user,name="updateSpecificUser"),
    path('user/deleteuser/<email>',rest_user.specific_user,name="deleteSpecificUser"),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ...
]

