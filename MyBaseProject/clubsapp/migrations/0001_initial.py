# Generated by Django 3.2.5 on 2021-07-11 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Название')),
                ('shrt_name', models.CharField(max_length=128, unique=True, verbose_name='Сокращенное Название')),
                ('email', models.EmailField(max_length=254, verbose_name='почта')),
                ('o_p_f', models.CharField(max_length=128, verbose_name='Форма')),
                ('jur_addr', models.CharField(max_length=128, verbose_name='Офиц. Адрес')),
                ('fact_addr', models.CharField(max_length=128, verbose_name='Факт. Адрес')),
                ('site', models.URLField(verbose_name='Сайт')),
                ('inn', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='ИНН')),
                ('ogrn', models.DecimalField(decimal_places=0, max_digits=13, verbose_name='ОГРН')),
                ('bank_name', models.CharField(max_length=128, verbose_name='Имя Банка')),
                ('check_ac', models.CharField(max_length=20, verbose_name='Расчетный счет')),
                ('ustav', models.FileField(default=0, upload_to='<django.db.models.fields.CharField>', verbose_name='Устав')),
                ('reg_in_min_just', models.FileField(default=0, upload_to='<django.db.models.fields.CharField>', verbose_name='МинЮст')),
                ('reg_in_tax', models.FileField(default=0, upload_to='<django.db.models.fields.CharField>', verbose_name='Налоговая')),
                ('creat_club', models.FileField(default=0, upload_to='<django.db.models.fields.CharField>', verbose_name='Создание')),
                ('creat_rucovod', models.FileField(default=0, upload_to='<django.db.models.fields.CharField>', verbose_name='Руководитель')),
                ('ofice', models.FileField(default=0, upload_to='<django.db.models.fields.CharField>', verbose_name='Офис')),
                ('notes', models.TextField(blank=True, verbose_name='Примечание')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'клуб',
                'verbose_name_plural': 'клубы',
            },
        ),
    ]