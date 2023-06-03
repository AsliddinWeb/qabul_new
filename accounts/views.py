from .models import User, UserVerification
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Random settings
import random
from django.utils import timezone

from .models import UserVerification
from .forms import UserCreationForm, LoginForm

from uiapp.models import SiteSettings, SocialNetworks
from infoapp.models import Passport, Diplom, PerevodDiplom
from infoapp.forms import PassportForm, DiplomForm, ArizaForm

from .send_sms import send_sms

from requiredapp.models import Region, District, PassportFuqaroligi, Nation
from applicationsapp.models import Application
from applicationsapp.forms import ApplicationUpdateKvitansiyaForm

# DECORATORS
def phone_verification_required(function):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_verification:
            return redirect('phone_verify')
        return function(request, *args, **kwargs)
    return wrapper

def REGISTER(request):
    site_settings = SiteSettings.objects.all().last()
    social_networks = SocialNetworks.objects.all().order_by('id')


    # User login qilib bo'lgan
    if request.user.is_authenticated:
        return redirect('cabinet')
    ctx = {
        'site_settings': site_settings,
        'social_networks': social_networks,
    }

    if request.method == "GET":
        form = UserCreationForm()
        ctx['form'] = form
        return render(request, 'auth/register.html', ctx)

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():


            # Customize ====================================
            random_int = random.randint(1000, 9999)

            # Send sms
            verify = send_sms(form.cleaned_data.get('phone_number'), str(random_int))
            if str(verify.get('status_code')) == "200":
                form.save()
                user = form.cleaned_data.get('phone_number')

                new_verify_code_instance = UserVerification(
                    phone_number=form.cleaned_data.get('phone_number'),
                    code=random_int
                )
                new_verify_code_instance.save()

                messages.success(request, f"{form.cleaned_data.get('phone_number')} raqamiga yuborilgan tasdiqlash kodini kiriting!")

                user = authenticate(request, username=form.cleaned_data.get('phone_number'), password=form.cleaned_data.get('password1'))
                login(request, user)

                return redirect('phone_verify')
            else:
                messages.error(request, "Tasdiqlash kodini yuborishda xatolik yuz berdi qaytadan urinib ko'ring!")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
            ctx['form'] = form

            return render(request, 'auth/register.html', ctx)

    return render(request, 'auth/register.html', ctx)

def LOGIN(request):
    # User login qilib bo'lgan
    if request.user.is_authenticated:
        return redirect('cabinet')

    site_settings = SiteSettings.objects.all().last()
    social_networks = SocialNetworks.objects.all().order_by('id')
    ctx = {
        'site_settings': site_settings,
        'social_networks': social_networks
    }

    if request.method == "GET":
        form = LoginForm()
        ctx['form'] = form
        return render(request, 'auth/login.html', ctx)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = authenticate(request, phone_number=phone_number, password=password)
            if user is not None:
                login(request, user)
                return redirect('cabinet')  # Redirect to the desired page after successful login
            else:
                ctx['form'] = form
                messages.error(request, "Telefon raqam yoki parolda xatolik!")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
            ctx['form'] = form

    return render(request, 'auth/login.html', ctx)

@login_required(login_url='login')
def PHONE_VERIFY(request):
    site_settings = SiteSettings.objects.all().last()
    social_networks = SocialNetworks.objects.all().order_by('id')
    ctx = {
        'site_settings': site_settings,
        'social_networks': social_networks
    }
    if request.method == 'POST':
        code = request.POST.get('code')  # Foydalanuvchidan kiritilgan SMS kod
        phone_number = request.user.phone_number
        last_code = UserVerification.objects.filter(
            phone_number=phone_number
        ).last()
        if last_code is None:
            messages.warning(request, "Noto'g'ri tasdiqlash kodi, iltimos tekshirib qaytadan urinib ko'ring!")
            return render(request, 'auth/phone_verify.html', ctx)
        else:
            if code == last_code.code:
                user = User.objects.get(phone_number=phone_number)
                user.is_verification = True
                user.save()
                return redirect('cabinet')
            else:
                messages.warning(request, "Noto'g'ri tasdiqlash kodi, iltimos tekshirib qaytadan urinib ko'ring!")
                return render(request, 'auth/phone_verify.html', ctx)

    return render(request, 'auth/phone_verify.html', ctx)

@login_required(login_url='login')
@phone_verification_required
def CABINET(request):
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

    passport_form = PassportForm()
    diplom_form = DiplomForm()
    ariza_form = ArizaForm()

    pay_form = ApplicationUpdateKvitansiyaForm()

    if request.method == "POST":
        user = User()
        print(user)
        print(request.FILES['file'])
        # user.image = request.FILES['file']
        # user.save()

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

        'passport_form': passport_form,
        'diplom_form': diplom_form,
        'ariza_form': ariza_form,
        'pay_form': pay_form
    }

    return render(request, 'cabinet/home.html', ctx)

