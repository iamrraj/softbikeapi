from rest_framework.generics import ListAPIView
from ..models import ElectricBike
from deliveries.models import Delivery
from rest_framework import generics
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from django.db.models import Sum, Avg
from rest_framework.response import Response


# class CustomPagination(PageNumberPagination):
#     def get_paginated_response(self, data):
#         return Response({
#             'next': self.get_next_link(),
#             'previous': self.get_previous_link(),
#             'count': self.page.paginator.count,
#             'total_milage': Delivery.objects.all().aggregate(total_milage=Sum('milage')),
#             'results': data,

#         })

#


class SummeryElectricBikeList(generics.ListCreateAPIView):
    serializer_class = serializers.ElectricBikeSerializerSummery
    queryset = ElectricBike.objects.all()[:1]
    # pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'too': ['lte'],
        'fromm': ['gte']
    }


class ElectricBikeList(generics.ListCreateAPIView):
    serializer_class = serializers.ElectricBikeSerializer
    queryset = ElectricBike.objects.all()
    # pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'too': ['lte'],
        'fromm': ['gte']
    }


class DetailElectricBikeList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.DetialElectricBikeSerializer
    queryset = ElectricBike.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'too': ['lte'],
        'fromm': ['gte'],
    }
