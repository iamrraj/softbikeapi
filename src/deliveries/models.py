from django.conf import settings
from django.db import models
from electric.models import ElectricBike


class Delivery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    addresses = models.IntegerField(help_text='Number of addresses')
    letters_number = models.IntegerField(help_text='Number of letters')
    letters_weight = models.FloatField(help_text='Weight of letters, in kg')
    packages_number = models.IntegerField(help_text='Number of packages')
    packaged_weight = models.FloatField(help_text='Weight of packages, in kg')

    mode = models.CharField(max_length=64, null=True, blank=True, choices=[('foot', 'foot'), ('bike', 'bike'), ('electric-bike', 'electric-bike')], help_text='Mode of transport')
    electric_bike = models.ForeignKey(ElectricBike, models.PROTECT, null=True, blank=True)

    class Meta:
        ordering = ('timestamp',)

    def __str__(self):
        return str(self.timestamp)
