# Generated by Django 2.1.2 on 2018-12-11 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Address',
            field=models.TextField(verbose_name='Адрес пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Email',
            field=models.CharField(max_length=30, verbose_name='Емейл пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='FirstName',
            field=models.CharField(max_length=30, verbose_name='Имя пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Gender',
            field=models.CharField(choices=[('М', 'Мужской'), ('Ж', 'Женский')], max_length=1, verbose_name='Пол пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='LastName',
            field=models.CharField(max_length=30, verbose_name='Фамилия пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Login',
            field=models.CharField(max_length=30, verbose_name='Логин пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Phone',
            field=models.CharField(max_length=30, verbose_name='Мобильный телефон пользователя'),
        ),
    ]
