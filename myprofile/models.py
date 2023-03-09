from django.db import models
from django.contrib.auth import get_user_model
from category.models import CategoryModel, SubCategoryModel
from userprofile.models import UserPostModel
from courses.models import CourseModel
from .utils import UserStatusEnumType
from jobapplication.models import JobApplicationModel
from examination.models import ExamApplicationModel
# Create your models here.

class UserCategoryInterestModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="UserCategoryInterestModel_user")
    category = models.ManyToManyField(CategoryModel, related_name="UserCategoryInterestModel_category", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserSubCategoryInterestModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="UserSubCategoryInterestModel_user")
    cateory = models.ForeignKey(UserCategoryInterestModel,on_delete=models.CASCADE, related_name="UserSubCategoryInterestModel_cateory", blank=True)
    sub_category = models.ManyToManyField(SubCategoryModel, related_name="UserSubCategoryInterestModel_sub_category", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserSavedPostsModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="UserSavedPostsModel_user")
    posts = models.ManyToManyField(UserPostModel, related_name="UserSavedPostsModel_posts", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserCourseModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="UserCourseModel_user")
    courses = models.ManyToManyField(CourseModel, blank=True, related_name="UserCourseModel_courses")
    status = models.CharField(max_length=100, choices=UserStatusEnumType.choices(), default="NOSTARTED", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserJobApplicationModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="UserJobApplicationModel_user")
    job_application = models.ManyToManyField(JobApplicationModel, blank=True, related_name="UserJobApplicationModel_job_application")
    status = models.CharField(max_length=100, choices=UserStatusEnumType.choices(), default="NOSTARTED", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserExaminationModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="UserExaminationModel_user")
    examination = models.ManyToManyField(ExamApplicationModel, blank=True, related_name="UserExaminationModel_examination")
    status = models.CharField(max_length=100, choices=UserStatusEnumType.choices(), default="NOSTARTED", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# courses, jobapplications, examinations, 




