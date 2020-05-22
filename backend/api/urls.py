from django.conf.urls import url
from rest_framework.routers import DefaultRouter
# from api import views
from api import rest_user
from django.urls import path
# router = DefaultRouter(trailing_slash=False)
# router.register(r"users", views.StoreViewSet, basename="stores")

# urlpatterns = router.urls
urlpatterns=[
    path('user/getallusers',rest_user.all_users,name="getAllUsers"),
    path('user/getuser/<email>',rest_user.specific_user,name="getSpecificUser"),
    path('user/adduser',rest_user.all_users,name="addSpecificUser"),
    path('user/updateuser/<email>',rest_user.specific_user,name="updateSpecificUser"),
    path('user/deleteuser/<email>',rest_user.specific_user,name="deleteSpecificUser"),
]
