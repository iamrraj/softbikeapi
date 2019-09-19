from django.urls import path
from . import views


urlpatterns = [
    path('', views.DeliveriesView.as_view()),
]
