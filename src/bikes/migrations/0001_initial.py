# Generated by Django 2.2.2 on 2019-09-27 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElectricBike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(help_text='Textual bike identifier', max_length=255, unique=True)),
            ],
            options={
                'ordering': ('label',),
            },
        ),
    ]
