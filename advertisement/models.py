from django.db import models
from category.models import CategoryModel, SubCategoryModel
from company.models import CompanyDetailsModel
# Create your models here.
class AdvertisementTypeModel(models.Model):
    title = models.CharField(max_length=100) # paid, unpaid, company advertisement.. etc

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class AdvertisementMediaModel(models.Model):
    title = models.TextField(null=True, blank=True)
    file_field = models.FileField(upload_to="media/advertisement/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AdvertisementModel(models.Model):
    title = models.TextField()
    media = models.ManyToManyField(AdvertisementMediaModel, blank=True, related_name="AdvertisementModel_media")
    description = models.TextField(null=True, blank=True)
    advertisement_type = models.ForeignKey(AdvertisementTypeModel, on_delete=models.CASCADE, related_name="AdvertisementModel_AdvertisementModel", blank=True, null=True)
    company = models.ManyToManyField(CompanyDetailsModel, blank=True, related_name="AdvertisementModel_company")
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name="AdvertisementModel_category", null=True, blank=True)
    sub_category = models.ForeignKey(SubCategoryModel, on_delete=models.CASCADE, related_name="AdvertisementModel_sub_category", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[0:20]

