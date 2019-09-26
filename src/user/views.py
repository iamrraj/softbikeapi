from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Udetails, Muser
from .serializers import UlectricSerializer, DDetailSerializer, DetailSerializer, DUlectricSerializer, DSummerySerializer

from rest_framework import generics
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.views import APIView
from django.db.models import Sum
from rest_framework import pagination
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend


# Summery Of Index table
class dUbike(generics.ListCreateAPIView):
    queryset = Muser.objects.all()[:1]
    serializer_class = DUlectricSerializer
    filterset_fields = {
        'too': ['lte', 'gte'],
        'fromm': ['lte', 'gte'],
    }

# Summery Of Deatils Table


class DdUbike(generics.ListCreateAPIView):
    queryset = Udetails.objects.all()[:1]
    serializer_class = DSummerySerializer

# Electric Bike Add


class Ubike(generics.ListCreateAPIView):
    queryset = Muser.objects.all()
    serializer_class = UlectricSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'too': ['lte', 'gte'],
        'fromm': ['lte', 'gte'],
    }
    # return_data = {"sum": str(sum([lambda items: int(items['totalweight'])])), "objects": serializer.data}
    # return Response(return_data)


class UbikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Muser.objects.all()
    serializer_class = DDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'too': ['lte', 'gte'],
        'fromm': ['lte', 'gte'],
    }

# Electric Bike Detail Add


class UDbike(generics.ListCreateAPIView):
    queryset = Udetails.objects.all()
    serializer_class = DetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'too': ['lte', 'gte'],
        'fromm': ['lte', 'gte'],
    }


class UDbikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Udetails.objects.all()
    serializer_class = DetailSerializer


# Create your views here.
