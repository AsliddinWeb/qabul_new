# Generated by Django 4.2 on 2023-05-23 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userverification',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]