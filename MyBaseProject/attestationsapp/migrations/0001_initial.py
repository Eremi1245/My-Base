# Generated by Django 3.2.5 on 2021-07-11 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clubsapp', '0005_alter_clubs_status'),
        ('stadiumsapp', '0002_alter_stadiums_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attestations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_year', models.CharField(max_length=4, verbose_name='Год Аттестации')),
                ('application_1', models.FileField(blank=True, upload_to='attestations_documents', verbose_name='Заявление о процедуре аттестации')),
                ('application_2', models.FileField(blank=True, upload_to='attestations_documents', verbose_name='Проведение политики недопущения дискриминации')),
                ('application_3', models.FileField(blank=True, upload_to='attestations_documents', verbose_name='Согласие на соблюдение регламентов')),
                ('application_4', models.FileField(blank=True, upload_to='attestations_documents', verbose_name='Список сотрудников')),
                ('application_5', models.FileField(blank=True, upload_to='attestations_documents', verbose_name='Гарантийное письмо')),
                ('document', models.CharField(choices=[('аренда', 'Аренда'), ('Право оперативного пользования', 'Право оперативного пользования'), ('Свидетельство о собственности', 'Свидетельство о собственности')], default='Нет', max_length=32, verbose_name='Право пользования стадионом')),
                ('notes', models.TextField(blank=True, verbose_name='Примечание')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubsapp.clubs', verbose_name='Клуб')),
                ('stadium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stadiumsapp.stadiums', verbose_name='Стадион')),
            ],
            options={
                'verbose_name': 'Аттестация',
                'verbose_name_plural': 'Аттестации',
            },
        ),
    ]