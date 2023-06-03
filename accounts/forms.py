from django import forms
from django.utils.translation import gettext_lazy as _

from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm as UserCreationF

from .models import User


class UserCreationForm(UserCreationF):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].initial = '+998'

    phone_number = PhoneNumberField(required=True, label="Telefon raqam", error_messages={
        'invalid': "Telefon raqam noto'g'ri kiritildi. Namuna: +998901234567"
    })
    name = forms.CharField(label='Ism, Familiya', widget=forms.TextInput, required=True)
    password1 = forms.CharField(label='Parol', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Parolni tasdiqlang', widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ('phone_number', 'name', 'password1', 'password2')
        widgets = {
            'phone_number': forms.TextInput(attrs={'type': 'tel'}),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Bu raqam bilan avval ro'yhatdan o'tilgan. Shaxsiy kabinetingizga kiring!")
        return phone_number

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].initial = '+998'

    phone_number = PhoneNumberField(label="Telefon raqam", error_messages={
        'invalid': "Telefon raqam noto'g'ri kiritildi. Namuna: +998901234567"
    })
    password = forms.CharField(widget=forms.PasswordInput, label="Parol")

class UserUpdateImageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image']