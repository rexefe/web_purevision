# Generated by Django 3.0.2 on 2020-02-11 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('provison_users', '0010_participant'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='provison_users.Profile'),
        ),
    ]