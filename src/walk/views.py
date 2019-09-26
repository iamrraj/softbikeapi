from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Walk, Wdetails
from .serializers import *
from rest_framework import generics
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.views import APIView
from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend

# Electric Bike Summery


class WalkSummery(generics.ListCreateAPIView):
    queryset = Walk.objects.all()[:1]
    serializer_class = SummerySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'too': ['lte', 'gte'],
        'fromm': ['lte', 'gte'],
    }

# Electric Bike deails Summery


class DetailWalkSummery(generics.ListCreateAPIView):
    queryset = Walk.objects.all()[:1]
    serializer_class = DSummerySerializer

# Walk Add


class Wbike(generics.ListCreateAPIView):
    queryset = Walk.objects.all()
    serializer_class = WlectricSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'too': ['lte', 'gte'],
        'fromm': ['lte', 'gte'],
    }


class WbikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Walk.objects.all()
    serializer_class = DDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'too': ['lte', 'gte'],
        'fromm': ['lte', 'gte'],
    }

# WAlkDetail Add


class WDbike(generics.ListCreateAPIView):
    queryset = Wdetails.objects.all()
    serializer_class = DetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'too': ['lte', 'gte'],
        'fromm': ['lte', 'gte'],
    }


class WDbikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wdetails.objects.all()
    serializer_class = DetailSerializer


# Create your views here.
