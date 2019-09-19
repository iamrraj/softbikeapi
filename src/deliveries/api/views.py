from rest_framework.generics import CreateAPIView
from . import serializers


class DeliveriesView(CreateAPIView):
    serializer_class = serializers.DeliverySerializer

