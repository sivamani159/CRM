# Generated by Django 4.1.7 on 2023-05-17 05:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_courses_description_courses_keyfeatures'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be 10 digits without any special characters.', regex='^\\d{10}$')])),
                ('course', models.CharField(max_length=40)),
            ],
        ),
    ]
