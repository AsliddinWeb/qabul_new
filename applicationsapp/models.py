from accounts.models import User
from django.db import models

from infoapp.models import Passport, Diplom, PerevodDiplom

# Create your models here.
class Application(models.Model):
    abituriyent = models.ForeignKey(User, on_delete=models.CASCADE)
    talim_turi = models.CharField(max_length=255)
    talim_shakli = models.CharField(max_length=255)
    passport = models.ForeignKey(Passport, on_delete=models.CASCADE)

    is_perevod = models.BooleanField(default=False)
    diplom = models.ForeignKey(Diplom, on_delete=models.CASCADE, null=True, blank=True)
    perevod_diplom = models.ForeignKey(PerevodDiplom, on_delete=models.CASCADE, null=True, blank=True)

    talim_yonalishi = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    STATUS_CHOISES = (
        ("Topshirildi", "Topshirildi"),
        ("To'lov qilindi", "To'lov qilindi"),
        ("O'qishga qabul qilindi", "O'qishga qabul qilindi"),
        ("Bekor qilingan", "Bekor qilingan"),
    )

    status = models.CharField(max_length=100,
                             choices=STATUS_CHOISES,
                             default="Topshirildi")
    # is_payment = models.BooleanField(default=False)
    xatolik_sababi = models.TextField(null=True, blank=True)
    kvitansiya_upload = models.FileField(upload_to='kvitansiyalar', null=True, blank=True)

    def __str__(self):
        return f"{self.passport.first_name} {self.passport.last_name}"

    class Meta:
        verbose_name_plural = "Barcha Arizalar"