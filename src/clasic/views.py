from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import ClassicBike, Cdetails
from .serializers import *
from rest_framework import generics
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

# Summnery


class ClassicSummery(generics.ListCreateAPIView):
    queryset = ClassicBike.objects.all()[:1]
    serializer_class = SummerySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'too': ['lte'],
        'fromm': ['gte'],
    }


# Summnery
class DetailClassicSummery(generics.ListCreateAPIView):
    queryset = ClassicBike.objects.all()[:1]
    serializer_class = DSummerySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'too': ['lte'],
        'fromm': ['gte'],
    }

# Classic Bike List


class Cbike(generics.ListCreateAPIView):
    queryset = ClassicBike.objects.all()
    serializer_class = ClassicSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'too': ['lte'],
        'fromm': ['gte'],
    }


class CbikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassicBike.objects.all()
    serializer_class = DDetailSerializer


# Classic Bike Detail Add
class Dbike(generics.ListCreateAPIView):
    queryset = Cdetails.objects.all()
    serializer_class = DetailSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = {
    #     'too': ['lte', 'gte'],
    #     'fromm': ['lte', 'gte'],
    # }


class DbikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cdetails.objects.all()
    serializer_class = DetailSerializer
