from rest_framework import serializers
from .models import Wdetails, Walk
from rest_framework_jwt.settings import api_settings
from django.db.models import Sum, Avg, Max, Min, Count, F, Q
from django.db.models import Func


class WlectricSerializer(serializers.ModelSerializer):

    class Meta:
        model = Walk
        fields = ('pk', 'username', 'milage', 'movingtime', 'kgtransported',
                  'additionalbox', 'too', 'fromm', 'letteritems', 'shipweight', 'package')


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wdetails
        fields = '__all__'


class DDetailSerializer(serializers.ModelSerializer):
    items = DetailSerializer(many=True, read_only=True)

    class Meta:
        model = Walk
        fields = ('pk', 'username', 'milage', 'movingtime', 'kgtransported',
                  'additionalbox', 'too', 'fromm', 'letteritems', 'shipweight', 'package', 'items')


# class Round(Func):
#     function = 'ROUND'
#     template = '%(function)s(%(expressions)s, 2)'


class SummerySerializer(serializers.ModelSerializer):
    total_milage = serializers.SerializerMethodField()
    total_movingtime = serializers.SerializerMethodField()
    total_kg = serializers.SerializerMethodField()
    total_boxes = serializers.SerializerMethodField()
    total_letter = serializers.SerializerMethodField()
    total_ship_weight = serializers.SerializerMethodField()
    total_pack = serializers.SerializerMethodField()

    class Meta:
        model = Walk
        fields = ('too', 'fromm', 'total_milage', 'total_movingtime', 'total_kg',
                  'total_boxes',  'total_letter', 'total_ship_weight', 'total_pack')

    def get_total_letter(self, obj):
        totalpieces = Walk.objects.all().aggregate(total_letter=Sum('letteritems'))
        return totalpieces["total_letter"]

    def get_total_ship_weight(self, obj):
        totalpieces = Walk.objects.all().aggregate(
            total_ship_weight=Sum('shipweight'))
        return totalpieces["total_ship_weight"]

    def get_total_pack(self, obj):
        totalpieces = Walk.objects.all().aggregate(total_pack=Sum('package'))
        return totalpieces["total_pack"]

    def get_total_milage(self, obj):
        totalpieces = Walk.objects.all().aggregate(total_milage=Sum('milage'))
        return totalpieces["total_milage"]

    def get_total_movingtime(self, obj):
        totalpieces = Walk.objects.all().aggregate(total_movingtime=Sum('movingtime'))
        return totalpieces["total_movingtime"]

    def get_total_kg(self, obj):
        totalpieces = Walk.objects.all().aggregate(total_kg=Sum('kgtransported'))
        return totalpieces["total_kg"]

    def get_total_boxes(self, obj):
        totalpieces = Walk.objects.all().aggregate(total_boxes=Sum('additionalbox'))
        return totalpieces["total_boxes"]


class DSummerySerializer(serializers.ModelSerializer):
    total_milage = serializers.SerializerMethodField()
    total_movingtime = serializers.SerializerMethodField()
    total_kg = serializers.SerializerMethodField()
    total_boxes = serializers.SerializerMethodField()
    total_letter = serializers.SerializerMethodField()
    total_ship_weight = serializers.SerializerMethodField()
    total_pack = serializers.SerializerMethodField()
    items = DetailSerializer(many=True, read_only=True)

    class Meta:
        model = Walk
        fields = ('items', 'total_milage', 'total_movingtime',
                  'total_kg', 'total_boxes', 'total_letter', 'total_ship_weight', 'total_pack')

    def get_total_letter(self, obj):
        totalpieces = Wdetails.objects.all().aggregate(total_letter=Sum('letteritems'))
        return totalpieces["total_letter"]

    def get_total_ship_weight(self, obj):
        totalpieces = Wdetails.objects.all().aggregate(
            total_ship_weight=Sum('shipweight'))
        return totalpieces["total_ship_weight"]

    def get_total_pack(self, obj):
        totalpieces = Wdetails.objects.all().aggregate(total_pack=Sum('package'))
        return totalpieces["total_pack"]

    def get_total_milage(self, obj):
        totalpieces = Wdetails.objects.all().aggregate(total_milage=Sum('milage'))
        return totalpieces["total_milage"]

    def get_total_movingtime(self, obj):
        totalpieces = Wdetails.objects.all().aggregate(
            total_movingtime=Sum('movingtime'))
        return totalpieces["total_movingtime"]

    def get_total_kg(self, obj):
        totalpieces = Wdetails.objects.all().aggregate(total_kg=Sum('kgtransported'))
        return totalpieces["total_kg"]

    def get_total_boxes(self, obj):
        totalpieces = Wdetails.objects.all().aggregate(total_boxes=Sum('additionalbox'))
        return totalpieces["total_boxes"]
