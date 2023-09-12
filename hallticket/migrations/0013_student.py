# Generated by Django 3.0.5 on 2023-09-11 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hallticket', '0012_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('aadhaar_number', models.CharField(max_length=12)),
                ('program', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('enrollment_number', models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]
