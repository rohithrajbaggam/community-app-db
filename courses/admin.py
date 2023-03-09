from django.contrib import admin
from .models import CourseWhatYouWillLearnModel, CourseUserRequirementsModel, CourseMediaModel, CourseThisCourseIncludesModel, CourseQuizOptionsModel, CourseQuizModel, CourseVideoMediaModel, CourseSectionContentModel, CourseSectionModel, CourseModel
# Register your models here.

admin.site.register(CourseWhatYouWillLearnModel)
admin.site.register(CourseUserRequirementsModel)
admin.site.register(CourseMediaModel)
admin.site.register(CourseThisCourseIncludesModel)
admin.site.register(CourseQuizOptionsModel)
admin.site.register(CourseQuizModel)
admin.site.register(CourseVideoMediaModel)
admin.site.register(CourseSectionContentModel)
admin.site.register(CourseSectionModel)
admin.site.register(CourseModel)
# admin.site.register(CourseTrackerModel)
# admin.site.register(UserCourseContentModel)


