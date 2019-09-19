from rest_framework import serializers
from .. import models


class ElectricBikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ElectricBike
        fields = ['id', 'label']
