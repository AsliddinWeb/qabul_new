from django.db import models

from accounts.models import User


# Create your models here.
class Passport(models.Model):
    abituriyent = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255)
    birth_day = models.DateField()

    fuqaroligi = models.CharField(max_length=255) # Davlat
    nation = models.CharField(max_length=255) # Millati
    gender = models.CharField(max_length=255) # Jinsi

    viloyat = models.CharField(max_length=255)
    tuman = models.CharField(max_length=255)
    manzil = models.TextField() # Ko'cha nomi
    kim_tomonidan_berilgan = models.CharField(max_length=555)

    passport_series = models.CharField(max_length=9) # AC2223344
    passport_jshshir = models.CharField(max_length=14)

    passport_file = models.FileField(upload_to='files/passports/')

    def __str__(self):
        return f"{self.passport_series} | {self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Pasportlar"

class Diplom(models.Model):
    abituriyent = models.ForeignKey(User, on_delete=models.CASCADE)
    malumot_turi = models.CharField(max_length=255)
    muassasa_turi = models.CharField(max_length=255)
    muassasa_nomi = models.TextField()
    tugatgan_yili = models.CharField(max_length=255)
    tugatgan_muassasa_joylashgan_viloyat = models.CharField(max_length=255)
    tugatgan_muassasa_joylashgan_tuman = models.CharField(max_length=255)
    diplom_file = models.FileField(upload_to='files/diplomlar/')
    diplom_seriya = models.CharField(max_length=255)
    xalqaro_sertifikat_file = models.FileField(upload_to='files/tavsiyanomalar/', null=True, blank=True)

    def __str__(self):
        return self.diplom_seriya
    class Meta:
        verbose_name_plural = "Diplomlar"

class PerevodDiplom(models.Model):
    abituriyent = models.ForeignKey(User, on_delete=models.CASCADE)
    davlat = models.CharField(max_length=455)
    unv_nomi = models.CharField(max_length=555)
    file = models.FileField(upload_to='perevod/')
    kurs = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Perevod diplomlari"

# class Contact(models.Model):
#     abituriyent = models.ForeignKey(User, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=255)
#     email = models.CharField(max_length=255, null=True, blank=True)
#     izoh = models.TextField(null=True, blank=True)
#
#     def __str__(self):
#         return self.phone_number

