# Generated by Django 3.0.5 on 2023-09-12 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20230912_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
    ]
