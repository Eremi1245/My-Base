# Generated by Django 3.2.5 on 2021-07-11 18:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stadiumsapp', '0002_alter_stadiums_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stadiums',
            name='act_categ_date_until',
            field=models.DateField(default=datetime.date(1, 1, 1), verbose_name='Акт категорирования до'),
        ),
        migrations.AlterField(
            model_name='stadiums',
            name='instr_pub_order_date_until',
            field=models.DateField(default=datetime.date(1, 1, 1), verbose_name='Инструкция безопасности до'),
        ),
    ]
