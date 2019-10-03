from rest_framework import serializers


class DaysDaySerializer(serializers.Serializer):
    date = serializers.DateField()


class DaysSerializer(serializers.Serializer):
    days = DaysDaySerializer(many=True)


class DaySerializer(serializers.Serializer):
    mileage = serializers.FloatField(help_text='Total mileage in km')
    electricBikeMileage = serializers.FloatField(help_text='Electric bike mileage in km')
    weight = serializers.FloatField(help_text='Total weight in kg')

    time = serializers.IntegerField(help_text='Total work time, in seconds')
    bikeTime = serializers.IntegerField(help_text='Total bike time, in seconds')
    footTime = serializers.IntegerField(help_text='Total on foot time, in seconds')
    co2 = serializers.IntegerField(help_text='CO2 saved, in mg')


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(help_text='Preferred user display name')
