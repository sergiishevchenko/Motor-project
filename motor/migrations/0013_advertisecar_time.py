# Generated by Django 2.2.7 on 2020-01-17 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motor', '0012_remove_advertisecar_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisecar',
            name='Time',
            field=models.CharField(default=None, max_length=55, verbose_name='Дата добавления объявления'),
            preserve_default=False,
        ),
    ]