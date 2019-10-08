from rest_framework.generics import CreateAPIView
from rest_framework import generics
from . import serializers
from .filters import ReportFilter
from deliveries.models import Delivery, User
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum, Avg
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.contrib.auth.models import User


class Test(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = serializers.TestSerializer


class DeliveriesView(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = serializers.DeliverySerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'too': ['lte'],
        'fromm': ['gte'],
        'electric_bike': ['exact'],
        'mode': ['exact'],
        'user': ['exact'],
        'timestamp': ['exact'],
    }


class DDeliveriesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = serializers.DeliverySerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'too': ['lte'],
        'fromm': ['gte'],
        'electric_bike': ['exact'],
        'mode': ['exact'],
        'user': ['exact'],
        'timestamp': ['exact'],
    }


class Postman(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.PostmanSerializer
    # filter_backends = [DjangoFilterBackend]
    # filter_fields = {
    #     'too': ['lte'],
    #     'fromm': ['gte'],

    # }


class DPostman(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.DUserSerializer
    filter_backends = [DjangoFilterBackend]
    # filter_fields = {
    #     'too': ['lte'],
    #     'fromm': ['gte'],
    # }


class Userr1(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer1


# This Class Is only Specified for Dasboard
class Dashboard(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()[:1]
    serializer_class = serializers.DashboardSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'too': ['lte'],
        'fromm': ['gte'],
        'electric_bike': ['exact'],
        'mode': ['exact'],
        'user': ['exact'],

    }

# This Class Is only Specified for Dasboard


class Dashboard1(generics.ListCreateAPIView):
    # queryset = Delivery.objects.all()
    serializer_class = serializers.DashboardSerializer1
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'too': ['lte'],
        'fromm': ['gte'],
    }

    def get_queryset(self, *args, **kwargs):
        qs = Delivery.objects.all().distinct()
        # qs = qs.filter(user=self.request.user.id)
        return qs


# class CustomPagination(PageNumberPagination):
#     def get_paginated_response(self, data):
#         return Response({
#             'next': self.get_next_link(),
#             'previous': self.get_previous_link(),
#             'count': self.page.paginator.count,

#             'total_milage': Delivery.objects.filter().aggregate(total_milage=Sum('milage')),
#             'total_co2': Delivery.objects.aggregate(total_co2=Sum('co2')),
#             'total_box': Delivery.objects.aggregate(total_box=Sum('additionalbox')),
#             'total_average': Delivery.objects.aggregate(total_average=Avg('averagespeed')),
#             'total_user': Delivery.objects.aggregate(total_user=sum('nouser')),
#             'total_time': Delivery.objects.aggregate(total_time=Sum('movingtime')),
#             'results': data,

#         })


class ReportView(generics.ListCreateAPIView):
    queryset = Delivery.objects.all().order_by('-user').distinct()
    serializer_class = serializers.ReportSerializer
    # pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReportFilter

    # def get_queryset(self, *args, **kwargs):
    #     qs = Delivery.objects.all().distinct()
    #     # qs = qs.filter(user=self.request.user.id)
    #     return qs
