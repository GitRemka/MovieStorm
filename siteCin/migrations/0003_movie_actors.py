# Generated by Django 3.0.3 on 2020-06-02 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteCin', '0002_auto_20200602_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='film_actor', to='siteCin.Actor', verbose_name='актеры'),
        ),
    ]
