from django.db import models
from datetime import datetime
# from tinymce.models import HTMLField
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Muser(models.Model):
    user = models.CharField(max_length=150, help_text="User will be in name")
    trwalk = models.IntegerField(help_text="travel by walk will be in KM")
    Dtwalk = models.IntegerField(help_text="Distributed by walk will be in KG")
    trclassic = models.IntegerField(
        help_text="travel by classic will be in KM")
    Dtclassic = models.IntegerField(
        help_text="Distributed by classic will be in KG")
    trelectric = models.IntegerField(
        help_text="travel by electric will be in KM")
    Dtelectric = models.IntegerField(
        help_text="Distributed by electric will be in KG")
    totalMilage = models.IntegerField(help_text="Total Milage  will be in KM")
    totalweight = models.IntegerField(help_text="Total weight  will be in KG")
    phone = models.CharField(
        max_length=20, help_text="phone will be in phone number format")
    too = models.DateField(default=datetime.now)
    fromm = models.DateField(default=datetime.now)

    def __unicode__(self):
        return self.user

    def __str__(self):
        return self.user


class Udetails(models.Model):
    TRAVEL_TYPE = (
        ('ELECTRIC BIKE', 'Electric Bike'),
        ('CLASSIC BIKE', 'Clasic Bike'),
        ('WALK', 'Walk'),
    )

    user = models.ForeignKey(
        Muser, related_name='items', on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    dstrtype = models.CharField(max_length=150,choices=TRAVEL_TYPE, help_text="Select from box")
    milage = models.IntegerField(help_text="Milage will be in Km")
    movingtime = models.FloatField(help_text="moving time will be in decimal")
    kgtransported = models.IntegerField(default=14,help_text="Kg Transportd will be in Kg")
    additionalbox = models.IntegerField(help_text='Additionl box will be in Number')
    too = models.DateField(default=datetime.now)
    fromm = models.DateField(default=datetime.now)

    def __unicode__(self):
        return self.date

    @property
    def electric_detail(self):
        return self.items.all().order_by('-date')
