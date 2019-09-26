from django.contrib import admin
from .models import Edetails,ElectricBike

# Register your models here.

class ElectricAdmin(admin.ModelAdmin):
    list_display=('bikeid','milage','movingtime','averagespeed','co2')
    list_filter=['bikeid','averagespeed','milage']
    search_fields=['bikeid']
    list_per_page=20

class DetailAdmin(admin.ModelAdmin):
    list_display=('date','user','movingtime','averagespeed','milage')
    list_filter=['user','averagespeed','milage']
    search_fields=['user']
    list_per_page=20

admin.site.register(ElectricBike, ElectricAdmin)
admin.site.register(Edetails,DetailAdmin)
