# Generated by Django 4.2 on 2023-04-29 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicationsapp', '0002_application_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='passport',
        ),
    ]
