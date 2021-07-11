# Generated by Django 3.2.5 on 2021-07-11 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubsapp', '0004_clubs_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubs',
            name='status',
            field=models.CharField(choices=[('Допущен', 'Допущен до соревнования'), ('Не Допущен', 'Не допущен до соревнования')], default='Не Допущен', max_length=32, verbose_name='Статус'),
        ),
    ]