# Generated by Django 2.2.7 on 2020-01-14 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motor', '0008_auto_20200114_0752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisecar',
            name='AudioSystemCar',
        ),
        migrations.RemoveField(
            model_name='advertisecar',
            name='ClimateCar',
        ),
        migrations.RemoveField(
            model_name='advertisecar',
            name='SitDriverCar',
        ),
        migrations.RemoveField(
            model_name='advertisecar',
            name='SitPassrCar',
        ),
        migrations.RemoveField(
            model_name='advertisecar',
            name='WheelCar',
        ),
    ]