# Generated by Django 3.1.1 on 2021-07-12 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubsapp', '0005_alter_clubs_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubs',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
