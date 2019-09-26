from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('ebike',views.Ebike.as_view()),
    path('ebike/<int:pk>/',views.EbikeDetail.as_view()),

    path('sebike',views.ElectricSummery.as_view()),
    path('dsebike',views.DetailElectricSummery.as_view()),

    path('dbike',views.Dbike.as_view()),
    path('dbike/<int:pk>/',views.DbikeDetail.as_view()),
]
