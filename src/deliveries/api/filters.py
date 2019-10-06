from deliveries.models import Delivery
from django_filters.rest_framework import BaseInFilter, NumberFilter, FilterSet


class NumberInFilter(BaseInFilter, NumberFilter):
    pass


class ReportFilter(FilterSet):
    user = NumberInFilter(field_name='user', lookup_expr='in')

    class Meta:
        model = Delivery
        # You should put here your existing filters
        fields = {
            'too': ['lte'],
            'fromm': ['gte'],
            'electric_bike': ['exact'],
            'mode': ['exact'],
        }
