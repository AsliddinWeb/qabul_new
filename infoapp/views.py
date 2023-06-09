from django.http import JsonResponse
from uiapp.models import SiteSettings, SocialNetworks

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import Passport, Diplom, PerevodDiplom
from applicationsapp.models import Application
from applicationsapp.new_pdf import create_word_template, create_malumotnoma

from requiredapp.models import District, Region, PassportFuqaroligi, Nation

from .forms import PassportForm, DiplomForm, ArizaForm, PerevodDiplomForm
from accounts.models import User
from accounts.forms import UserUpdateImageForm
from accounts.send_sms import send_sms_ariza_topshirilidi

from requiredapp.models import TalimShakli, TalimYonalishi


# DECORATORS
def phone_verification_required(function):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_verification:
            return redirect('phone_verify')
        return function(request, *args, **kwargs)
    return wrapper

@login_required(login_url='login')
@phone_verification_required
def CABINET_PASSPORT(request):
    site_settings = SiteSettings.objects.all().last()
    social_networks = SocialNetworks.objects.all().order_by('id')
    viloyatlar = Region.objects.all().order_by('id')
    tumanlar = District.objects.all().order_by('id')
    davlatlar = PassportFuqaroligi.objects.all().order_by('id')
    millatlar = Nation.objects.all().order_by('id')

    passport_info = Passport.objects.filter(abituriyent=request.user).last()
    diplom_info = Diplom.objects.filter(abituriyent=request.user).last()
    perevod_diplom_info = PerevodDiplom.objects.filter(abituriyent=request.user).last()
    ariza_info = Application.objects.filter(abituriyent=request.user).last()

    ctx = {
        'site_settings': site_settings,
        'social_networks': social_networks,

        'passport_info': passport_info,
        'diplom_info': diplom_info,
        'perevod_diplom_info': perevod_diplom_info,
        'ariza_info': ariza_info,

        'viloyatlar': viloyatlar,
        'tumanlar': tumanlar,
        'davlatlar': davlatlar,
        'millatlar': millatlar,
        # 'passport_form': passport_form,
    }

    if passport_info is not None:
        obj = get_object_or_404(Passport, pk=passport_info.id)
        passport_form = PassportForm(request.POST or None, instance=obj)

        if passport_form.is_valid():
            obj = passport_form.save(commit=False)

            obj.viloyat = Region.objects.get(
                id=obj.viloyat).name
            obj.tuman = District.objects.get(
                id=obj.tuman).name
            obj.save()

            messages.success(request, "Passport ma'lumotlaringiz muvaffaqqiyatli o'zgartirildi!")
            return redirect('cabinet_passport')
        ctx['passport_form'] = passport_form
    else:
        if request.method == 'POST':
            passport_form = PassportForm(request.POST, request.FILES)
            if passport_form.is_valid():
                passport = passport_form.save(commit=False)  # Bazaga saqlamaymiz
                passport.abituriyent = request.user  # abituriyent ni request.user ga tenglaymiz
                passport.viloyat = Region.objects.get(id=passport.viloyat).name
                passport.tuman = District.objects.get(id=passport.tuman).name
                print(passport.tuman)

                passport.save()  # Keyin saqlaymiz
                messages.success(request, "Ajoyib. Passport ma'lumotlaringiz muvaffaqqiyatli saqlandi!")
                return redirect('cabinet_diplom')  # Redirect to a success page
        else:
            passport_form = PassportForm()
        ctx['passport_form'] = passport_form

    return render(request, 'cabinet/passport.html', ctx)

