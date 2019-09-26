from rest_framework import serializers
from .models import Udetails,Muser
from rest_framework_jwt.settings import api_settings
from django.db.models import Sum,Avg,Max,Min,Count,F,Q

class UlectricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muser
        fields = ('pk','user','trwalk','Dtwalk','trclassic','Dtclassic','trelectric','Dtelectric','totalMilage',
                'totalweight','phone','too','fromm')
        

class DUlectricSerializer(serializers.ModelSerializer):
    total_milage = serializers.SerializerMethodField()
    total_weight = serializers.SerializerMethodField()
    total_travel_walk = serializers.SerializerMethodField()
    total_distribute_walk = serializers.SerializerMethodField()
    total_travel_classic = serializers.SerializerMethodField()
    total_distribute_classic = serializers.SerializerMethodField()
    total_travel_electric = serializers.SerializerMethodField()
    total_distribute_electric= serializers.SerializerMethodField()

    class Meta:
        model = Muser
        fields = ('too','fromm','pk','total_milage','total_weight','total_travel_walk','total_distribute_walk',
                'total_travel_classic','total_distribute_classic','total_travel_electric','total_distribute_electric')

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

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Udetails
        fields = '__all__'


class DSummerySerializer(serializers.ModelSerializer):
    total_milage = serializers.SerializerMethodField()
    total_movingtime = serializers.SerializerMethodField()
    total_kg = serializers.SerializerMethodField()
    total_boxes = serializers.SerializerMethodField()
    items = DetailSerializer(many=True, read_only=True)
    class Meta:
        model = Udetails
        fields=('items','total_milage','total_movingtime','total_kg','total_boxes')

    def get_total_milage(self, obj):
        totalpieces = Udetails.objects.all().aggregate(total_milage=Sum('milage'))
        return totalpieces["total_milage"]
    
    def get_total_movingtime(self, obj):
        totalpieces = Udetails.objects.all().aggregate(total_movingtime=Sum('movingtime'))
        return totalpieces["total_movingtime"]

    def get_total_kg(self, obj):
        totalpieces = Udetails.objects.all().aggregate(total_kg=Sum('kgtransported'))
        return totalpieces["total_kg"]

    def get_total_boxes(self, obj):
        totalpieces = Udetails.objects.all().aggregate(total_boxes=Sum('additionalbox'))
        return totalpieces["total_boxes"]



class DDetailSerializer(serializers.ModelSerializer):
    items = DetailSerializer(many=True, read_only=True)
    class Meta:
        model = Muser
        fields = ('pk','user','trwalk','Dtwalk','trclassic','Dtclassic','trelectric','Dtelectric','totalMilage','totalweight','phone','too','fromm','items')
