# Generated by Django 2.2.2 on 2019-10-08 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('walk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wdetails',
            name='user',
        ),
        migrations.DeleteModel(
            name='Walk',
        ),
        migrations.DeleteModel(
            name='Wdetails',
        ),
    ]
