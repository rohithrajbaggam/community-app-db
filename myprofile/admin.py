from django.contrib import admin
from .models import UserCategoryInterestModel, UserSubCategoryInterestModel, UserSavedPostsModel, UserCourseModel, UserJobApplicationModel, UserExaminationModel
# Register your models here.

admin.site.register(UserCategoryInterestModel)
admin.site.register(UserSubCategoryInterestModel)
admin.site.register(UserSavedPostsModel)
admin.site.register(UserCourseModel)
admin.site.register(UserJobApplicationModel)
admin.site.register(UserExaminationModel)

