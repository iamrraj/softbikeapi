from django.urls import path
from . import views


urlpatterns = [

    path('', views.Walk.as_view()),
    path('<int:pk>/', views.DWalk.as_view()),

    path('summery/', views.WalkSummery.as_view()),

]
