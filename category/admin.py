from django.contrib import admin
from .models import CategoryModel, SubCategoryModel
# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(SubCategoryModel)
