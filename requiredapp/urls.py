from django.urls import path
from .views import TalimShakliAW, NationAW, SexAW, DistrictAW, RegionAW, \
    PassportFuqaroligiAW

urlpatterns = [
    # 1- tanlanadigan
    path('talim-shakli/', TalimShakliAW.as_view(), name='talim-shakli'),

    # Passport uchun
    path('millatlar/', NationAW.as_view(), name='millatlar'),
    path('jinslar/', SexAW.as_view(), name='jinslar'),
    path('viloyatlar/', DistrictAW.as_view(), name='viloyatlar'),
    path('tumanlar/', RegionAW.as_view(), name='tumanlar'),
    path('fuqaroliklar/', PassportFuqaroligiAW.as_view(), name='fuqaroliklar'),
]