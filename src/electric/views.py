from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Edetails, ElectricBike
from .serializers import *
from rest_framework import generics
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.db.models import Sum, Avg


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            # # 'total_co22': Electricbike.objects.annotate(mileage=Sum('co2')).values_list('co2', flat=True),
            # 'items': ElectricBike.objects.all().annotate(Sum('milage')).values_list('milage', flat=True),
            'total_milage': ElectricBike.objects.all().aggregate(total_milage=Sum('milage')),
            'total_co2': ElectricBike.objects.aggregate(total_co2=Sum('co2')),
            'total_box': ElectricBike.objects.aggregate(total_box=Sum('additionalbox')),
            'total_average': ElectricBike.objects.aggregate(total_average=Avg('averagespeed')),
            'total_user': ElectricBike.objects.aggregate(total_user=Avg('nouser')),
            'total_time': ElectricBike.objects.aggregate(total_time=Sum('movingtime')),
            'results': data,

        })

# Summnery


class ElectricSummery(generics.ListCreateAPIView):
    queryset = ElectricBike.objects.all()[:1]
    serializer_class = SummerySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'too': ['lte'],
        'fromm': ['gte'],
    }


# Detail Summnery
class DetailElectricSummery(generics.ListCreateAPIView):
    queryset = ElectricBike.objects.all()[:1]
    serializer_class = DSummerySerializer

# Electric Bike Add


class Ebike(generics.ListCreateAPIView):
    queryset = ElectricBike.objects.all()
    serializer_class = ElectricSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'too': ['lte'],
        'fromm': ['gte'],
    }


class EbikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ElectricBike.objects.all()
    serializer_class = DDetailSerializer

# Electric Bike Detail Add


class Dbike(generics.ListCreateAPIView):
    queryset = Edetails.objects.all()
    serializer_class = DetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'too': ['lte'],
        'fromm': ['gte'],
    }


class DbikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Edetails.objects.all()
    serializer_class = DetailSerializer
