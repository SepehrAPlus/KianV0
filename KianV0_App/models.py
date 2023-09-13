from django.db import models
from django.contrib import admin 
import time 
from django.shortcuts import render
# Create your models here


def generate_image_path(instance, file_name):
  return int(time.time()).__str__()+"__"+file_name


class ShopItem(models.Model):
  title = models.CharField(max_length=248)
  mareket_price = models.FloatField(default=0.0)
  offered_price = models.FloatField(default=0.0)
  order_count = models.IntegerField(default=0)
  caption = models.TextField(max_length=400, default="")
  #will be using id of model
  image = models.ImageField(upload_to=generate_image_path)
  is_is_stock = models.BooleanField(default=True)
  
admin.site.register(ShopItem)

class ViewCounter(models.Model):
  value = models.IntegerField()
  caller = models.CharField(default="counter", max_length=7)

admin.site.register(ViewCounter)
