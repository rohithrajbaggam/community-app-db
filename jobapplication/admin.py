from django.contrib import admin
from .models import JobApplicationMediaModel, JobApplicationDetailModel, JobQualificationModel, JobTypeTitleModel, JobApplicationSkillsRequired, JobExperienceLevelModel, JobApplicationModel
# Register your models here.

admin.site.register(JobApplicationMediaModel)
admin.site.register(JobApplicationDetailModel)
admin.site.register(JobQualificationModel)
admin.site.register(JobTypeTitleModel)
admin.site.register(JobApplicationSkillsRequired)
admin.site.register(JobExperienceLevelModel)
admin.site.register(JobApplicationModel)
