# Generated by Django 4.2 on 2023-05-24 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uiapp', '0004_homesection_background_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='homesection',
            name='button_image',
            field=models.ImageField(null=True, upload_to='images/ui'),
        ),
    ]