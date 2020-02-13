# Generated by Django 3.0.2 on 2020-01-26 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webinars', '0002_webinar_youtube_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='webinar',
            name='webinar_type',
            field=models.CharField(choices=[('free', 'Free'), ('paid', 'Paid')], default='free', max_length=6, null=True),
        ),
    ]
