from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter(trailing_slash=False)
router.register(r"stores", views.StoreViewSet, basename="stores")

urlpatterns = router.urls
