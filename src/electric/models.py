from django.db import models
from datetime import datetime
from tinymce.models import HTMLField
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class ElectricBike(models.Model):
    id = models.AutoField(primary_key=True)
    bikeid = models.CharField(
        max_length=100, help_text="Bike id will be String")
    milage = models.IntegerField(help_text="Milage Will be in Km/hr")
    movingtime = models.FloatField(default=10)
    averagespeed = models.IntegerField(
        help_text="Average Speed Will be in km/hr")
    letteritems = models.IntegerField(
        default=10, help_text="This field Will be in digit")
    shipweight = models.IntegerField(
        default=10, help_text="This field Will be in kgs")
    package = models.IntegerField(
        default=10, help_text="This field Will be in digit")
    kgtrasported = models.IntegerField(
        help_text="Kg Transported will be in Kg")
    co2 = models.IntegerField(help_text="Co2 will be in mg ")
    additionalbox = models.IntegerField(
        help_text="Additional Boxes will be in Number ")
    nouser = models.IntegerField(help_text="No Of User will be in integer")
    too = models.DateField(default=datetime.now)

    fromm = models.DateField(default=datetime.now)

    def __unicode__(self):
        return self.bikeid

    def __str__(self):
        return self.bikeid


class Edetails(models.Model):
    id = models.AutoField(primary_key=True)
    bike = models.ForeignKey(
        ElectricBike, related_name='items', on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    user = models.CharField(max_length=150,help_text="User will be in name")
    milage = models.IntegerField(help_text="Milage will be in Km")
    movingtime = models.FloatField()
    averagespeed = models.IntegerField(help_text="Average Speed will be in Km")
    letteritems = models.IntegerField(
        default=10, help_text="This field Will be in digit")
    shipweight = models.IntegerField(
        default=10, help_text="This field Will be in kgs")
    package = models.IntegerField(
        default=10, help_text="This field Will be in digit")
    kgtrasported = models.IntegerField(help_text="Kg Transportd will be in Kg")
    additionalbox = models.IntegerField(help_text='Additionl box will be in Number')
    co2 = models.IntegerField(default=160, help_text="Co2 will be in mg ")
    too = models.DateField(default=datetime.now)
    fromm = models.DateField(default=datetime.now)

    def __unicode__(self):
        return self.date

    @property
    def electric_detail(self):
        return self.items.all().order_by('-date')
