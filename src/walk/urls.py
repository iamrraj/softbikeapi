from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('walk',views.Wbike.as_view()),
    path('walk/<int:pk>/',views.WbikeDetail.as_view(), name='Edetail'),

    path('swalk',views.WalkSummery.as_view()),
    path('dswalk',views.DetailWalkSummery.as_view()),

    path('dwalk',views.WDbike.as_view()),
    path('dwalk/<int:pk>/',views.WDbikeDetail.as_view()),
]