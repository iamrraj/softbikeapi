# Generated by Django 2.2.2 on 2019-09-23 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electric', '0009_auto_20190923_0829'),
    ]

    operations = [
        migrations.AddField(
            model_name='edetails',
            name='frm',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='edetails',
            name='to',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
