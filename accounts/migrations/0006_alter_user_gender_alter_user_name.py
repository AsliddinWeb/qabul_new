# Generated by Django 4.2 on 2023-05-01 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_first_name_user_name_remove_user_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
