from rest_framework.generics import ListAPIView
from ..models import ElectricBike
from . import serializers


class ElectricBikeList(ListAPIView):
    serializer_class = serializers.ElectricBikeSerializer
    queryset = ElectricBike.objects.all()

