# Generated by Django 3.2.5 on 2021-07-11 18:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubstateapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubsstate',
            name='licence_under',
            field=models.DateField(default=datetime.date(1, 1, 1), verbose_name='Лицензия до'),
        ),
    ]