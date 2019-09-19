from django.urls import path
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User


urlpatterns = [
    path('', ListView.as_view(model=User)),
    path('<int:pk>/', DetailView.as_view(model=User), name='user_trip'),
]
