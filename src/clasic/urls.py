from django.urls import path
from django.contrib import admin

from rest_framework import routers


from .import views

urlpatterns = [
    path('cbike',views.Cbike.as_view()),
    path('cbike/<int:pk>/',views.CbikeDetail.as_view()),

    path('scbike',views.ClassicSummery.as_view()),
    path('dscbike',views.DetailClassicSummery.as_view()),

    path('cdbike',views.Dbike.as_view()),
    path('cdbike/<int:pk>/',views.DbikeDetail.as_view()),
]