# Generated by Django 3.0.2 on 2020-02-11 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0020_courseinfo_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_icon',
            field=models.ImageField(default='/images/defaultsimage.png', upload_to='images/'),
        ),
    ]
