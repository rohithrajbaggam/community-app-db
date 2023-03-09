from django.db import models
from category.models import CategoryModel, SubCategoryModel
from company.models import CompanyDetailsModel, CompanyAddressModel
from .utils import ExamModeEnumType

# Create your models here.

class ExamMediaModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    file_field = models.FileField(upload_to="media/examination", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ExamApplicationDetailModel(models.Model):
    website_link = models.TextField(null=True, blank=True)
    posted_date = models.DateTimeField(null=True, blank=True)
    last_date = models.DateTimeField(null=True, blank=True)
    drive_date = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class ExamQualificationModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ExamTypeTitleModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # file_field = models.FileField(upload_to="media/examApplications/", 
    #                               null=True, blank=True)
    media = models.ManyToManyField(ExamMediaModel, related_name="ExamTypeTitleModel_media", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class ExamApplicationSkillsRequired(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    experience_in_years = models.CharField(max_length=200, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ExamExperienceLevelModel(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ExamApplicationModel(models.Model):
    title = models.TextField()
    description = models.TextField(null=True, blank=True)
    media = models.ManyToManyField(ExamMediaModel, related_name="ExamApplicationModel_media", blank=True)
    attchments = models.FileField(upload_to="media/examApplications/", 
                                  null=True, blank=True)
    examination_fee = models.CharField(max_length=100, null=True, blank=True)
    exam_type = models.ManyToManyField(ExamTypeTitleModel, 
                                related_name="ExamApplicationModel_exam_type", 
                                blank=True)
    exam_mode = models.CharField(max_length=100, 
                                choices=ExamModeEnumType.choices(), 
                                null=True, blank=True)
    is_third_party_application = models.BooleanField(null=True, blank=True)
    # if it was a third party exam application, redirect to company website
    exam_application_details = models.ForeignKey(
                    ExamApplicationDetailModel,
                    on_delete=models.CASCADE,
                    related_name = "ExamApplicationModel_exam_application_details", 
                    null=True, blank=True)
    qualification = models.ManyToManyField(
                    ExamQualificationModel, 
                    blank=True, 
                    related_name="ExamApplicationModel_qualification"
                    ) # BTECH, METECH

    skills_required = models.ManyToManyField(ExamApplicationSkillsRequired, 
                    related_name="ExamApplicationModel_skills_required", 
                    blank=True)

    experience_level = models.ManyToManyField(ExamExperienceLevelModel, 
                    related_name="ExamApplicationModel_experience_level", 
                    blank=True)
    address = models.ManyToManyField(CompanyAddressModel,  
                    related_name="ExamApplicationModel_address", 
                    blank=True)
    company = models.ForeignKey(CompanyDetailsModel, on_delete=models.CASCADE, 
                    related_name="ExamApplicationModel_company", 
                    null=True, blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, 
                    related_name="ExamApplicationModel_category", 
                    null=True, blank=True)
    sub_category = models.ForeignKey(SubCategoryModel, on_delete=models.CASCADE, 
                    related_name="ExamApplicationModel_sub_category", 
                    null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.role 
    






