# Generated by Django 4.2 on 2023-05-25 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicationsapp', '0006_application_abituriyent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name_plural': 'Barcha Arizalar'},
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Topshirildi', 'Topshirildi'), ("To'lov qilindi", "To'lov qilindi"), ("O'qishga qabul qilindi", "O'qishga qabul qilindi"), ('Bekor qilingan', 'Bekor qilingan')], default='Topshirildi', max_length=100),
        ),
    ]
