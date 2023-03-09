from django.contrib import admin
from .models import UserCategoryInterestModel, UserSubCategoryInterestModel, UserSavedPostsModel
# Register your models here.

admin.site.register(UserCategoryInterestModel)
admin.site.register(UserSubCategoryInterestModel)
admin.site.register(UserSavedPostsModel)
