from electric.models import ElectricBike
from clasic.models import ClassicBike
from user.models import Muser
from walk.models import Walk
from django.shortcuts import render
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.db.models import Sum,Avg,Max,Min,Count,F,Q
from django.db.models import Func

class DashBoardSerializer(serializers.ModelSerializer):
    total_co2_electric = serializers.SerializerMethodField()
    total_co2_classic = serializers.SerializerMethodField()
    total_milage = serializers.SerializerMethodField()
    total_weight = serializers.SerializerMethodField()
    total_travel_walk = serializers.SerializerMethodField()
    total_distribute_walk = serializers.SerializerMethodField()
    total_travel_classic = serializers.SerializerMethodField()
    total_distribute_classic = serializers.SerializerMethodField()
    total_travel_electric = serializers.SerializerMethodField()
    total_distribute_electric= serializers.SerializerMethodField()
    # total_co2 = serializers.SerializerMethodField()
    # total_milage1 = serializers.SerializerMethodField()
    # total_weight1 = serializers.SerializerMethodField()

    class Meta:
        model = ElectricBike
        fields=('total_co2_electric','total_co2_classic','total_milage','total_weight','total_travel_walk','total_distribute_walk','total_travel_classic',
        'total_distribute_classic','total_travel_electric','total_distribute_electric')


     # Total Co2 save by Electric
    def get_total_co2_electric(self,obj):
        totalpieces = ElectricBike.objects.all().aggregate(total_co2_electric=Sum('co2'))
        return totalpieces["total_co2_electric"]

    # Total Co2 save by Electric
    def get_total_co2_classic(self,obj):
        totalprice = ClassicBike.objects.all().aggregate(total_co2_classic=Sum('co2'))
        return totalprice["total_co2_classic"]

    # def get_total_co2(self):
    #     totalprice = (self.get_total_co2_classic() + self.get_total_co2_electric())
    #     return totalprice['total_co2']


    # Total Milage and Weight by Electric
    def get_total_milage(self, obj):
        totalpieces = Muser.objects.all().aggregate(total_milage=Sum('totalMilage'))
        return totalpieces["total_milage"]
    def get_total_weight(self, obj):
        totalprice = Muser.objects.all().aggregate(total_weight=Sum('totalweight'))
        return totalprice["total_weight"]

   # Total Travel and distributed by Walk
    def get_total_travel_walk(self, obj):
        totalprice = Muser.objects.all().aggregate(total_travel_walk=Sum('trwalk'))
        return totalprice["total_travel_walk"]
    def get_total_distribute_walk(self, obj):
        totalprice = Muser.objects.all().aggregate(total_distribute_walk=Sum('Dtwalk'))
        return totalprice["total_distribute_walk"]

    # Total Travel and distributed by Classic Bike
    def get_total_travel_classic(self, obj):
        totalprice = Muser.objects.all().aggregate(total_travel_classic=Sum('trclassic'))
        return totalprice["total_travel_classic"]
    def get_total_distribute_classic(self, obj):
        totalprice = Muser.objects.all().aggregate(total_distribute_classic=Sum('Dtclassic'))
        return totalprice["total_distribute_classic"]

# Total Travel and distributed by Electric Bike
    def get_total_travel_electric(self, obj):
        totalprice = Muser.objects.all().aggregate(total_travel_electric=Sum('trelectric'))
        return totalprice["total_travel_electric"]
    def get_total_distribute_electric(self, obj):
        totalprice = Muser.objects.all().aggregate(total_distribute_electric=Sum('Dtelectric'))
        return totalprice["total_distribute_electric"]

