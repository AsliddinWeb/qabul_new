# Generated by Django 4.2 on 2023-05-30 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicationsapp', '0010_application_xatolik_sababi'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
