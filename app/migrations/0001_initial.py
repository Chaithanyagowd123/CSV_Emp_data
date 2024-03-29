# Generated by Django 4.2.7 on 2024-02-15 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business_Employment_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series_reference', models.CharField(max_length=100)),
                ('period', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_value', models.DecimalField(decimal_places=6, max_digits=10)),
                ('suppressed', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('units', models.CharField(max_length=100)),
                ('magnitude', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('group', models.CharField(max_length=100)),
                ('series_title_1', models.CharField(max_length=100)),
                ('series_title_2', models.CharField(max_length=100)),
                ('series_title_3', models.CharField(max_length=100)),
                ('series_title_4', models.CharField(max_length=100)),
                ('series_title_5', models.CharField(max_length=100)),
            ],
        ),
    ]
