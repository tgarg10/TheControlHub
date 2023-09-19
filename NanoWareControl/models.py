from django.db import models
from datetime import datetime

# Create your models here.
class Logs(models.Model):
    image_link = models.CharField(max_length=16, blank=True)
    camera = models.CharField(max_length=16, blank=True, default = "Main")
    time = models.CharField(max_length=16, blank=True)
    date = models.CharField(max_length=16, blank=True)
    details = models.CharField(max_length=64, blank=True, default = "Logged Image")

class Moisture_Checker(models.Model):
    moisture_level = models.FloatField(blank=True)
    date = models.CharField(max_length=16, default=datetime.now().strftime('%d %b'))

class Water_Irrigated(models.Model):
    water_irrigated = models.FloatField(blank=True)
    date = models.CharField(max_length=16, default=datetime.now().strftime('%d %b'))

class Seed_Type(models.Model):
    seed_type = models.CharField(max_length=16)
    colour_on_graph = models.CharField(max_length=16, choices=[('Red', 'Red'), ('Orange', 'Orange'), ('Yellow', 'Yellow'), ('Green', 'Green'), ('Cyan', 'Cyan'), ('Blue', 'Blue'), ('Violet', 'Violet'), ('Magenta', 'Magenta'), ('Rose', 'Rose'), ('Black', 'Black')])
    seed_type_count = models.IntegerField()
    
class Tomato_Plant_Height1(models.Model):
    plant_height = models.FloatField(blank=True)
    date = models.CharField(max_length=16, default=datetime.now().strftime('%d %b'))

class Greengram_Plant_Height1(models.Model):
    plant_height = models.FloatField(blank=True)
    date = models.CharField(max_length=16, default=datetime.now().strftime('%d %b'))

class Tomato_Plant_Height2(models.Model):
    plant_height = models.FloatField(blank=True)
    date = models.CharField(max_length=16, default=datetime.now().strftime('%d %b'))

class Greengram_Plant_Height2(models.Model):
    plant_height = models.FloatField(blank=True)
    date = models.CharField(max_length=16, default=datetime.now().strftime('%d %b'))

class Tomato_Plant_Height3(models.Model):
    plant_height = models.FloatField(blank=True)
    date = models.CharField(max_length=16, default=datetime.now().strftime('%d %b'))

class Greengram_Plant_Height3(models.Model):
    plant_height = models.FloatField(blank=True)
    date = models.CharField(max_length=16, default=datetime.now().strftime('%d %b'))

class Seeds_Sown(models.Model):
    seed_sown_count = models.FloatField(blank=True)
    date = models.CharField(max_length=16, default=datetime.now().strftime('%d %b'))

class Plants_Harvest(models.Model):
    plants_harvested_count = models.FloatField(blank=True)
    date = models.CharField(max_length=16, default=datetime.now().strftime('%d %b'))
