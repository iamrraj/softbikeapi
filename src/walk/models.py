from django.db import models
from datetime import datetime
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Walk(models.Model):
    username = models.CharField(max_length=150)
    milage = models.IntegerField(help_text="Milage will be in Km")
    movingtime = models.FloatField(help_text="moving time will be in decimal")
    letteritems = models.IntegerField(
        default=10, help_text="This field Will be in digit")
    shipweight = models.IntegerField(
        default=10, help_text="This field Will be in kgs")
    package = models.IntegerField(
        default=10, help_text="This field Will be in digit")
    kgtransported = models.IntegerField(
        help_text="Kg Transportd will be in Kg")
    additionalbox = models.IntegerField(
        help_text="Average Speed will be in Km")
    too = models.DateField(default=datetime.now)
    fromm = models.DateField(default=datetime.now)

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username


class Wdetails(models.Model):
    user = models.ForeignKey(Walk, related_name='items',
                             on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    milage = models.IntegerField(help_text="Milage will be in Km")
    movingtime = models.FloatField(help_text="moving time will be in decimal")

    letteritems = models.IntegerField(
        default=10, help_text="This field Will be in digit")
    shipweight = models.IntegerField(
        default=10, help_text="This field Will be in kgs")
    package = models.IntegerField(
        default=10, help_text="This field Will be in digit")
    kgtransported = models.IntegerField(
        help_text="Kg Transportd will be in Kg")
    additionalbox = models.IntegerField(
        help_text="Average Speed will be in Km")
    too = models.DateField(default=datetime.now)
    fromm = models.DateField(default=datetime.now)

    def __unicode__(self):
        return self.date

    @property
    def electric_detail(self):
        return self.items.all().order_by('-date')
