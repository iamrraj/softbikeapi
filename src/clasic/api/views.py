from rest_framework.generics import CreateAPIView
from rest_framework import generics
from . import serializers
from deliveries.models import Delivery, User

from django_filters.rest_framework import DjangoFilterBackend

# This Class Is only Specified for Classic Bike


class Classs(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ClassSerializer
    # filter_backends = [DjangoFilterBackend]
    # filter_fields = {
    #     'too': ['lte'],
    #     'fromm': ['gte'],

    # }

# This Class Is only Specified for Classic Bike


class DClasss(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.DetailClassSerializer
    # filter_backends = [DjangoFilterBackend]
    # filter_fields = {
    #     'too': ['lte'],
    #     'fromm': ['gte'],

    # }


class ClassicSummery(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()[:1]
    serializer_class = serializers.ClassicSummery
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'too': ['lte'],
        'fromm': ['gte'],
        'electric_bike': ['exact'],
        'mode': ['exact'],
        'user': ['exact'],
        'timestamp': ['exact'],
    }
