from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User

from .forms import ApplicationUpdateKvitansiyaForm
from .models import Application

from django.contrib import messages

def phone_verification_required(function):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_verification:
            return redirect('phone_verify')
        return function(request, *args, **kwargs)
    return wrapper

@login_required(login_url='login')
@phone_verification_required
def CABINET_UPLOAD_KVITANSIYA(request):
    if request.method == 'POST':
        application = get_object_or_404(Application, abituriyent=request.user)
        if request.method == 'POST':
            ariza_form = ApplicationUpdateKvitansiyaForm(request.POST, request.FILES, instance=application)
            if ariza_form.is_valid():
                ariza_form.save()
                messages.success(request, "To'lov ma'lumotlari muvaffaqqiyatli yuborildi!")
                return redirect('cabinet')
            else:
                messages.error(request, "To'lov ma'lumotlarini yuborishda xatolik!")
                return redirect('cabinet')
        else:
            ariza_form = ApplicationUpdateKvitansiyaForm(instance=application)
            messages.error(request, "To'lov ma'lumotlarini yuborishda xatolik!")
            return redirect('cabinet')