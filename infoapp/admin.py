from django.contrib import admin

from .models import Passport, Diplom, PerevodDiplom

# Register your models here.
admin.site.register(Passport)
admin.site.register(Diplom)
admin.site.register(PerevodDiplom)
# admin.site.register(Contact)