# Generated by Django 3.0.3 on 2020-06-30 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteCin', '0007_remove_reviews_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='email',
        ),
    ]
