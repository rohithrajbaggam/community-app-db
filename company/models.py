from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class CompanyAddressModel(models.Model):
    address_1 = models.CharField(max_length=500, null=True, blank=True)
    address_2 = models.CharField(max_length=500, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=500, null=True, blank=True)
    state = models.CharField(max_length=500, null=True, blank=True)
    country = models.CharField(max_length=500, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class CompanyContactInfoModel(models.Model):
    gmail = models.CharField(max_length=200, null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    whatsapp = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CompanyManagerInfoModel(models.Model):
    name = models.CharField(max_length=100)
    # user = models.ForeignKey(get_user_model(), related_name="CompanyManagerInfoModel_user", on_delete=models.CASCADE, null=True, blank=True)
    designation = models.CharField(max_length=200, null=True, blank=True)
    role = models.CharField(max_length=200, null=True, blank=True)
    gmail = models.CharField(max_length=200, null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    whatsapp = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=200, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class companyMediaModel(models.Model):
    title = models.TextField(null=True, blank=True)
    file_field = models.FileField(upload_to="media/advertisement/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CompanyDetailsModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    address = models.ManyToManyField(CompanyAddressModel, blank=True, related_name="CompanyDetailsModel_address")
    media = models.ManyToManyField(companyMediaModel, related_name="CompanyDetailsModel_media", blank=True)
    contact_info = models.ManyToManyField(CompanyContactInfoModel, blank=True, related_name="CompanyDetailsModel_contact_info")
    manager_info = models.ManyToManyField(CompanyManagerInfoModel, blank=True, related_name="CompanyDetailsModel_manager_info")
    company_website = models.CharField(max_length=200, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

