from rest_framework import serializers
from .. import models


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Delivery
        exclude = ['id', 'timestamp', 'user',]

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
