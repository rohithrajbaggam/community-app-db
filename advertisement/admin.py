from django.contrib import admin
from .models import AdvertisementTypeModel, AdvertisementModel
      
# Register your models here.

admin.site.register(AdvertisementTypeModel)
admin.site.register(AdvertisementModel)


