from django.shortcuts import render
from uiapp.models import SiteSettings, SocialNetworks, HomeSection, \
    Facultet, AboutSection, TalimYonalishlariSection, Litsenziya, Video, Faq

def HOME_PAGE(request):
    site_settings = SiteSettings.objects.all().last()
    social_networks = SocialNetworks.objects.all().order_by('id')
    home_section = HomeSection.objects.all().last()
    faculties = Facultet.objects.all().order_by('id')
    about_section = AboutSection.objects.all().last()
    talim_yonalishlari = TalimYonalishlariSection.objects.all().order_by('id')
    litsenziya = Litsenziya.objects.all().order_by('id')
    video = Video.objects.all().last()
    faq = Faq.objects.all().order_by('id')

    ctx = {
        'site_settings': site_settings,
        'social_networks': social_networks,
        'home_section': home_section,
        'faculties': faculties,
        'about_section': about_section,
        'talim_yonalishlari': talim_yonalishlari,
        'litsenziya': litsenziya,
        'video': video,
        'faq': faq
    }

    return render(request, 'home.html', ctx)