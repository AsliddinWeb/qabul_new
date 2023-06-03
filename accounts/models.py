from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import MyUserManager

from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


class User(AbstractBaseUser):
    phone_number = PhoneNumberField(unique=True,)
    is_verification = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)

    # No required
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='users/profile', null=True, blank=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        if self.name:
            return f"{self.name} | {str(self.phone_number)}"
        else:
            return str(self.phone_number)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_all_permissions(user=None):
        if user.is_admin:
            return set()

    @property
    def is_staff(self):
        return self.is_admin

class UserVerification(models.Model):
    phone_number = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    is_checked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.phone_number} | {self.code}"
