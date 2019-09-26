from django.db import models
from electric.models import ElectricBike
from clasic.models import ClassicBike
from walk.models import Walk
from user.models import Muser
from datetime import datetime
# Create your models here.

class Report(models.Model):
    name = models.CharField(max_length=150, default="Electric  Bike Report")
    electric = models.ForeignKey(ElectricBike, related_name="electric",on_delete=models.CASCADE,help_text="Electric Bike id" )
    classic = models.ForeignKey(ClassicBike, related_name="classic",on_delete=models.CASCADE,help_text="Classic Bike id")
    walk = models.ForeignKey(Walk, related_name="walk",on_delete=models.CASCADE,help_text="Walk id")
    user = models.ForeignKey(Muser, related_name="muser",on_delete=models.CASCADE,help_text="user from Username id")
    too = models.DateField(default=datetime.now)
    fromm = models.DateField(default=datetime.now)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


