# Generated by Django 3.2.5 on 2021-07-11 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clubsapp', '0005_alter_clubs_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubsState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Имя')),
                ('secondname', models.CharField(max_length=128, verbose_name='Фамилия')),
                ('patrom', models.CharField(max_length=128, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=128, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='почта')),
                ('post', models.CharField(max_length=128, verbose_name='должность')),
                ('doc_of_study', models.FileField(blank=True, upload_to='clubs state documents', verbose_name='Лицензия/Документ об образовании')),
                ('licence_under', models.DateField(blank=True, verbose_name='Лицензия до')),
                ('notes', models.TextField(blank=True, verbose_name='Примечание')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubsapp.clubs', verbose_name='клуб')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
            },
        ),
    ]