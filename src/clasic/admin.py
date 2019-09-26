
from django.contrib import admin
from .models import ClassicBike,Cdetails

# Register your models here.

class ElectricAdmin(admin.ModelAdmin):
    list_display=('bikeid','milage','movingtime','averagespeed','co2')
    list_filter=['bikeid','averagespeed','milage']
    search_fields=['bikeid']
    list_per_page=20

class DetailAdmin(admin.ModelAdmin):
    list_display=('date','movingtime','averagespeed','milage')
    list_filter=['date','averagespeed','milage']
    list_per_page=20


admin.site.register(ClassicBike, ElectricAdmin)
admin.site.register(Cdetails,DetailAdmin)
