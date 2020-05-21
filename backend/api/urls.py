from django.conf.urls import url
from rest_framework.routers import DefaultRouter
# from api import views
from api import resttest
from django.urls import path
# router = DefaultRouter(trailing_slash=False)
# router.register(r"users", views.StoreViewSet, basename="stores")

# urlpatterns = router.urls
urlpatterns=[
    path('resttest/',resttest.all_users,name="restAllUsers")
]
