# Generated by Django 4.2 on 2023-04-29 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requiredapp', '0002_diplommalumotturi_diplommuassasaturi_talimshakli_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassportFuqaroligi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
