from django.contrib import admin
from .models import ExamMediaModel, ExamApplicationDetailModel, ExamQualificationModel, ExamTypeTitleModel, ExamApplicationSkillsRequired, ExamExperienceLevelModel, ExamApplicationModel
# Register your models here.
admin.site.register(ExamMediaModel)
admin.site.register(ExamApplicationDetailModel)
admin.site.register(ExamQualificationModel)
admin.site.register(ExamTypeTitleModel)
admin.site.register(ExamApplicationSkillsRequired)
admin.site.register(ExamExperienceLevelModel)
admin.site.register(ExamApplicationModel)

