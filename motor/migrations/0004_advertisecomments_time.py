# Generated by Django 2.2.7 on 2020-01-29 10:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('motor', '0003_advertisecomments'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisecomments',
            name='Time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]