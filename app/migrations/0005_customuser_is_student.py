# Generated by Django 3.0.5 on 2023-09-07 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_customuser_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
    ]
