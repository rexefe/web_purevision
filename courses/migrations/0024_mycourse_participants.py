# Generated by Django 3.0.2 on 2020-02-11 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provison_users', '0010_participant'),
        ('courses', '0023_auto_20200212_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycourse',
            name='participants',
            field=models.ManyToManyField(null=True, to='provison_users.Participant'),
        ),
    ]