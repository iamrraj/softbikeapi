# Generated by Django 2.2.2 on 2019-09-16 13:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassicBike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bikeid', models.CharField(max_length=100)),
                ('milage', models.IntegerField()),
                ('movingtime', models.CharField(max_length=150)),
                ('averagespeed', models.IntegerField()),
                ('kgtrasported', models.IntegerField()),
                ('co2', models.IntegerField()),
                ('additionalbox', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('milage', models.IntegerField()),
                ('movingtime', models.CharField(max_length=150)),
                ('averagespeed', models.IntegerField()),
                ('kgtrasported', models.IntegerField()),
                ('additionalbox', models.IntegerField()),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='clasic.ClassicBike')),
            ],
        ),
    ]