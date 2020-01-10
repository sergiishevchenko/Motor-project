# Generated by Django 2.2.7 on 2020-01-10 16:52

from django.db import migrations, models
import motor.models


class Migration(migrations.Migration):

    dependencies = [
        ('motor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertiseCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameCar', models.CharField(max_length=15, verbose_name='Марка автомобиля')),
                ('SeriaCar', models.CharField(max_length=25, verbose_name='Серия автомобиля')),
                ('YearCar', models.CharField(max_length=15, verbose_name='Год выпуска автомобиля')),
                ('KuzovCar', models.CharField(max_length=25, verbose_name='Кузов автомобиля')),
                ('GenerationCar', models.CharField(max_length=30, verbose_name='Поколение автомобиля')),
                ('GearCar', models.CharField(max_length=15, verbose_name='Коробка автомобиля')),
                ('DriveCar', models.CharField(max_length=25, verbose_name='Привод автомобиля')),
                ('MotorCar', models.CharField(max_length=25, verbose_name='Двигатель автомобиля')),
                ('ModificationCar', models.CharField(max_length=35, verbose_name='Модификация автомобиля')),
                ('ColorCar', models.CharField(max_length=15, verbose_name='Название автомобиля')),
                ('ImageCar', models.ImageField(blank=True, null=True, upload_to=motor.models.get_image_path)),
                ('MediaCar', models.CharField(max_length=25, verbose_name='Мультмедиа автомобиля')),
                ('ComfortCar', models.CharField(max_length=25, verbose_name='Комфорт автомобиля')),
                ('BuyYearCar', models.CharField(max_length=25, verbose_name='Год покупки автомобиля')),
                ('BuyMonthCar', models.CharField(max_length=25, verbose_name='Месяц покупки автомобиля')),
                ('RunCar', models.CharField(max_length=25, verbose_name='Пробег автомобиля')),
                ('PriceCar', models.CharField(max_length=25, verbose_name='Цена автомобиля')),
                ('OwnerCar', models.CharField(max_length=25, verbose_name='Владелец автомобиля')),
                ('DopCar', models.CharField(max_length=25, verbose_name='Дополнительное описание автомобиля')),
            ],
            options={
                'verbose_name_plural': 'Объявления',
            },
        ),
    ]
