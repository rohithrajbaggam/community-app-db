from django.contrib import admin
from .models import CategoryModel, SubCategoryModel, CategoryMediaModel
# Register your models here.
admin.site.register(CategoryMediaModel)
admin.site.register(CategoryModel)
admin.site.register(SubCategoryModel)
