from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.MeView.as_view()), #name
    path('days/', views.DaysView.as_view()), # dates by month # do we need paging?
    path('days/<date>/', views.DayView.as_view()), # km, time, bike time, foot time, co2
]
