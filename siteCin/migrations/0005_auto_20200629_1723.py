# Generated by Django 3.0.3 on 2020-06-29 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteCin', '0004_auto_20200609_1803'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='session',
            options={'ordering': ('movie',), 'verbose_name': 'Сеанс', 'verbose_name_plural': 'Сеансы'},
        ),
        migrations.RemoveField(
            model_name='movie',
            name='formats',
        ),
        migrations.AddField(
            model_name='session',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата сеанса'),
        ),
        migrations.AddField(
            model_name='session',
            name='formats',
            field=models.ManyToManyField(to='siteCin.Format', verbose_name='Форматы'),
        ),
    ]