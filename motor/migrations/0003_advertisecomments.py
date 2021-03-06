# Generated by Django 2.2.7 on 2020-01-29 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motor', '0002_advertisecar'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertiseComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30, verbose_name='Имя пользователя')),
                ('Email', models.CharField(max_length=30, unique=True, verbose_name='Емейл пользователя')),
                ('Comment', models.CharField(max_length=30, verbose_name='Комментарий пользователя')),
                ('ID_Advertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motor.AdvertiseCar')),
                ('ID_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motor.User')),
            ],
            options={
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
