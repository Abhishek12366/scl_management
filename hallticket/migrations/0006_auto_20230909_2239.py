# Generated by Django 3.0.5 on 2023-09-09 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hallticket', '0005_student_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='student_name',
        ),
    ]