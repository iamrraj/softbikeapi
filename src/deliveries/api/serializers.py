from rest_framework import serializers
from ..models import Delivery, User

from bikes.models import ElectricBike
from django.db.models import Sum, Avg, Max, Min, Count, F, Q
from django.db.models import Func
from django.db.models import Q

# class Report

class Round(Func):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 2)'


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields=['addresses','letters_number','letters_weight','packages_number','packaged_weight']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class DeliverySerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username
    class Meta:
        model = Delivery
        fields = '__all__'

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class DashboardSerializer(serializers.ModelSerializer):
    total_milage=serializers.SerializerMethodField()
    total_kg=serializers.SerializerMethodField()
    total_co2=serializers.SerializerMethodField()
    total_walk_milage = serializers.SerializerMethodField()
    total_electric_milage = serializers.SerializerMethodField()
    total_classic_milage = serializers.SerializerMethodField()
    total_walk_kg = serializers.SerializerMethodField()
    total_electric_kg = serializers.SerializerMethodField()
    total_classic_kg = serializers.SerializerMethodField()

    class Meta:
        model = Delivery
        fields = ['total_milage','total_kg','total_co2','total_walk_milage','total_electric_milage','total_classic_milage','total_walk_kg','total_electric_kg','total_classic_kg','too','fromm']

# Its For All Together
    def get_total_milage(self, obj):
        totalpieces = Delivery.objects.all().aggregate(total_milage=Sum('milage'))
        return totalpieces["total_milage"]

    def get_total_kg(self, obj):
        totalpieces = Delivery.objects.all().aggregate(total_kg=Sum('kgtrasported'))
        return totalpieces["total_kg"]

    def get_total_co2(self, obj):
        totalpieces = Delivery.objects.all().aggregate(total_co2=Sum('co2'))
        return totalpieces["total_co2"]
    
# Its For Specific Kg Milage
    def get_total_walk_milage(self, obj):
        totalpieces = Delivery.objects.filter(mode="foot").aggregate(total_walk_milage=Sum('milage'))
        return totalpieces["total_walk_milage"]
    
    def get_total_electric_milage(self, obj):
        totalpieces = Delivery.objects.filter(mode="electric-bike").aggregate(total_electric_milage=Sum('milage'))
        return totalpieces["total_electric_milage"]

    def get_total_classic_milage(self, obj):
        totalpieces = Delivery.objects.filter(mode="bike").aggregate(total_classic_milage=Sum('milage'))
        return totalpieces["total_classic_milage"]

# Its For Specific Kg Transpotead
    def get_total_walk_kg(self, obj):
        totalpieces = Delivery.objects.filter(mode="foot").aggregate(get_total_walk_kg=Sum('kgtrasported'))
        return totalpieces["get_total_walk_kg"]

    def get_total_electric_kg(self, obj):
        totalpieces = Delivery.objects.filter(mode="electric-bike").aggregate(total_electric_kg=Sum('kgtrasported'))
        return totalpieces["total_electric_kg"]

    def get_total_classic_kg(self, obj):
        totalpieces = Delivery.objects.filter(mode="bike").aggregate(total_classic_kg=Sum('kgtrasported'))
        return totalpieces["total_classic_kg"]



class DashboardSerializer1(serializers.ModelSerializer):
    total_milage=serializers.SerializerMethodField()
    total_kg=serializers.SerializerMethodField()
    total_co2=serializers.SerializerMethodField()
    total_walk_milage = serializers.SerializerMethodField()
    total_electric_milage = serializers.SerializerMethodField()
    total_classic_milage = serializers.SerializerMethodField()
    total_walk_kg = serializers.SerializerMethodField()
    total_electric_kg = serializers.SerializerMethodField()
    total_classic_kg = serializers.SerializerMethodField()

    class Meta:
        model = Delivery
        fields = ['total_milage','total_kg','total_co2','total_walk_milage','total_electric_milage','total_classic_milage','total_walk_kg','total_electric_kg','total_classic_kg','too','fromm']

# Its For All Together
    def get_total_milage(self, obj):
        totalpieces = Delivery.objects.filter(too=obj.too,fromm=obj.fromm).aggregate(total_milage=Sum('milage'))
        return totalpieces["total_milage"]

    def get_total_kg(self, obj):
        totalpieces = Delivery.objects.filter(too=obj.too,fromm=obj.fromm).aggregate(total_kg=Sum('kgtrasported'))
        return totalpieces["total_kg"]

    def get_total_co2(self, obj):
        totalpieces = Delivery.objects.filter(too=obj.too,fromm=obj.fromm).aggregate(total_co2=Sum('co2'))
        return totalpieces["total_co2"]
    
