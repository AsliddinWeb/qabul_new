# Generated by Django 4.2 on 2023-05-24 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicationsapp', '0004_application_passport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='contact',
        ),
    ]
