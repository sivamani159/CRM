# Generated by Django 4.1.7 on 2023-05-15 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
