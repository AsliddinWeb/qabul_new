# Generated by Django 4.2 on 2023-05-28 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicationsapp', '0008_application_is_perevod_application_perevod_diplom_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='is_payment',
            field=models.BooleanField(default=False),
        ),
    ]