# Generated by Django 2.2.7 on 2020-02-21 20:04

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motor', '0017_auto_20200221_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comparisongeneral',
            name='ID_LIST',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None),
        ),
    ]
