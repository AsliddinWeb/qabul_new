# Generated by Django 4.2 on 2023-05-24 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uiapp', '0008_alter_facultet_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultet',
            name='body',
            field=models.TextField(null=True),
        ),
    ]