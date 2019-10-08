from django.urls import path
from . import views


urlpatterns = [

    path('', views.Classs.as_view()),
    path('<int:pk>/', views.DClasss.as_view()),

    path('summery/', views.ClassicSummery.as_view()),




]
