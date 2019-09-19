from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from . import serializers


class MeView(APIView):
    @swagger_auto_schema(responses={200: serializers.UserSerializer})
    def get(self, request):
        return Response({
            #"first_name": request.user.first_name,
            #"last_name": request.user.last_name,
            "name": "%s %s" % (request.user.first_name, request.user.last_name),
        })



class DaysView(APIView):
    @swagger_auto_schema(responses={200: serializers.DaysSerializer})
    def get(self, request):
        return Response({
            "days": [
                {
                    "date": "2019-09-15",
                },
                {
                    "date": "2019-09-16",
                },
            ]})


class DayView(APIView):
    @swagger_auto_schema(
            responses={200: serializers.DaySerializer},
            manual_parameters=[openapi.Parameter('date', 'path', description='Date in ISO format', type='string', format='date')]
        )
    def get(self, request, date):
        return Response({
            "mileage": 1234.56,
            "time": 123456,
            "bikeTime": 123000,
            "footTime": 456,
            "co2": 234,
        })