@login_required(login_url='login')
@phone_verification_required
def CABINET_DIPLOM(request):
    site_settings = SiteSettings.objects.all().last()
    social_networks = SocialNetworks.objects.all().order_by('id')

    passport_info = Passport.objects.filter(abituriyent=request.user).last()
    diplom_info = Diplom.objects.filter(abituriyent=request.user).last()
    perevod_diplom_info = PerevodDiplom.objects.filter(abituriyent=request.user).last()
    ariza_info = Application.objects.filter(abituriyent=request.user).last()

    ctx = {
        'site_settings': site_settings,
        'social_networks': social_networks,

        'passport_info': passport_info,
        'diplom_info': diplom_info,
        'perevod_diplom_info': perevod_diplom_info,
        'ariza_info': ariza_info,
    }

    if diplom_info is not None:
        obj = get_object_or_404(Diplom, pk=diplom_info.id)
        diplom_form = DiplomForm(request.POST or None, instance=obj)

        if diplom_form.is_valid():
            obj = diplom_form.save(commit=False)

            obj.tugatgan_muassasa_joylashgan_viloyat = Region.objects.get(
                id=obj.tugatgan_muassasa_joylashgan_viloyat).name
            obj.tugatgan_muassasa_joylashgan_tuman = District.objects.get(
                id=obj.tugatgan_muassasa_joylashgan_tuman).name
            obj.save()
            messages.success(request, "Diplom ma'lumotlaringiz muvaffaqqiyatli o'zgartirildi!")
            return redirect('cabinet_diplom')
        ctx['diplom_form'] = diplom_form
    else:
        if request.method == 'POST':
            diplom_form = DiplomForm(request.POST, request.FILES)
            if diplom_form.is_valid():
                diplom = diplom_form.save(commit=False)  # Bazaga saqlamaymiz
                diplom.abituriyent = request.user

                diplom.tugatgan_muassasa_joylashgan_viloyat = Region.objects.get(id=diplom.tugatgan_muassasa_joylashgan_viloyat).name
                diplom.tugatgan_muassasa_joylashgan_tuman = District.objects.get(id=diplom.tugatgan_muassasa_joylashgan_tuman).name

                diplom.save()  # Keyin saqlaymiz
                messages.success(request, "Ajoyib. Diplom ma'lumotlaringiz muvaffaqqiyatli saqlandi!")
                return redirect('cabinet_ariza')
        else:
            diplom_form = DiplomForm()
        ctx['diplom_form'] = diplom_form

    return render(request, 'cabinet/diplom.html', ctx)

@login_required(login_url='login')
@phone_verification_required
def CABINET_PEREVOD_DIPLOM(request):
    site_settings = SiteSettings.objects.all().last()
    social_networks = SocialNetworks.objects.all().order_by('id')

    passport_info = Passport.objects.filter(abituriyent=request.user).last()
    diplom_info = Diplom.objects.filter(abituriyent=request.user).last()
    perevod_diplom_info = PerevodDiplom.objects.filter(abituriyent=request.user).last()
    ariza_info = Application.objects.filter(abituriyent=request.user).last()

    ctx = {
        'site_settings': site_settings,
        'social_networks': social_networks,

        'passport_info': passport_info,
        'diplom_info': diplom_info,
        'perevod_diplom_info': perevod_diplom_info,
        'ariza_info': ariza_info,
    }

    if perevod_diplom_info is not None:
        obj = get_object_or_404(PerevodDiplom, pk=perevod_diplom_info.id)
        perevod_diplom_form = PerevodDiplomForm(request.POST or None, instance=obj)

        if perevod_diplom_form.is_valid():
            perevod_diplom_form.save()
            messages.success(request, "Diplom ma'lumotlaringiz muvaffaqqiyatli o'zgartirildi!")
            return redirect('cabinet_perevod_diplom')
        ctx['perevod_diplom_form'] = perevod_diplom_form
    else:
        if request.method == 'POST':
            perevod_diplom_form = PerevodDiplomForm(request.POST, request.FILES)
            if perevod_diplom_form.is_valid():
                diplom = perevod_diplom_form.save(commit=False)  # Bazaga saqlamaymiz
                diplom.abituriyent = request.user
                diplom.save()  # Keyin saqlaymiz
                messages.success(request, "Ajoyib. Diplom ma'lumotlaringiz muvaffaqqiyatli saqlandi!")
                return redirect('cabinet_ariza')
        else:
            perevod_diplom_form = PerevodDiplomForm()
        ctx['perevod_diplom_form'] = perevod_diplom_form

    return render(request, 'cabinet/diplom-perevod.html', ctx)

