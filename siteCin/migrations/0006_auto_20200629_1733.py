# Generated by Django 3.0.3 on 2020-06-29 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteCin', '0005_auto_20200629_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='formats',
        ),
        migrations.AddField(
            model_name='session',
            name='format',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='siteCin.Format', verbose_name='Формат'),
        ),
    ]
