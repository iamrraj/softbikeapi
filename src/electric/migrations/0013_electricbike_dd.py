# Generated by Django 2.2.2 on 2019-09-23 08:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electric', '0012_auto_20190923_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='electricbike',
            name='dd',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
