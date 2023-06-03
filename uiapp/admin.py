from django.contrib import admin
from .models import HomeSection, AboutSection, TalimYonalishlariSection, Litsenziya, \
    Video, Faq, Facultet, SiteSettings, SocialNetworks

# Register your models here.
admin.site.register(HomeSection)
admin.site.register(AboutSection)
admin.site.register(TalimYonalishlariSection)
admin.site.register(Litsenziya)
admin.site.register(Video)
admin.site.register(Faq)
admin.site.register(Facultet)
admin.site.register(SiteSettings)
admin.site.register(SocialNetworks)