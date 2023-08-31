from django.db import models
from django.contrib import admin 
import time 
# Create your models here


def generate_image_path(instance, file_name):
  return int(time.time()).__str__()+"__"+file_name


class ShopItem(models.Model):
  title = models.CharField(max_length=248)
  image = models.ImageField(upload_to=generate_image_path)
  caption = models.TextField(max_length=400, default="")
  mareket_price = models.FloatField()
  offered_price = models.FloatField()
  is_is_stock = models.BooleanField()
admin.site.register(ShopItem)

class ViewCounter(models.Model):
  value = models.IntegerField()
  caller = models.CharField(default="counter", max_length=7)

admin.site.register(ViewCounter)
