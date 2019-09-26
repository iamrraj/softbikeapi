# Generated by Django 2.2.2 on 2019-09-26 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electric', '0020_auto_20190925_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edetails',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='edetails',
            name='additionalbox',
            field=models.IntegerField(help_text='Additionl box will be in Number'),
        ),
        migrations.AlterField(
            model_name='edetails',
            name='averagespeed',
            field=models.IntegerField(help_text='Average Speed will be in Km'),
        ),
        migrations.AlterField(
            model_name='edetails',
            name='kgtrasported',
            field=models.IntegerField(help_text='Kg Transportd will be in Kg'),
        ),
        migrations.AlterField(
            model_name='edetails',
            name='milage',
            field=models.IntegerField(help_text='Milage will be in Km'),
        ),
        migrations.AlterField(
            model_name='edetails',
            name='movingtime',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='edetails',
            name='user',
            field=models.CharField(help_text='User will be in name', max_length=150),
        ),
    ]
