from django.urls import path, include
from rest_framework import routers
from .views import PassportVS, DiplomVS, ContactVS

router_passport = routers.DefaultRouter()
router_passport.register(r'', PassportVS)

router_diplom = routers.DefaultRouter()
router_diplom.register(r'', DiplomVS)

router_contact = routers.DefaultRouter()
router_contact.register(r'', ContactVS)

urlpatterns = [
    path('passport/', include(router_passport.urls)),
    path('diplom/', include(router_diplom.urls)),
    path('contact/', include(router_contact.urls))
]