# Generated by Django 3.0.3 on 2020-07-01 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteCin', '0012_auto_20200630_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster_2',
            field=models.ImageField(default=1, upload_to='images/', verbose_name='Постер_2'),
        ),
    ]