from django.db import models
from django.contrib.auth import get_user_model
from .utils import GenderEnumType
from category.models import CategoryModel, SubCategoryModel
# Create your models here.
class UserAddressModel(models.Model):
    address_1 = models.CharField(max_length=500, null=True, blank=True)
    address_2 = models.CharField(max_length=500, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=500, null=True, blank=True)
    state = models.CharField(max_length=500, null=True, blank=True)
    country = models.CharField(max_length=500, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserEducationDetailsModel(models.Model):
    university_name = models.CharField(max_length=500, null=True, blank=True)
    degree = models.CharField(max_length=500,null=True, blank=True)
    percentage =  models.DecimalField(max_digits = 5,decimal_places = 2, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_pursuing = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserExperienceDetailsModel(models.Model):
    company = models.CharField(max_length=500, null=True, blank=True)
    designation = models.CharField(max_length=500, null=True, blank=True)
    role = models.CharField(max_length=500, null=True, blank=True)
    technology = models.CharField(max_length=500, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    currently_working = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserContactInfoModel(models.Model):
    gmail = models.CharField(max_length=200, null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    whatsapp = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserResumeModel(models.Model):
    file_field = models.FileField(upload_to="media/user_profile/resumes/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserProfileModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="UserProfileModel_user")

    profile_picture = models.FileField(upload_to="media/user_profile/resumes/")
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=50, choices=GenderEnumType.choices(), null=True, blank=True)
    
    resume = models.ManyToManyField(UserResumeModel, related_name="UserProfileModel_resume", blank=True)
    address = models.ManyToManyField(UserAddressModel, related_name="UserProfileModel_address", blank=True)
    education = models.ManyToManyField(UserEducationDetailsModel, related_name="UserProfileModel_education", blank=True)
    experiences = models.ManyToManyField(UserExperienceDetailsModel, related_name="UserProfileModel_experiences", blank=True)
    contact_info = models.ForeignKey(UserContactInfoModel, on_delete=models.CASCADE, related_name="UserProfileModel_contact_info", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email 

class UserPostMediaModel(models.Model):
    file_field = models.FileField(upload_to="media/user-posts/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserPostModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="UserPostModel_user")
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    media = models.ManyToManyField(UserPostMediaModel, related_name="UserPostModel_media", blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name="UserPostModel_category", null=True, blank=True)
    sub_category = models.ForeignKey(SubCategoryModel, on_delete=models.CASCADE, related_name="UserPostModel_sub_category", null=True, blank=True)
    likes = models.ManyToManyField(get_user_model(), related_name="UserPostModel_likes")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email 




