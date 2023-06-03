from django.db import models

# Create your models here.
# Millati +
class Nation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Jins +
class Sex(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Viloyat +
class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Tuman +
class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TalimTuri(models.Model): # Magistr, bakalavr
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# +++++
class TalimShakli(models.Model): # Kunduzgi, kechki
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Ta'lim shakllari"

# Iqtisod, moliya, ...
class TalimYonalishi(models.Model):
    # talim_turi = models.ForeignKey(TalimTuri, on_delete=models.CASCADE)
    talim_shakli = models.ForeignKey(TalimShakli, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Diplom
class DiplomMalumotTuri(models.Model): # O'rta, o'rta maktab, oliy
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class DiplomMuassasaTuri(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PassportFuqaroligi(models.Model): # Uzb, Russiya
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
