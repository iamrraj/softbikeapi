from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from clasic.models import ClassicBike
# Create your views here.

# Summnery 
class Dashboard(generics.ListCreateAPIView):
    queryset = ClassicBike.objects.all()[:1]
    serializer_class = DashBoardSerializer

