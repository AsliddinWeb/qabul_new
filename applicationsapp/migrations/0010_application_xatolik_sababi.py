# Generated by Django 4.2 on 2023-05-29 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicationsapp', '0009_application_is_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='xatolik_sababi',
            field=models.TextField(blank=True, null=True),
        ),
    ]