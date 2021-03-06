"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path as url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from rest_framework_swagger.views import get_swagger_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="SoftBike API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('trips/', include('trips.urls')),

    path('api/1/oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/1/bikes/', include('bikes.api.urls')),
    path('api/1/data/', include('data.api.urls')),

    path('api/1/deliveries/', include('deliveries.api.urls')),

    path('api/1/push/', include('push.api.urls')),

    path('api/1/walk/', include('walk.api.urls')),
    path('api/1/classic/', include('clasic.api.urls')),

    path('api/1/', include('trips.api.urls')),


    path('token-auth/', obtain_jwt_token),
    path('core/', include('login.urls')),

    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger',
                                           cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc',
                                         cache_timeout=0), name='schema-redoc'),
]
