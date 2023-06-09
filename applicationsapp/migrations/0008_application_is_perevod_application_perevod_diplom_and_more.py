# Generated by Django 4.2 on 2023-05-28 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infoapp', '0014_perevoddiplom_abituriyent'),
        ('applicationsapp', '0007_alter_application_options_alter_application_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='is_perevod',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='perevod_diplom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='infoapp.perevoddiplom'),
        ),
        migrations.AlterField(
            model_name='application',
            name='diplom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='infoapp.diplom'),
        ),
    ]
