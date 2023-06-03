from django.contrib import admin
from django.urls import path, include
from .views import *

# Static settings
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import REGISTER, PHONE_VERIFY, LOGIN, CABINET, \
    RESEND_CODE, RESET_PASSWORD_1, LOGOUT, RESET_PASSWORD_2, LOGOUT_REGISTER
from infoapp.views import CABINET_PASSPORT, CABINET_DIPLOM, CABINET_PEREVOD_DIPLOM, \
    CABINET_ARIZA, viloyatlar_api, tumanlar_api, CABINET_UPLOAD_IMAGE, \
    talim_shakli_api, yonalishlar_api

from applicationsapp.views import CABINET_UPLOAD_KVITANSIYA

admin.site.site_header = 'Qabul.XiuEdu.UZ'
admin.site.site_title = 'Qabul.XiuEdu.UZ'
admin.site.index_title = 'Dashboard'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HOME_PAGE, name='home_page'),
    path('auth/register/', REGISTER, name='register'),
    path('auth/login/', LOGIN, name='login'),
    path('auth/phone-verify/', PHONE_VERIFY, name='phone_verify'),
    path('auth/resend-code/', RESEND_CODE, name='resend_code'),
    path('auth/reset/', RESET_PASSWORD_1, name='reset_password_1'),
    path('auth/reset-password/', RESET_PASSWORD_2, name='reset_password_2'),
    path('auth/logout/', LOGOUT, name='logout'),
    path('auth/logout-register/', LOGOUT_REGISTER, name='logout_register'),

    path('cabinet/', CABINET, name='cabinet'),
    path('cabinet/passport/', CABINET_PASSPORT, name='cabinet_passport'),
    path('cabinet/diplom/', CABINET_DIPLOM, name='cabinet_diplom'),
    path('cabinet/diplom-perevod/', CABINET_PEREVOD_DIPLOM, name='cabinet_perevod_diplom'),
    path('cabinet/ariza/', CABINET_ARIZA, name='cabinet_ariza'),
    path('cabinet/upload-image/', CABINET_UPLOAD_IMAGE, name='cabinet_upload_image'),
    path('cabinet/upload-pay/', CABINET_UPLOAD_KVITANSIYA, name='cabinet_upload_pay'),

    # API
    path('api/viloyatlar/', viloyatlar_api, name='viloyatlar_api'),
    path('api/tumanlar/<int:viloyat_id>/', tumanlar_api, name='tumanlar_api'),

    path('api/talim-shakllari/', talim_shakli_api, name='talim_shakli_api'),
    path('api/yonalishlar/<int:talim_shakli_id>/', yonalishlar_api, name='yonalishlar_api'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Media fayllarni serv qilish uchun
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)