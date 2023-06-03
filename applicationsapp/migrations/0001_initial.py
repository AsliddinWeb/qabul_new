# Generated by Django 4.2 on 2023-04-29 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('infoapp', '0005_diplom_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talim_turi', models.CharField(max_length=255)),
                ('talim_shakli', models.CharField(max_length=255)),
                ('talim_yonalishi', models.CharField(max_length=255)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infoapp.contact')),
                ('diplom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infoapp.diplom')),
                ('passport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infoapp.passport')),
            ],
        ),
    ]