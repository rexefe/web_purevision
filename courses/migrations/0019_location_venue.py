# Generated by Django 3.0.2 on 2020-02-04 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_remove_location_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='venue',
            field=models.CharField(default='The Default Venue', max_length=150),
        ),
    ]
