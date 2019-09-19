# Generated by Django 2.2.5 on 2019-09-19 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0001_initial'),
        ('deliveries', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='deliveries',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='weight',
        ),
        migrations.AddField(
            model_name='delivery',
            name='electric_bike',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bikes.ElectricBike'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='letters_number',
            field=models.IntegerField(default=0, help_text='Number of letters'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='delivery',
            name='letters_weight',
            field=models.FloatField(default=0, help_text='Weight of letters, in kg'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='delivery',
            name='packaged_weight',
            field=models.FloatField(default=0, help_text='Weight of packages, in kg'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='delivery',
            name='packages_number',
            field=models.IntegerField(default=0, help_text='Number of packages'),
            preserve_default=False,
        ),
    ]
