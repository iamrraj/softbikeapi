from django.urls import path
from . import views


urlpatterns = [

    path('classic/', views.Classs.as_view()),
    path('classic/<int:pk>/', views.DClasss.as_view()),

    path('classic/summery', views.ClassicSummery.as_view()),




]