# Its For Specific Kg Milage
    def get_total_walk_milage(self, obj):
        totalpieces = Delivery.objects.filter(mode="foot",too=obj.too,fromm=obj.fromm).aggregate(total_walk_milage=Sum('milage'))
        return totalpieces["total_walk_milage"]
    
    def get_total_electric_milage(self, obj):
        totalpieces = Delivery.objects.filter(mode="electric-bike",too=obj.too,fromm=obj.fromm).aggregate(total_electric_milage=Sum('milage'))
        return totalpieces["total_electric_milage"]

    def get_total_classic_milage(self, obj):
        totalpieces = Delivery.objects.filter(mode="bike",too=obj.too,fromm=obj.fromm).aggregate(total_classic_milage=Sum('milage'))
        return totalpieces["total_classic_milage"]

# Its For Specific Kg Transpotead
    def get_total_walk_kg(self, obj):
        totalpieces = Delivery.objects.filter(mode="foot",too=obj.too,fromm=obj.fromm).aggregate(get_total_walk_kg=Sum('kgtrasported'))
        return totalpieces["get_total_walk_kg"]

    def get_total_electric_kg(self, obj):
        totalpieces = Delivery.objects.filter(mode="electric-bike",too=obj.too,fromm=obj.fromm).aggregate(total_electric_kg=Sum('kgtrasported'))
        return totalpieces["total_electric_kg"]

    def get_total_classic_kg(self, obj):
        totalpieces = Delivery.objects.filter(mode="bike",too=obj.too,fromm=obj.fromm).aggregate(total_classic_kg=Sum('kgtrasported'))
        return totalpieces["total_classic_kg"]


class UserSerializer1(serializers.ModelSerializer):
    user1 = serializers.SerializerMethodField()

    def get_user1(self, obj):
        return obj.username

    class Meta:
        model = User
        fields = ['user1','username']

    


class PostmanSerializer(serializers.ModelSerializer):
    total_milage = serializers.SerializerMethodField()
    total_kg = serializers.SerializerMethodField()
    total_walk_milage = serializers.SerializerMethodField()
    total_electric_milage = serializers.SerializerMethodField()
    total_classic_milage = serializers.SerializerMethodField()
    total_walk_kg = serializers.SerializerMethodField()
    total_electric_kg = serializers.SerializerMethodField()
    total_classic_kg = serializers.SerializerMethodField()
    total_boxes=serializers.SerializerMethodField()
    total_movingtime=serializers.SerializerMethodField()
    total_ship=serializers.SerializerMethodField()
    total_letter=serializers.SerializerMethodField()
    total_package=serializers.SerializerMethodField()
    # user = serializers.SerializerMethodField()
    

    # def get_user(self, obj):
    #     return obj.user.username

    class Meta:
        model = User
        fields = '__all__'

     

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def get_total_letter(self, obj):
        totalpieces = Delivery.objects.filter(
            user_id=obj.id).aggregate(total_milage=Sum('letteritems'))
        return totalpieces["total_milage"]

    def get_total_package(self, obj):
        totalpieces = Delivery.objects.filter(
            user_id=obj.id).aggregate(total_package=Sum('package'))
        return totalpieces["total_package"]

    def get_total_ship(self, obj):
        totalpieces = Delivery.objects.filter(
            user_id=obj.id).aggregate(total_ship=Sum('shipweight'))
        return totalpieces["total_ship"]

    def get_total_milage(self, obj):
        totalpieces = Delivery.objects.filter(
            user_id=obj.id).aggregate(total_milage=Sum('milage'))
        return totalpieces["total_milage"]

    def get_total_milage(self, obj):
        totalpieces = Delivery.objects.filter(
            user_id=obj.id).aggregate(total_milage=Sum('milage'))
        return totalpieces["total_milage"]

    def get_total_kg(self, obj):
        totalpieces = Delivery.objects.filter(
            user_id=obj.id).aggregate(total_kg=Sum('kgtrasported'))
        return totalpieces["total_kg"]

    def get_total_co2(self, obj):
        totalpieces = Delivery.objects.filter(
            user_id=obj.id).aggregate(total_co2=Sum('co2'))
        return totalpieces["total_co2"]

    def get_total_boxes(self, obj):
        totalpieces=Delivery.objects.filter(user_id=obj.id).aggregate(
            total_boxes=Sum('additionalbox'))
        return totalpieces["total_boxes"]

    def get_total_movingtime(self, obj):
        totalpieces=Delivery.objects.filter(user_id=obj.id).aggregate(
            total_movingtime=Sum('movingtime'))
        return totalpieces["total_movingtime"]

