from rest_framework import serializers
from .models import Report
from rest_framework_jwt.settings import api_settings
from django.db.models import Sum,Avg,Max,Min,Count,F,Q
from django.db.models import Func

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

# class DetailSerializer()