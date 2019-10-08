from django.db import models
from django.conf import settings
from bikes.models import ElectricBike
from datetime import datetime


class User(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    too = models.DateField(default=datetime.now)
    fromm = models.DateField(default=datetime.now)

    class Meta:
        ordering = ('user',)

    def __str__(self):
        return str(self.user)


class Delivery(models.Model):
    user = models.ForeignKey(
        User, related_name='detail', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    milage = models.IntegerField(
        help_text="Milage Will be in Km/hr", default=10)
    movingtime = models.FloatField(
        help_text="Milage Will be in 5.30hr", default=10)
    averagespeed = models.IntegerField(
        help_text="Average Speed Will be in km/hr", default=10)
    letteritems = models.IntegerField(
        default=10, help_text="This field Will be in digit")
    shipweight = models.IntegerField(
        default=10, help_text="This field Will be in kgs")
    package = models.IntegerField(
        default=10, help_text="This field Will be in digit")
    kgtrasported = models.IntegerField(
        help_text="Kg Transported will be in Kg", default=10)
    co2 = models.IntegerField(help_text="Co2 will be in mg ", default=10)
    additionalbox = models.IntegerField(
        help_text="Additional Boxes will be in Number ", default=10)
    nouser = models.IntegerField(
        help_text="No Of User will be in integer", default=10)
    addresses = models.IntegerField(
        help_text="No Of address", default=1)
    letters_number = models.IntegerField(
        help_text="No Of address", default=1)
    letters_weight = models.FloatField(
        help_text="Kg Transported will be in Kg", default=10)
    packages_number = models.IntegerField(
        help_text="No Of address", default=1)
    packaged_weight = models.FloatField(
        help_text="Kg Transported will be in Kg", default=10)
    mode = models.CharField(max_length=64, null=True, blank=True, choices=[(
        'foot', 'foot'), ('bike', 'bike'), ('electric-bike', 'electric-bike')], help_text='Mode of transport')
    electric_bike = models.ForeignKey(
        ElectricBike, models.PROTECT, null=True, related_name='results', blank=True)
    too = models.DateField(default=datetime.now)
    fromm = models.DateField(default=datetime.now)

    class Meta:
        ordering = ('timestamp',)

    def __str__(self):
        return str(self.timestamp)

    @property
    def electric_detail(self):
        return self.items.all().order_by('-date')

# Create your models here.
