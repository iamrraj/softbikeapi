from rest_framework import serializers
from deliveries.models import Delivery, User
from deliveries.api.serializers import DeliverySerializer
from bikes.models import ElectricBike
from bikes.api.serializers import ElectricBikeSerializer
from walk.api.serializers import WalkSerializer
from django.db.models import Sum, Avg, Max, Min, Count, F, Q
from django.db.models import Func
from django.db.models import Q

# This is Specified for Classic bike


class Round(Func):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 2)'


class ClassSerializer(serializers.ModelSerializer):
    total_milage = serializers.SerializerMethodField()
    total_movingtime = serializers.SerializerMethodField()
    total_averagespeed = serializers.SerializerMethodField()
    total_kg = serializers.SerializerMethodField()
    total_co2_save = serializers.SerializerMethodField()
    total_boxes = serializers.SerializerMethodField()
    total_letter = serializers.SerializerMethodField()
    total_ship_weight = serializers.SerializerMethodField()
    total_pack = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    # summery = ClassicSummerySerializer(source='*')

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def get_total_letter(self, obj):
        totalpieces = Delivery.objects.filter(user_id=obj.user.id, mode__exact="bike").aggregate(
            total_letter=Sum('letteritems'))
        return totalpieces["total_letter"]

    def get_total_ship_weight(self, obj):
        totalpieces = Delivery.objects.filter(user_id=obj.user.id, mode__exact="bike").aggregate(
            total_ship_weight=Sum('shipweight'))
        return totalpieces["total_ship_weight"]

    def get_total_pack(self, obj):
        totalpieces = Delivery.objects.filter(
            user_id=obj.user.id, mode__exact="bike").aggregate(total_pack=Sum('package'))
        return totalpieces["total_pack"]

    def get_total_milage(self, obj):
        totalpieces = Delivery.objects.filter(
            user_id=obj.user.id, mode__exact="bike").aggregate(total_milage=Sum('milage'))
        return totalpieces["total_milage"]

    def get_total_movingtime(self, obj):
        totalpieces = Delivery.objects.filter(user_id=obj.user.id, mode__exact="bike").aggregate(
            total_movingtime=Sum('movingtime'))
        return totalpieces["total_movingtime"]

    def get_total_averagespeed(self, obj):
        totalpieces = Delivery.objects.filter(user_id=obj.user.id, mode__exact="bike").aggregate(
            total_averagespeed=Round(Avg('averagespeed')))
        return totalpieces["total_averagespeed"]

    def get_total_kg(self, obj):
        totalpieces = Delivery.objects.filter(
            user_id=obj.user.id, mode__exact="bike").aggregate(total_kg=Sum('kgtrasported'))
        return totalpieces["total_kg"]

    def get_total_co2_save(self, obj):
        totalpieces = Delivery.objects.filter(
            user_id=obj.user.id, mode__exact="bike").aggregate(total_co2_save=Sum('co2'))
        return totalpieces["total_co2_save"]

    def get_total_boxes(self, obj):
        totalpieces = Delivery.objects.filter(user_id=obj.user.id, mode__exact="bike").aggregate(
            total_boxes=Sum('additionalbox'))
        return totalpieces["total_boxes"]


# This is for walk
class DetailClassSerializer(serializers.ModelSerializer):
    detail = serializers.SerializerMethodField()
    summery = ClassSerializer(source='*')
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    def get_detail(self, obj):
        return DeliverySerializer(
            Delivery.objects.filter(user_id=obj.user.id, mode="bike"),
            many=True
        ).data

    class Meta:
        model = User
        fields = '__all__'


class ClassicSummery(serializers.ModelSerializer):
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
        model = Delivery
        fields = ['too', 'fromm', 'total_milage', 'total_movingtime', 'total_averagespeed', 'total_kg', 'total_co2_save',
                  'total_boxes', 'total_user', 'total_letter', 'total_ship_weight', 'total_pack', 'too', 'fromm']

    def get_total_letter(self, obj):
        totalpieces = Delivery.objects.filter(mode__exact="bike").aggregate(
            total_letter=Sum('letteritems'))
        return totalpieces["total_letter"]

    def get_total_ship_weight(self, obj):
        totalpieces = Delivery.objects.filter(mode__exact="bike").aggregate(
            total_ship_weight=Sum('shipweight'))
        return totalpieces["total_ship_weight"]

    def get_total_pack(self, obj):
        totalpieces = Delivery.objects.filter(
            mode__exact="bike").aggregate(total_pack=Sum('package'))
        return totalpieces["total_pack"]

    def get_total_milage(self, obj):
        totalpieces = Delivery.objects.filter(
            mode__exact="bike").aggregate(total_milage=Sum('milage'))
        return totalpieces["total_milage"]

    def get_total_movingtime(self, obj):
        totalpieces = Delivery.objects.filter(mode__exact="bike").aggregate(
            total_movingtime=Sum('movingtime'))
        return totalpieces["total_movingtime"]

    def get_total_averagespeed(self, obj):
        totalpieces = Delivery.objects.filter(mode__exact="bike").aggregate(
            total_averagespeed=Round(Avg('averagespeed')))
        return totalpieces["total_averagespeed"]

    def get_total_kg(self, obj):
        totalpieces = Delivery.objects.filter(
            mode__exact="bike").aggregate(total_kg=Sum('kgtrasported'))
        return totalpieces["total_kg"]

    def get_total_co2_save(self, obj):
        totalpieces = Delivery.objects.filter(
            mode__exact="bike").aggregate(total_co2_save=Sum('co2'))
        return totalpieces["total_co2_save"]

    def get_total_boxes(self, obj):
        totalpieces = Delivery.objects.filter(mode__exact="bike").aggregate(
            total_boxes=Sum('additionalbox'))
        return totalpieces["total_boxes"]

    def get_total_user(self, obj):
        totalpieces = Delivery.objects.filter(
            mode__exact="bike").aggregate(total_user=Sum('nouser'))
        return totalpieces["total_user"]
