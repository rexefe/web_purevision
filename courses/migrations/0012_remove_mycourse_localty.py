# Generated by Django 3.0.2 on 2020-02-02 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20200202_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mycourse',
            name='localty',
        ),
    ]