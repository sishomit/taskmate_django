# Generated by Django 3.0.7 on 2020-07-02 23:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0005_auto_20200703_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='current_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]