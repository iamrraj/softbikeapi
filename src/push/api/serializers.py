from rest_framework import serializers
from .. import models


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PushToken
        fields = ['token',]

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
