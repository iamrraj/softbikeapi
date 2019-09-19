from django.urls import path
from . import views


urlpatterns = [
    path('electric/', views.ElectricBikeList.as_view()),
]
