# Generated by Django 2.0 on 2018-09-30 23:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_auto_20180930_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='body',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 30, 23, 29, 24, 861737)),
        ),
    ]
