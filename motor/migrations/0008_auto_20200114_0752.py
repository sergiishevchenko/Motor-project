# Generated by Django 2.2.7 on 2020-01-14 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motor', '0007_auto_20200113_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisecar',
            name='AudioSystemCar',
            field=models.CharField(default=None, max_length=55, verbose_name='Аудиосистема'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisecar',
            name='ClimateCar',
            field=models.CharField(default=None, max_length=55, verbose_name='Климат'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisecar',
            name='SitDriverCar',
            field=models.CharField(default=None, max_length=55, verbose_name='Сиденье водителя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisecar',
            name='SitPassrCar',
            field=models.CharField(default=None, max_length=55, verbose_name='Сиденье пассажира'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisecar',
            name='WheelCar',
            field=models.CharField(default=None, max_length=55, verbose_name='Регулировка руля'),
            preserve_default=False,
        ),
    ]
