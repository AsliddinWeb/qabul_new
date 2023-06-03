from django.urls import path
from .views import ApplicationVS
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', ApplicationVS)

urlpatterns = router.urls