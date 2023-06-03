from django.db import models

# Create your models here.
class HomeSection(models.Model):
    h1 = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField()
    button_href = models.CharField(max_length=255)
    button_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/ui')

    background_image = models.ImageField(upload_to='images/ui', null=True)

    def __str__(self):
        return self.h1

class AboutSection(models.Model):
    image_1 = models.ImageField(upload_to='images/ui')
    image_2 = models.ImageField(upload_to='images/ui')
    image_3 = models.ImageField(upload_to='images/ui')

    subtitle = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField()

    icon = models.CharField(max_length=255)
    count = models.CharField(max_length=255)
    what = models.CharField(max_length=255)
    what_body = models.CharField(max_length=255)

    button_href = models.CharField(max_length=255)
    button_title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class TalimYonalishlariSection(models.Model):
    image = models.ImageField(upload_to='images/ui')
    title = models.CharField(max_length=255)

    p1 = models.CharField(max_length=255)
    p2 = models.CharField(max_length=255)

    button_href = models.CharField(max_length=255)
    button_title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Litsenziya(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    button_href = models.CharField(max_length=255)
    button_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/ui')

class Video(models.Model):
    subtitle = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/ui')
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.url

class Faq(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title

class Facultet(models.Model):
    icon = models.FileField(upload_to='images/ui', null=True)
    title = models.CharField(max_length=255)
    body = models.TextField(null=True)

    button_title = models.CharField(max_length=255)
    button_href = models.CharField(max_length=255)


class SiteSettings(models.Model):
    keywords = models.TextField()
    description = models.TextField()
    site_title = models.TextField()
    author = models.TextField()

    logo = models.ImageField(upload_to='images/ui')
    footer_logo = models.ImageField(upload_to='images/ui', null=True, blank=True)
    favicon = models.ImageField(upload_to='images/ui')

    phone_1 = models.CharField(max_length=255)
    phone_2 = models.CharField(max_length=255)
    right_text = models.CharField(max_length=455, null=True)

class SocialNetworks(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    link = models.CharField(max_length=455)

    def __str__(self):
        return self.title