from django import forms
from .models import Application

class ApplicationUpdateKvitansiyaForm(forms.ModelForm):
    kvitansiya_upload = forms.FileField(label="Kvitansiyani yuklash (10 MB dan oshmagan holda)")
    class Meta:
        model = Application
        fields = ['kvitansiya_upload']