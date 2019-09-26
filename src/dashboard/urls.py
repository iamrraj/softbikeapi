from django.urls import path
from django.contrib import admin

from rest_framework import routers

from . import views

urlpatterns = [
    path('',views.Dashboard.as_view())
]
