from django.contrib.auth.models import BaseUserManager

class MyUserManager(BaseUserManager):

    def create_user(self, phone_number, name, password=None):
        if not phone_number:
            raise ValueError("Telefon raqam majburiy!")
        elif not name:
            raise ValueError("Ism majburiy")


        user = self.model(phone_number=phone_number, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, name, password, **kwargs):
        user = self.create_user(phone_number=phone_number, name=name, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user