# Generated by Django 2.2.7 on 2020-02-19 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motor', '0012_comparisonfirst_comparisongeneral'),
    ]

    operations = [
        migrations.AddField(
            model_name='comparisongeneral',
            name='ID_User',
            field=models.CharField(default=None, max_length=30, verbose_name='Номер пользователя'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comparisongeneral',
            name='ID_LIST',
            field=models.CharField(max_length=30, verbose_name='Список сравнения объявлений'),
        ),
    ]