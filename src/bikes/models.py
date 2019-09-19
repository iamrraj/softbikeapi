from django.db import models


class ElectricBike(models.Model):
    label = models.CharField(
            max_length=255, unique=True,
            help_text='Textual bike identifier')

    class Meta:
        ordering = ('label',)

    def __str__(self):
        return self.label