@login_required(login_url='login')
@phone_verification_required
def CABINET_ARIZA(request):
    value = "add"
    site_settings = SiteSettings.objects.all().last()
    social_networks = SocialNetworks.objects.all().order_by('id')

    passport_info = Passport.objects.filter(abituriyent=request.user).last()
    diplom_info = Diplom.objects.filter(abituriyent=request.user).last()
    perevod_diplom_info = PerevodDiplom.objects.filter(abituriyent=request.user).last()

    if passport_info is None or (perevod_diplom_info or diplom_info) is None:
        messages.error(request, "Barcha ma'lumotlaringiz kiritilganligini tekshirib ko'ring va qayta urinib ko'ring!")
        return redirect('cabinet')

    ariza_info = Application.objects.filter(abituriyent=request.user).last()

    ctx = {
        'site_settings': site_settings,
        'social_networks': social_networks,

        'passport_info': passport_info,
        'diplom_info': diplom_info,
        'perevod_diplom_info': perevod_diplom_info,
        'ariza_info': ariza_info,
        'value': value
    }

    if ariza_info is not None:
        obj = get_object_or_404(Application, pk=ariza_info.id)
        ariza_form = ArizaForm(request.POST or None, instance=obj)

        if ariza_form.is_valid():
            ariza = ariza_form.save(commit=False)
            ariza.talim_turi = "Bakalavr"
            ariza.talim_shakli = TalimShakli.objects.get(id=ariza.talim_shakli).name
            ariza.talim_yonalishi = TalimYonalishi.objects.get(id=ariza.talim_yonalishi).name

            if perevod_diplom_info:
                ariza.is_perevod = True

                ariza.perevod_diplom = perevod_diplom_info
            else:
                ariza.diplom = diplom_info

            # INVOYS GENERATSIYA =================
            name = f"{ariza.passport.last_name} {ariza.passport.first_name} {ariza.passport.other_name}"
            create_word_template(name, ariza.passport.passport_series)

            # =================================

            ariza.save()
            messages.success(request, "Arizangiz muvaffaqqiyatli o'zgartirildi!")
            return redirect('cabinet')
        ctx['ariza_form'] = ariza_form

        value = "edit"
        ctx['value'] = value
    else:
        if request.method == 'POST':
            ariza_form = ArizaForm(request.POST, request.FILES)
            if ariza_form.is_valid():
                ariza = ariza_form.save(commit=False)  # Bazaga saqlamaymiz
                ariza.abituriyent = request.user
                ariza.passport = passport_info
                ariza.talim_turi = "Bakalavr"
                ariza.talim_shakli = TalimShakli.objects.get(id=ariza.talim_shakli).name
                ariza.talim_yonalishi = TalimYonalishi.objects.get(id=ariza.talim_yonalishi).name

                if perevod_diplom_info:
                    ariza.is_perevod = True

                    ariza.perevod_diplom = perevod_diplom_info
                else:
                    ariza.diplom = diplom_info


                # INVOYS GENERATSIYA =================
                name = f"{ariza.passport.last_name} {ariza.passport.first_name} {ariza.passport.other_name}"
                create_word_template(name, ariza.passport.passport_series)

                # =================================

                ariza.save()  # Keyin saqlaymiz
                messages.success(request, "Arizangiz muvaffaqqiyatli qabul qilindi!")

                # Sms orqali xabarnoma
                send_sms_ariza_topshirilidi(str(request.user.phone_number), str(ariza.id))

                return redirect('cabinet')
        else:
            ariza_form = ArizaForm()
        ctx['ariza_form'] = ariza_form

    return render(request, 'cabinet/ariza.html', ctx)

@login_required(login_url='login')
@phone_verification_required
def CABINET_UPLOAD_IMAGE(request):
    if request.method == 'POST':
        user = get_object_or_404(User, phone_number=request.user.phone_number)
        if request.method == 'POST':
            form = UserUpdateImageForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, "Profil rasmingiz muvaffaqqiyatli saqlandi!")
                return redirect('cabinet')
            else:
                messages.error(request, "Rasm yuklashda xatolik!")
                return redirect('cabinet')
        else:
            form = UserUpdateImageForm(instance=user)
            messages.error(request, "Rasm yuklashda xatolik!")
            return redirect('cabinet')




def viloyatlar_api(request):
    viloyatlar = Region.objects.all().values('id', 'name')
    return JsonResponse({'viloyatlar': list(viloyatlar)})

def tumanlar_api(request, viloyat_id):
    tumanlar = District.objects.filter(region=viloyat_id).values('id', 'name')
    return JsonResponse({'tumanlar': list(tumanlar)})

def talim_shakli_api(request):
    talim_shakllar = TalimShakli.objects.all().values('id', 'name')
    return JsonResponse({'talim_shakllari': list(talim_shakllar)})

def yonalishlar_api(request, talim_shakli_id):
    yonalishlar = TalimYonalishi.objects.filter(talim_shakli__id=talim_shakli_id).values('id', 'name')
    return JsonResponse({'yonalishlar': list(yonalishlar)})