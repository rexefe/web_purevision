# Generated by Django 3.0.2 on 2020-02-13 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0025_category_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='event',
            field=models.CharField(choices=[('Upcoming', 'Upcoming'), ('Special', 'Special')], default='Upcoming', max_length=20),
        ),
    ]
