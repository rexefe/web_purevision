# Generated by Django 3.0.2 on 2020-02-02 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20200202_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycourse',
            name='course_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.CourseInfo'),
        ),
    ]
