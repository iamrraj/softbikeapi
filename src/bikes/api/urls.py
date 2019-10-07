from django.urls import path
from . import views


urlpatterns = [
    path('electric/', views.ElectricBikeList.as_view()),
    path('electric/<int:pk>/', views.DetailElectricBikeList.as_view()),

    path('electric/summery/', views.SummeryElectricBikeList.as_view()),
    # path('walk/summery/', views.SummeryWalkBikeList.as_view()),
]
