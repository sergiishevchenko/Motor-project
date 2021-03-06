# Generated by Django 2.2.7 on 2020-02-06 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motor', '0007_auto_20200203_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kuzov', models.CharField(max_length=30, verbose_name='Целостность кузова')),
                ('cover', models.CharField(max_length=30, verbose_name='Лакокрасочное покрытие')),
                ('salon', models.CharField(max_length=30, verbose_name='Салон и интерьер')),
                ('exterer', models.CharField(max_length=30, verbose_name='+1 пункт по экстерьеру')),
                ('electro', models.CharField(max_length=30, verbose_name='Электрооборудование')),
                ('hod', models.CharField(max_length=30, verbose_name='Ходовая часть')),
                ('motor', models.CharField(max_length=30, verbose_name='Двигатель')),
                ('gearbox', models.CharField(max_length=30, verbose_name='Коробка передач')),
                ('ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motor.User')),
            ],
            options={
                'verbose_name_plural': 'Голосование',
            },
        ),
    ]
