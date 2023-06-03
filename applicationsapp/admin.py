from django.contrib import admin
from django.db.models import Count
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin

from django.urls import reverse, path
from django.utils.html import format_html

from .models import Application
from infoapp.models import Passport

class ApplicationResource(resources.ModelResource):
    class Meta:
        model = Application
        fields = ('abituriyent__phone_number',
                  'passport__first_name', 'passport__last_name', 'passport__other_name',
                  'passport__birth_day', 'passport__fuqaroligi', 'passport__nation',
                  'passport__gender', 'passport__viloyat', 'passport__tuman',
                  'passport__manzil', 'passport__kim_tomonidan_berilgan',
                  'passport__passport_series', 'passport__passport_jshshir',
                  'diplom__malumot_turi', 'diplom__muassasa_turi', 'diplom__muassasa_nomi',
                  'diplom__tugatgan_yili', 'diplom__diplom_seriya',

                  'talim_turi', 'talim_shakli', 'talim_yonalishi')

@admin.register(Application)
class ApplicationAdmin(ImportExportModelAdmin):

    resource_class = ApplicationResource
    filter_vertical = ()
    list_display = ('abituriyent', 'id', 'passport', 'diplom', 'perevod_diplom', 'is_perevod', 'talim_shakli', 'talim_yonalishi', 'created_at', 'kvitansiya_upload', 'status')
    list_filter = ('talim_turi', 'talim_shakli', 'talim_yonalishi', 'is_perevod', 'status')
    ordering = ('-id',)