@login_required(login_url='login')
def RESEND_CODE(request):
    site_settings = SiteSettings.objects.all().last()
    social_networks = SocialNetworks.objects.all().order_by('id')
    ctx = {
        'site_settings': site_settings,
        'social_networks': social_networks
    }

    if request.method == 'POST':
        code = request.POST.get('code')  # Foydalanuvchidan kiritilgan SMS kod
        phone_number = request.user.phone_number
        last_code = UserVerification.objects.filter(
            phone_number=phone_number
        ).last()
        if last_code is None:
            messages.warning(request, "Noto'g'ri tasdiqlash kodi, iltimos tekshirib qaytadan urinib ko'ring!")
            return render(request, 'auth/phone_verify.html', ctx)
        else:
            if code == last_code.code:
                user = User.objects.get(phone_number=phone_number)
                user.is_verification = True
                user.save()
                return redirect('cabinet')
            else:
                messages.warning(request, "Noto'g'ri tasdiqlash kodi, iltimos tekshirib qaytadan urinib ko'ring!")
                return render(request, 'auth/phone_verify.html', ctx)

    phone_number = request.user.phone_number
    last_code = UserVerification.objects.filter(
        phone_number=phone_number
    ).last()

    if last_code:
        current_time = timezone.now()
        time_difference = current_time - last_code.created_at

        if time_difference.total_seconds() <= 60:
            messages.warning(request, "Sizga sms kod yuborilgan, 1 daqiqadan so'ng qayta urinib ko'ring!")

            return render(request, 'auth/phone_verify.html', ctx)
        else:
            # Customize
            random_int = random.randint(1000, 9999)

            # Send sms
            send_sms(phone_number, str(random_int))

            # DB saved line
            new_verify_code_instance = UserVerification(
                phone_number=request.user.phone_number,
                code=random_int
            )
            new_verify_code_instance.save()

            messages.success(request, "Sms kod qaytadan yuborildi!")
    else:
        # Customize
        random_int = random.randint(1000, 9999)

        # Send sms
        send_sms(phone_number, str(random_int))

        # DB saved line
        new_verify_code_instance = UserVerification(
            phone_number=request.user.phone_number,
            code=random_int
        )
        new_verify_code_instance.save()

        messages.success(request, "Sms kod qaytadan yuborildi!")

    return render(request, 'auth/phone_verify.html', ctx)


def RESET_PASSWORD_1(request):
    site_settings = SiteSettings.objects.all().last()
    social_networks = SocialNetworks.objects.all().order_by('id')
    ctx = {
        'site_settings': site_settings,
        'social_networks': social_networks
    }

    if request.method == 'POST':
        phone_number = request.POST['phone_number']

        # Telefon raqami va SMS-kodni tekshirish
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            user = None

        if user is not None:
            last_code = UserVerification.objects.filter(
                phone_number=phone_number
            ).last()

            current_time = timezone.now()
            time_difference = current_time - last_code.created_at

            if time_difference.total_seconds() <= 60:
                messages.warning(request, "Sizga sms kod yuborilgan, 1 daqiqadan so'ng qayta urinib ko'ring!")
            else:
                # Customize
                random_int = random.randint(1000, 9999)

                # Send sms
                send_sms(phone_number, str(random_int))

                # DB saved line
                new_verify_code_instance = UserVerification(
                    phone_number=phone_number,
                    code=random_int
                )
                new_verify_code_instance.save()
                messages.success(request, 'Sms kod yuborildi.')
                return redirect('reset_password_2')
        else:
            messages.error(request, 'Telefon raqam xato!')

    return render(request, 'auth/reset_password_1.html', ctx)

def RESET_PASSWORD_2(request):
    site_settings = SiteSettings.objects.all().last()
    social_networks = SocialNetworks.objects.all().order_by('id')
    ctx = {
        'site_settings': site_settings,
        'social_networks': social_networks
    }

    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        sms_code = request.POST['code']
        new_password = request.POST['password']

        # Telefon raqami va SMS-kodni tekshirish
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            user = None

        if user is not None and UserVerification.objects.filter(phone_number=phone_number).last().code == sms_code:
            # Parolni yangilash
            user.set_password(new_password)
            user.save()

            messages.success(request, 'Parolingiz muvaffaqiyatli yangilandi.')
            return redirect('login')
        else:
            messages.error(request, 'Sms kod xato, tekshirib qaytadan urinib ko\'ring!')

    return render(request, 'auth/reset_password_2.html', ctx)

@login_required(login_url='login')
def LOGOUT(request):
    logout(request)
    return redirect('home_page')

@login_required(login_url='login')
def LOGOUT_REGISTER(request):
    logout(request)
    return redirect('register')