# Its For Specific Kg Milage
    def get_total_walk_milage(self, obj):
        totalpieces = Delivery.objects.filter(
            user_id=obj.id, mode="foot").aggregate(total_walk_milage=Sum('milage'))
        return totalpieces["total_walk_milage"]

    def get_total_electric_milage(self, obj):
        totalpieces = Delivery.objects.filter(
            user_id=obj.id, mode="electric-bike").aggregate(total_electric_milage=Sum('milage'))
        return totalpieces["total_electric_milage"]

    def get_total_classic_milage(self, obj):
        totalpieces = Delivery.objects.filter(
            user_id=obj.id, mode="bike").aggregate(total_classic_milage=Sum('milage'))
        return totalpieces["total_classic_milage"]

# Its For Specific Kg Transpotead
    def get_total_walk_kg(self, obj):
        totalpieces = Delivery.objects.filter(user_id=obj.id, mode="foot").aggregate(
            get_total_walk_kg=Sum('kgtrasported'))
        return totalpieces["get_total_walk_kg"]

    def get_total_electric_kg(self, obj):
        totalpieces = Delivery.objects.filter(
            user_id=obj.id, mode="electric-bike").aggregate(total_electric_kg=Sum('kgtrasported'))
        return totalpieces["total_electric_kg"]

    def get_total_classic_kg(self, obj):
        totalpieces = Delivery.objects.filter(user_id=obj.id, mode="bike").aggregate(
            total_classic_kg=Sum('kgtrasported'))
        return totalpieces["total_classic_kg"]


class DUserSerializer(serializers.ModelSerializer):
    # detail = DeliverySerializer(many=True, read_only=True)
    results = serializers.SerializerMethodField()
    summery = PostmanSerializer(source="*")
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.username

    class Meta:
        model = User
        fields = '__all__'

    def get_results(self, obj):
        return DeliverySerializer(
            Delivery.objects.filter(
                user=obj.id),
            many=True
        ).data




class ReportSerializer(serializers.ModelSerializer):
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
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = Delivery
        fields = ['too', 'fromm','user', 'total_milage', 'total_movingtime', 'total_averagespeed', 'total_kg', 'total_co2_save',
                  'total_boxes', 'total_user', 'total_letter', 'total_ship_weight', 'total_pack', 'too', 'fromm']


    # def get_mode(self, obj):
    #     totalpiece = Delivery.objects.filter(mode__exact="bike")

    # def get_user(self, obj):
    #     return obj.user.username
        
    def get_total_letter(self, obj):
        totalpieces = Delivery.objects.filter(user_id=obj.id,mode=obj.mode).aggregate(
            total_letter=Sum('letteritems'))
        return totalpieces["total_letter"]

    def get_total_ship_weight(self, obj):
        totalpieces = Delivery.objects.filter(user_id=obj.id,mode=obj.mode).aggregate(
            total_ship_weight=Sum('shipweight'))
        return totalpieces["total_ship_weight"]

    def get_total_pack(self, obj):
        totalpieces = Delivery.objects.filter(user_id=obj.id,mode=obj.mode).aggregate(total_pack=Sum('package'))
        return totalpieces["total_pack"]

    def get_total_milage(self, obj):
        totalpieces = Delivery.objects.filter(user_id=obj.id,mode=obj.mode).aggregate(total_milage=Sum('milage'))
        return totalpieces["total_milage"]

    def get_total_movingtime(self, obj):
        totalpieces = Delivery.objects.filter(user_id=obj.id,mode=obj.mode).aggregate(
            total_movingtime=Sum('movingtime'))
        return totalpieces["total_movingtime"]

    def get_total_averagespeed(self, obj):
        totalpieces = Delivery.objects.filter(user_id=obj.id,mode=obj.mode).aggregate(
            total_averagespeed=Round(Avg('averagespeed')))
        return totalpieces["total_averagespeed"]

    def get_total_kg(self, obj):
        totalpieces = Delivery.objects.filter(user_id=obj.id,mode=obj.mode).aggregate(total_kg=Sum('kgtrasported'))
        return totalpieces["total_kg"]

    def get_total_co2_save(self, obj):
        totalpieces = Delivery.objects.filter(user_id=obj.id,mode=obj.mode).aggregate(total_co2_save=Sum('co2'))
        return totalpieces["total_co2_save"]

    def get_total_boxes(self, obj):
        totalpieces = Delivery.objects.filter(user_id=obj.id,mode=obj.mode).aggregate(total_boxes=Sum('additionalbox'))
        return totalpieces["total_boxes"]

    def get_total_user(self, obj):
        totalpieces = Delivery.objects.filter(user_id=obj.user.id,
            mode=obj.mode).aggregate(total_user=Sum('nouser'))
        return totalpieces["total_user"]


