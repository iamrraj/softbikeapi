# Generated by Django 2.2.2 on 2019-09-25 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clasic', '0006_auto_20190925_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cdetails',
            name='movingtime',
            field=models.DecimalField(blank=True, decimal_places=1, default=10, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='classicbike',
            name='movingtime',
            field=models.DecimalField(blank=True, decimal_places=1, default=10, max_digits=3, null=True),
        ),
    ]