# Generated by Django 3.0.2 on 2020-01-26 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aurthor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authur',
            name='description',
            field=models.TextField(null=True),
        ),
    ]