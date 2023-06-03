from django import forms
from .models import Passport, Diplom, PerevodDiplom
from applicationsapp.models import Application
from requiredapp.models import Nation, PassportFuqaroligi, Sex, Region, \
    District, TalimShakli, TalimYonalishi, DiplomMalumotTuri, DiplomMuassasaTuri

class PassportForm(forms.ModelForm):
    first_name = forms.CharField(label='Ism', widget=forms.TextInput(attrs={'placeholder': 'Ism...'}))
    last_name = forms.CharField(label='Familiya', widget=forms.TextInput(attrs={'placeholder': 'Familiya...'}))
    other_name = forms.CharField(label='Otasinging ismi', widget=forms.TextInput(attrs={'placeholder': 'Otasining ismi...'}))
    passport_series = forms.CharField(label='Passport seriya', widget=forms.TextInput(attrs={'placeholder': 'AA1234567'}), max_length=9, min_length=9)
    passport_jshshir = forms.CharField(label='Jshshir', widget=forms.TextInput(attrs={'placeholder': 'Jshshir...', 'type': 'number'}), max_length=14, min_length=14)
    passport_file = forms.FileField(label='Passport fayli')

    nation = forms.ModelChoiceField(queryset=Nation.objects.all(), label="Millati")
    gender = forms.ModelChoiceField(queryset=Sex.objects.all(), label="Jinsi")
    fuqaroligi = forms.ModelChoiceField(queryset=PassportFuqaroligi.objects.all())
    birth_day = forms.DateField(label="Tog'ilgan sana", widget=forms.DateInput(attrs={'type': 'date'}))

    viloyat = forms.CharField(widget=forms.Select())
    tuman = forms.CharField(widget=forms.Select())
    class Meta:
        model = Passport
        fields = "__all__"
        exclude = ['abituriyent']

class DiplomForm(forms.ModelForm):
    malumot_turi = forms.ModelChoiceField(queryset=DiplomMalumotTuri.objects.all(), label="Ma'lumot turi")
    muassasa_turi = forms.ModelChoiceField(queryset=DiplomMuassasaTuri.objects.all(), label="Muassasa turi")
    tugatgan_yili = forms.CharField(label="Tugatgan yili", widget=forms.NumberInput())

    tugatgan_muassasa_joylashgan_viloyat = forms.CharField(widget=forms.Select(attrs={'id': 'id_viloyat'}))
    tugatgan_muassasa_joylashgan_tuman = forms.CharField(widget=forms.Select(attrs={'id': 'id_tuman'}))


    class Meta:
        model = Diplom
        fields = "__all__"
        exclude = ['abituriyent']

class PerevodDiplomForm(forms.ModelForm):
    davlat = forms.ModelChoiceField(queryset=PassportFuqaroligi.objects.all())
    unv_nomi = forms.CharField(label="Universitet nomi")
    file = forms.FileField(label="Akademik ma'lumotnoma yoki Transkript")

    kurslar = (
        ("1-kurs", "1-kurs"),
        ("2-kurs", "2-kurs"),
    )
    kurs = forms.ChoiceField(choices=kurslar)
    class Meta:
        model = PerevodDiplom
        fields = "__all__"
        exclude = ['abituriyent']

class ArizaForm(forms.ModelForm):
    talim_shakli = forms.CharField(widget=forms.Select())
    talim_yonalishi = forms.CharField(widget=forms.Select())
    # talim_shakli = forms.ModelChoiceField(queryset=TalimShakli.objects.all(), label="Ta'lim shakli")
    # talim_yonalishi = forms.ModelChoiceField(queryset=TalimYonalishi.objects.all(), label="Yo'nalish")
    class Meta:
        model = Application
        fields = "__all__"
        exclude = ['abituriyent', 'passport', 'diplom', 'is_perevod',
                   'perevod_diplom', 'status', 'talim_turi', 'xatolik_sababi',
                   'is_payment', 'kvitansiya_upload']