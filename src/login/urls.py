from django.urls import path
from .views import current_user, UserList, Logout

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('logout/', Logout.as_view()),
]
