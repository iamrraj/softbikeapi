from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from . import serializers
from ..models import WorkDay


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
                    "date": obj.date.isoformat(),
                }
                for obj in request.user.workday_set.order_by('date')
            ]})


class DayView(APIView):
    @swagger_auto_schema(
            responses={200: serializers.DaySerializer},
            manual_parameters=[openapi.Parameter('date', 'path', description='Date in ISO format', type='string', format='date')]
        )
    def get(self, request, date):
        day = request.user.workday_set.get(date=date)
        return Response({
            "mileage":day.mileage,
            "electricBikeMileage": day.electric_bike_mileage,
            "weight": day.weight,
            "time": day.time,
            "bikeTime": int(day.bike_time),
            "footTime": int(day.foot_time),
            "co2": int(day.co2),
        })

