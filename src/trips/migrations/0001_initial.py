# Generated by Django 2.2.5 on 2019-09-30 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('mileage', models.FloatField(default=0)),
                ('electric_bike_mileage', models.FloatField(default=0)),
                ('bike_mileage', models.FloatField(default=0)),
                ('foot_mileage', models.FloatField(default=0)),
                ('weight', models.FloatField(default=0)),
                ('time', models.FloatField(default=0)),
                ('electric_bike_time', models.FloatField(default=0)),
                ('bike_time', models.FloatField(default=0)),
                ('foot_time', models.FloatField(default=0)),
                ('co2', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]