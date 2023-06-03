# Generated by Django 4.2 on 2023-05-18 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_userverification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userverification',
            name='user',
        ),
        migrations.AddField(
            model_name='userverification',
            name='phone_number',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]