# Generated by Django 2.2.7 on 2020-02-06 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motor', '0010_auto_20200206_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratings',
            name='ID_average',
        ),
    ]
