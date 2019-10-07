# Generated by Django 2.2.2 on 2019-09-25 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electric', '0015_auto_20190923_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='edetails',
            name='co2',
            field=models.IntegerField(default=160, help_text='Co2 will be in mg '),
        ),
        migrations.AddField(
            model_name='edetails',
            name='letteritems',
            field=models.IntegerField(default=10, help_text='This field Will be in digit'),
        ),
        migrations.AddField(
            model_name='edetails',
            name='package',
            field=models.IntegerField(default=10, help_text='This field Will be in digit'),
        ),
        migrations.AddField(
            model_name='edetails',
            name='shipweight',
            field=models.IntegerField(default=10, help_text='This field Will be in kgs'),
        ),
        migrations.AddField(
            model_name='electricbike',
            name='letteritems',
            field=models.IntegerField(default=10, help_text='This field Will be in digit'),
        ),
        migrations.AddField(
            model_name='electricbike',
            name='package',
            field=models.IntegerField(default=10, help_text='This field Will be in digit'),
        ),
        migrations.AddField(
            model_name='electricbike',
            name='shipweight',
            field=models.IntegerField(default=10, help_text='This field Will be in kgs'),
        ),
        migrations.AlterField(
            model_name='electricbike',
            name='movingtime',
            field=models.FloatField(default=5.3, help_text='This Field will be in decimal 5.30'),
        ),
    ]