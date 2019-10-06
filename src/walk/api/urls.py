from django.urls import path
from . import views


urlpatterns = [

    path('walk/', views.Walk.as_view()),
    path('walk/<int:pk>/', views.DWalk.as_view()),

    path('walk/summery', views.WalkSummery.as_view()),

]
