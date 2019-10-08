from rest_framework import serializers
from deliveries.models import Delivery, User
from deliveries.api.serializers import DeliverySerializer
from bikes.models import ElectricBike
from django.db.models import Sum, Avg, Max, Min, Count, F, Q
from django.db.models import Func
from django.db.models import Q


class Round(Func):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 2)'


class WalkSerializer(serializers.ModelSerializer):
    total_milage = serializers.SerializerMethodField()
    total_movingtime = serializers.SerializerMethodField()
    total_kg = serializers.SerializerMethodField()
    total_boxes = serializers.SerializerMethodField()
    total_letter = serializers.SerializerMethodField()
    total_ship_weight = serializers.SerializerMethodField()
    total_pack = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.username

    class Meta:
        model = User
        fields = ['user', 'id', 'total_letter', 'total_milage', 'total_movingtime', 'total_kg', 'total_boxes', 'total_ship_weight', 'total_pack'
                  ]

    def get_total_letter(self, obj):
        totalpieces = Delivery.objects.filter(user_id=obj.id, mode="foot").aggregate(
            total_letter=Sum('letteritems'))
        return totalpieces["total_letter"]

    def get_total_ship_weight(self, obj):
        totalpieces = Delivery.objects.filter(user_id=obj.id, mode="foot").aggregate(
            total_ship_weight=Sum('shipweight'))
        return totalpieces["total_ship_weight"]

    def get_total_pack(self, obj):
        totalpieces = Delivery.objects.filter(
            user_id=obj.id, mode="foot").aggregate(total_pack=Sum('package'))
        return totalpieces["total_pack"]

    def get_total_milage(self, obj):
        totalpieces = Delivery.objects.filter(
            user_id=obj.id, mode="foot").aggregate(total_milage=Sum('milage'))
        return totalpieces["total_milage"]

    def get_total_movingtime(self, obj):
        totalpieces = Delivery.objects.filter(
            user_id=obj.id, mode="foot").aggregate(
            total_movingtime=Sum('movingtime'))
        return totalpieces["total_movingtime"]

    def get_total_kg(self, obj):
        totalpieces = Delivery.objects.filter(
            user_id=obj.id, mode="foot").aggregate(total_kg=Sum('kgtrasported'))
        return totalpieces["total_kg"]

    def get_total_boxes(self, obj):
        totalpieces = Delivery.objects.filter(user_id=obj.id, mode="foot").aggregate(
            total_boxes=Sum('additionalbox'))
        return totalpieces["total_boxes"]


class WalkDetailSerializer(serializers.ModelSerializer):
    # detail = DeliverySerializer(many=True, read_only=True)
    detail = serializers.SerializerMethodField()
    summery = WalkSerializer(source='*')
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.username

    class Meta:
        model = User
        fields = '__all__'

    def get_detail(self, obj):
        return DeliverySerializer(
            Delivery.objects.filter(user_id=obj.id, mode="foot"),
            many=True
        ).data


class WalkSummerySerializer(serializers.ModelSerializer):
    total_milage = serializers.SerializerMethodField()
    total_movingtime = serializers.SerializerMethodField()
    total_kg = serializers.SerializerMethodField()
    total_boxes = serializers.SerializerMethodField()
    total_letter = serializers.SerializerMethodField()
    total_ship_weight = serializers.SerializerMethodField()
    total_pack = serializers.SerializerMethodField()

    class Meta:
        model = Delivery
        fields = ['id', 'total_milage', 'total_movingtime', 'total_kg',
                  'total_boxes',  'total_letter', 'total_ship_weight', 'total_pack', 'too', 'fromm']

    def get_total_letter(self, obj):
        totalpieces = Delivery.objects.filter(mode__exact="foot").aggregate(
            total_letter=Sum('letteritems'))
        return totalpieces["total_letter"]

    def get_total_ship_weight(self, obj):
        totalpieces = Delivery.objects.filter(mode__exact="foot").aggregate(
            total_ship_weight=Sum('shipweight'))
        return totalpieces["total_ship_weight"]

    def get_total_pack(self, obj):
        totalpieces = Delivery.objects.filter(
            mode__exact="foot").aggregate(total_pack=Sum('package'))
        return totalpieces["total_pack"]

    def get_total_milage(self, obj):
        totalpieces = Delivery.objects.filter(
            mode__exact="foot").aggregate(total_milage=Sum('milage'))
        return totalpieces["total_milage"]

    def get_total_movingtime(self, obj):
        totalpieces = Delivery.objects.filter(mode__exact="foot").aggregate(
            total_movingtime=Sum('movingtime'))
        return totalpieces["total_movingtime"]

    def get_total_kg(self, obj):
        totalpieces = Delivery.objects.filter(
            mode__exact="foot").aggregate(total_kg=Sum('kgtrasported'))
        return totalpieces["total_kg"]

    def get_total_boxes(self, obj):
        totalpieces = Delivery.objects.filter(mode__exact="foot").aggregate(
            total_boxes=Sum('additionalbox'))
        return totalpieces["total_boxes"]
