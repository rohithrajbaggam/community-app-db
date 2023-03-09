from django.contrib import admin
from .models import AdvertisementTypeModel, AdvertisementModel, AdvertisementMediaModel
      
# Register your models here.
admin.site.register(AdvertisementMediaModel)
admin.site.register(AdvertisementTypeModel)
admin.site.register(AdvertisementModel)


