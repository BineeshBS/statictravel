# Generated by Django 4.1.6 on 2023-02-12 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='images'),
        ),
    ]
