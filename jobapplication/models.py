from django.db import models
from category.models import CategoryModel, SubCategoryModel
from company.models import CompanyDetailsModel, CompanyAddressModel
from .utils import JobModeEnumType

# Create your models here.

class JobApplicationMediaModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    file_field = models.FileField(upload_to="media/examination", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


class JobApplicationDetailModel(models.Model):
    website_link = models.TextField(null=True, blank=True)
    posted_date = models.DateTimeField(null=True, blank=True)
    last_date = models.DateTimeField(null=True, blank=True)
    drive_date = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


class JobQualificationModel(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


class JobTypeTitleModel(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    # file_field = models.FileField(upload_to="media/jobApplications/", 
    #                               null=True, blank=True)
    media = models.ManyToManyField(JobApplicationMediaModel, related_name="JobTypeTitleModel_media", blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class JobApplicationSkillsRequired(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    experience_in_years = models.CharField(max_length=200, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

class JobExperienceLevelModel(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

class JobApplicationModel(models.Model):
    role = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    media = models.ManyToManyField(JobApplicationMediaModel, related_name="JobApplicationModel_media", blank=True)
    # file_field = models.FileField(upload_to="media/jobApplications/", 
    #                               null=True, blank=True)
    package = models.CharField(max_length=100, null=True, blank=True)
    attchments = models.FileField(upload_to="media/jobApplications/", 
                                  null=True, blank=True)
    job_type = models.ManyToManyField(JobTypeTitleModel, 
                                related_name="JobApplicationModel_job_type", 
                                blank=True)
    job_mode = models.CharField(max_length=100, 
                                choices=JobModeEnumType.choices(), 
                                null=True, blank=True)
    notice_period = models.CharField(max_length=100, null=True, blank=True)
    no_of_experience = models.CharField(max_length=100, null=True, blank=True)
    is_third_party_application = models.BooleanField(null=True, blank=True)
    # if it was a third party job application, redirect to company website
    job_application_details = models.ForeignKey(
                    JobApplicationDetailModel,
                    on_delete=models.CASCADE,
                    related_name = "JobApplicationModel_job_application_details", 
                    null=True, blank=True)
    qualification = models.ManyToManyField(
                    JobQualificationModel, 
                    blank=True, 
                    related_name="JobApplicationModel_qualification"
                    ) # BTECH, METECH

    skills_required = models.ManyToManyField(JobApplicationSkillsRequired, 
                    related_name="JobApplicationModel_skills_required", 
                    blank=True)

    experience_level = models.ManyToManyField(JobExperienceLevelModel, 
                    related_name="JobApplicationModel_experience_level", 
                    blank=True)
    address = models.ManyToManyField(CompanyAddressModel,  
                    related_name="JobApplicationModel_address", 
                    blank=True)
    company = models.ForeignKey(CompanyDetailsModel, on_delete=models.CASCADE, 
                    related_name="JobApplicationModel_company", 
                    null=True, blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, 
                    related_name="JobApplicationModel_category", 
                    null=True, blank=True)
    sub_category = models.ForeignKey(SubCategoryModel, on_delete=models.CASCADE, 
                    related_name="JobApplicationModel_sub_category", 
                    null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    






