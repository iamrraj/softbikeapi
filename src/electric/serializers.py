from rest_framework import serializers
from .models import Edetails,ElectricBike
from rest_framework_jwt.settings import api_settings
from django.db.models import Sum,Avg,Max,Min,Count,F,Q
from django.db.models import Func

class ElectricSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectricBike
        fields = ('pk','bikeid','milage','movingtime','averagespeed','kgtrasported','co2','additionalbox','nouser','too','fromm','letteritems','shipweight','package')

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edetails
        fields = '__all__'

class DDetailSerializer(serializers.ModelSerializer):
    items = DetailSerializer(many=True, read_only=True)
    class Meta:
        model = ElectricBike
        fields = ('pk','bikeid','milage','movingtime','averagespeed','kgtrasported','co2','additionalbox','nouser','too','fromm','letteritems','shipweight','package','items')


class Round(Func):
    function = 'ROUND'
    template='%(function)s(%(expressions)s, 2)'

class SummerySerializer(serializers.ModelSerializer):
    total_milage = serializers.SerializerMethodField()
    total_movingtime = serializers.SerializerMethodField()
    total_averagespeed = serializers.SerializerMethodField()
    total_kg = serializers.SerializerMethodField()
    total_co2_save = serializers.SerializerMethodField()
    total_boxes = serializers.SerializerMethodField()
    total_user = serializers.SerializerMethodField()
    total_letter = serializers.SerializerMethodField()
    total_ship_weight = serializers.SerializerMethodField()
    total_pack = serializers.SerializerMethodField()
    class Meta:
        model = ElectricBike
        fields=('too','total_milage','total_movingtime','total_averagespeed','total_kg','total_co2_save','total_boxes','total_user','total_letter','total_ship_weight','total_pack')
        extra_kwargs = {
            'total_averagespeed': {'max_digits': 16, 'decimal_places': 2}
        }

    def get_total_letter(self, obj):
        totalpieces = ElectricBike.objects.all().aggregate(total_letter=Sum('letteritems'))
        return totalpieces["total_letter"]

    def get_total_ship_weight(self, obj):
        totalpieces = ElectricBike.objects.all().aggregate(total_ship_weight=Sum('shipweight'))
        return totalpieces["total_ship_weight"]

    def get_total_pack(self, obj):
        totalpieces = ElectricBike.objects.all().aggregate(total_pack=Sum('package'))
        return totalpieces["total_pack"]


    def get_total_milage(self, obj):
        totalpieces = ElectricBike.objects.all().aggregate(total_milage=Sum('milage'))
        return totalpieces["total_milage"]
    
    def get_total_movingtime(self, obj):
        totalpieces = ElectricBike.objects.all().aggregate(total_movingtime=Sum('movingtime'))
        return totalpieces["total_movingtime"]
    
    def get_total_averagespeed(self, obj):
        totalpieces = ElectricBike.objects.all().aggregate(total_averagespeed=Round(Avg('averagespeed')))
        return totalpieces["total_averagespeed"]

    def get_total_kg(self, obj):
        totalpieces = ElectricBike.objects.all().aggregate(total_kg=Sum('kgtrasported'))
        return totalpieces["total_kg"]
    
    def get_total_co2_save(self, obj):
        totalpieces = ElectricBike.objects.all().aggregate(total_co2_save=Sum('co2'))
        return totalpieces["total_co2_save"]
    
    def get_total_boxes(self, obj):
        totalpieces = ElectricBike.objects.all().aggregate(total_boxes=Sum('additionalbox'))
        return totalpieces["total_boxes"]

    def get_total_user(self, obj):
        totalpieces = ElectricBike.objects.all().aggregate(total_user=Sum('nouser'))
        return totalpieces["total_user"]



class DSummerySerializer(serializers.ModelSerializer):
    total_milage = serializers.SerializerMethodField()
    total_movingtime = serializers.SerializerMethodField()
    total_averagespeed = serializers.SerializerMethodField()
    total_kg = serializers.SerializerMethodField()
    total_boxes = serializers.SerializerMethodField()
    total_letter = serializers.SerializerMethodField()
    total_ship_weight = serializers.SerializerMethodField()
    total_pack = serializers.SerializerMethodField()
    # items = DetailSerializer(many=True, read_only=True)
    class Meta:
        model = ElectricBike
        fields=('total_milage','total_movingtime','total_averagespeed','total_kg','total_boxes','total_letter','total_ship_weight','total_pack')


    def get_total_letter(self, obj):
        totalpieces = Edetails.objects.all().aggregate(total_letter=Sum('letteritems'))
        return totalpieces["total_letter"]

    def get_total_ship_weight(self, obj):
        totalpieces = Edetails.objects.all().aggregate(total_ship_weight=Sum('shipweight'))
        return totalpieces["total_ship_weight"]

    def get_total_pack(self, obj):
        totalpieces = Edetails.objects.all().aggregate(total_pack=Sum('package'))
        return totalpieces["total_pack"]
    
    def get_total_milage(self, obj):
        totalpieces = Edetails.objects.all().aggregate(total_milage=Sum('milage'))
        return totalpieces["total_milage"]
    
    def get_total_movingtime(self, obj):
        totalpieces = Edetails.objects.all().aggregate(total_movingtime=Sum('movingtime'))
        return totalpieces["total_movingtime"]
    
    def get_total_averagespeed(self, obj):
        totalpieces = Edetails.objects.all().aggregate(total_averagespeed=Round(Avg('averagespeed')))
        return totalpieces["total_averagespeed"]

    def get_total_kg(self, obj):
        totalpieces = Edetails.objects.all().aggregate(total_kg=Sum('kgtrasported'))
        return totalpieces["total_kg"]

    def get_total_boxes(self, obj):
        totalpieces = Edetails.objects.all().aggregate(total_boxes=Sum('additionalbox'))
        return totalpieces["total_boxes"]
