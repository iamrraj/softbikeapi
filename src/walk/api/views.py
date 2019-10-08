from rest_framework.generics import CreateAPIView
from rest_framework import generics
from . import serializers
from deliveries.models import Delivery, User

from django_filters.rest_framework import DjangoFilterBackend


# This Class Is only Specified for Walk
class Walk(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.WalkSerializer
    # filter_backends = [DjangoFilterBackend]
    # filter_fields = {
    #     'too': ['lte'],
    #     'fromm': ['gte'],
    # }

# This Class Is only Specified for Walk


class DWalk(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.WalkDetailSerializer
    # filter_backends = [DjangoFilterBackend]
    # filter_fields = {
    #     'too': ['lte'],
    #     'fromm': ['gte'],
    # }

# This Class Is only Specified for Dasboard


class WalkSummery(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()[:1]
    serializer_class = serializers.WalkSummerySerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'too': ['lte'],
        'fromm': ['gte'],
        'electric_bike': ['exact'],
        'mode': ['exact'],
        'user': ['exact'],
        'timestamp': ['exact'],
    }
