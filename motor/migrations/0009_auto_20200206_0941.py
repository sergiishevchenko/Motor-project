# Generated by Django 2.2.7 on 2020-02-06 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motor', '0008_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='ID',
            field=models.CharField(max_length=30, verbose_name='Номер объявления'),
        ),
    ]
