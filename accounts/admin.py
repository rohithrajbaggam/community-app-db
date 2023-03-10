from django.contrib import admin
from .models import UserModel, EmailOtpVerifyModel
from django.contrib.auth.admin import UserAdmin
# Register your models here.


# class UserModelAdmin(UserAdmin):
#     readonly_fields = ('password',)
#     exclude = ("first_name", "last_name")

admin.site.register(UserModel)
admin.site.register(EmailOtpVerifyModel)
