from django.db import models
from datetime import datetime
# from tinymce.models import HTMLField
from django.utils import timezone
from django.urls import reverse


class ClassicBike(models.Model):
    bikeid = models.CharField(
        max_length=100, help_text="Bike id will be in String")
    milage = models.IntegerField(help_text="Milage will be in Km")
    movingtime = models.FloatField(help_text="moving time will be in decimal")
    letteritems = models.IntegerField(
        default=10, help_text="This field Will be in digit")
    shipweight = models.IntegerField(
        default=10, help_text="This field Will be in kgs")
    package = models.IntegerField(
        default=10, help_text="This field Will be in digit")
    averagespeed = models.IntegerField(help_text="Average Speed will be in Km")
    kgtrasported = models.IntegerField(help_text="Kg Transportd will be in Kg")
    co2 = models.IntegerField(help_text='CO2 saved, in mg')
    additionalbox = models.IntegerField(
        help_text='Additionl box will be in Number')
    too = models.DateField(default=datetime.now)
    fromm = models.DateField(default=datetime.now)

    def __unicode__(self):
        return self.bikeid

    def __str__(self):
        return self.bikeid


class Cdetails(models.Model):
    bike = models.ForeignKey(
        ClassicBike, related_name='items', on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    milage = models.IntegerField(help_text="Milage will be in Km")
    movingtime = models.FloatField(help_text="moving time will be in decimal")
    letteritems = models.IntegerField(
        default=10, help_text="This field Will be in digit")
    shipweight = models.IntegerField(
        default=10, help_text="This field Will be in kgs")
    package = models.IntegerField(
        default=10, help_text="This field Will be in digit")
    averagespeed = models.IntegerField(help_text="Average Speed will be in Km")
    kgtrasported = models.IntegerField(help_text="Kg Transportd will be in Kg")
    additionalbox = models.IntegerField(
        help_text='Additionl box will be in Number')
    too = models.DateField(default=datetime.now)
    fromm = models.DateField(default=datetime.now)

    def __unicode__(self):
        return self.date

    @property
    def electric_detail(self):
        return self.items.all().order_by('-date')
