from django.urls import path
from . import views


urlpatterns = [
    path('', views.ReceiveData.as_view()),
]
