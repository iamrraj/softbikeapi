from django.db import models
from django.conf import settings
from datetime import datetime


class ElectricBike(models.Model):
    label = models.CharField(
        max_length=255, unique=True,
        help_text='Textual bike identifier')
    too = models.DateField(default=datetime.now)
    fromm = models.DateField(default=datetime.now)

    class Meta:
        ordering = ('label',)

    def __str__(self):
        return self.label
