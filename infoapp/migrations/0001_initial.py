# Generated by Django 4.2 on 2023-04-28 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('other_name', models.CharField(max_length=255)),
                ('birth_day', models.DateTimeField()),
                ('nation', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('place_of_birth', models.TextField()),
                ('passport_series', models.CharField(max_length=7)),
                ('passport_jshshir', models.CharField(max_length=14)),
                ('passport_file', models.FileField(upload_to='files/passports/')),
            ],
        ),
    ]