from django.contrib import admin

from NanoWareControl.models import Logs, Moisture_Checker, Tomato_Plant_Height1, Tomato_Plant_Height2, Tomato_Plant_Height3, Greengram_Plant_Height1, Greengram_Plant_Height2, Greengram_Plant_Height3, Plants_Harvest, Seeds_Sown, Water_Irrigated, Seed_Type

# Register your models here.
admin.site.register(Logs)
admin.site.register(Moisture_Checker)
admin.site.register(Water_Irrigated)
admin.site.register(Seed_Type)
admin.site.register(Tomato_Plant_Height1)
admin.site.register(Tomato_Plant_Height2)
admin.site.register(Tomato_Plant_Height3)
admin.site.register(Greengram_Plant_Height1)
admin.site.register(Greengram_Plant_Height2)
admin.site.register(Greengram_Plant_Height3)
admin.site.register(Seeds_Sown)
admin.site.register(Plants_Harvest)