# Generated by Django 2.2.2 on 2019-09-25 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clasic', '0005_auto_20190925_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cdetails',
            name='movingtime',
            field=models.FloatField(default=5, help_text='This Field will be in decimal 5.30'),
        ),
        migrations.AlterField(
            model_name='classicbike',
            name='movingtime',
            field=models.FloatField(default=5, help_text='This Field will be in decimal 5.30'),
        ),
    ]
