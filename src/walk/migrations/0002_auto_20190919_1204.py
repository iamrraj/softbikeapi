# Generated by Django 2.2.2 on 2019-09-19 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wdetails',
            name='movingtime',
        ),
        migrations.AddField(
            model_name='walk',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='wdetails',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='walk',
            name='movingtime',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
