# Generated by Django 3.0.2 on 2020-02-02 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aurthor', '0002_authur_description'),
        ('courses', '0014_auto_20200202_1613'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorie',
            new_name='Category',
        ),
    ]