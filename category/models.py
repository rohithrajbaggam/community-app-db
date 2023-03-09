from django.db import models

# Create your models here.
class CategoryMediaModel(models.Model):
    title = models.TextField(null=True, blank=True)
    file_field = models.FileField(upload_to="media/category/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CategoryModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    media = models.ManyToManyField(CategoryMediaModel, blank=True, related_name="CategoryModel_media")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SubCategoryModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name="SubCategoryModel_category")
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    media = models.ManyToManyField(CategoryMediaModel, blank=True, related_name="SubCategoryModel_media")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

