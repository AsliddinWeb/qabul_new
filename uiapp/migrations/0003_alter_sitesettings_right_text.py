# Generated by Django 4.2 on 2023-05-24 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uiapp', '0002_sitesettings_right_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='right_text',
            field=models.CharField(max_length=455, null=True),
        ),
    ]
