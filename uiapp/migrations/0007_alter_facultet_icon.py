# Generated by Django 4.2 on 2023-05-24 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uiapp', '0006_remove_homesection_button_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultet',
            name='icon',
            field=models.FileField(null=True, upload_to='images/ui'),
        ),
    ]
