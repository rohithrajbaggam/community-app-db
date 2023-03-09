from django.contrib import admin
from .models import UserAddressModel, UserContactInfoModel, UserEducationDetailsModel, UserExperienceDetailsModel, UserProfileModel
# Register your models here.

admin.site.register(UserAddressModel)
admin.site.register(UserContactInfoModel)
admin.site.register(UserEducationDetailsModel)
admin.site.register(UserExperienceDetailsModel)
admin.site.register(UserProfileModel)
