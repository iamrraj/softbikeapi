# Generated by Django 2.2.2 on 2019-10-08 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0003_auto_20191007_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]