# Generated by Django 3.0.2 on 2020-01-25 11:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20200125_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 25, 17, 21, 11, 718797)),
        ),
    ]
