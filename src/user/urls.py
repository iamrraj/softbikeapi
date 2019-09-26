from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('user',views.Ubike.as_view()),
    path('user/<int:pk>/',views.UbikeDetail.as_view()),

    path('sduser',views.dUbike.as_view() ),
    path('sdetails',views.DdUbike.as_view() ),

    path('duser',views.UDbike.as_view()),
    path('duser/<int:pk>/',views.UDbikeDetail.as_view()),
]
