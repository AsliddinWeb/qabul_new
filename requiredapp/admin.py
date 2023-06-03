from django.contrib import admin

from .models import Nation, Sex, Region, District, TalimTuri, TalimShakli, \
    TalimYonalishi, DiplomMalumotTuri, DiplomMuassasaTuri, PassportFuqaroligi

# Register your models here.
admin.site.register(Nation)
admin.site.register(Sex)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(TalimTuri)
admin.site.register(TalimShakli)

admin.site.register(DiplomMalumotTuri)
admin.site.register(DiplomMuassasaTuri)
admin.site.register(PassportFuqaroligi)

class TalimYonalishiAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'talim_shakli')

admin.site.register(TalimYonalishi, TalimYonalishiAdmin)