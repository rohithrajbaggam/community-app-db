from django.contrib import admin
from .models import  CompanyAddressModel,CompanyContactInfoModel, CompanyManagerInfoModel, CompanyDetailsModel, companyMediaModel
# Register your models here.

admin.site.register(CompanyAddressModel)
admin.site.register(CompanyContactInfoModel)
admin.site.register(companyMediaModel)
admin.site.register(CompanyManagerInfoModel)
admin.site.register(CompanyDetailsModel)

