# Generated by Django 2.2.2 on 2019-09-19 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electric', '0003_auto_20190919_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edetails',
            name='movingtime',
            field=models.CharField(default='3h 13min', max_length=150),
        ),
        migrations.AlterField(
            model_name='edetails',
            name='user',
            field=models.CharField(max_length=150),
        ),
    ]
