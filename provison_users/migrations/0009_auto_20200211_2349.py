# Generated by Django 3.0.2 on 2020-02-11 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provison_users', '0008_auto_20200211_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]
