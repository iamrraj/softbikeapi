from django.urls import path
from . import views


urlpatterns = [
    path('data/', views.DeliveriesView.as_view()),
    path('data/<int:pk>/', views.DDeliveriesView.as_view()),

    path('postman/', views.Postman.as_view()),
    path('postman/<int:pk>/', views.DPostman.as_view()),


    path('dashboard/', views.Dashboard.as_view()),
    path('dashboard1/', views.Dashboard1.as_view()),

    path('report/', views.ReportView.as_view()),
    path('user1/', views.Userr1.as_view()),


]
