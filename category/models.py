from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="media/category/images/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SubCategoryModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name="SubCategoryModel_category")
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="media/category/images/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

