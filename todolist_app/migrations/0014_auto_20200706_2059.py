# Generated by Django 3.0.7 on 2020-07-06 14:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0013_auto_20200706_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 14, 59, 31, 235197, tzinfo=utc)),
        ),
    ]