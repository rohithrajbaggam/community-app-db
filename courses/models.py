from django.db import models
from category.models import CategoryModel, SubCategoryModel
from django.contrib.auth import get_user_model
from .utils import CourseStatusEnum
# Create your models here.

# class CourseLanguageModel(models.Model):
    # title = models.CharField(max_length=100)

class CourseMediaModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    file_field = models.FileField(upload_to="media/courses", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class CourseWhatYouWillLearnModel(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    # file_field = models.FileField(upload_to="media/courses", null=True, blank=True)
    media = models.ManyToManyField(CourseMediaModel, related_name="CourseWhatYouWillLearnModel_media", blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class CourseUserRequirementsModel(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    media = models.ManyToManyField(CourseMediaModel, related_name="CourseUserRequirementsModel_media", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class CourseThisCourseIncludesModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    media = models.ManyToManyField(CourseMediaModel, related_name="CourseThisCourseIncludesModel_media", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Quiz options Model
class CourseQuizOptionsModel(models.Model):
    title = models.TextField(null=True, blank=True)
    media = models.ManyToManyField(CourseMediaModel, related_name="CourseQuizOptionsModel_media", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Quiz Question Model 
class CourseQuizModel(models.Model):
    question = models.TextField(null=True, blank=True)
    media = models.ManyToManyField(CourseMediaModel, related_name="CourseQuizModel_media", blank=True)
    answer = models.ForeignKey(CourseQuizOptionsModel, on_delete=models.CASCADE, related_name="CourseQuizModel_answer")
    options = models.ManyToManyField(CourseQuizOptionsModel, blank=True, related_name="CourseQuizModel_options")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CourseVideoMediaModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    media = models.ManyToManyField(CourseMediaModel, related_name="CourseVideoMediaModel_media", blank=True)
    resources = models.FileField(upload_to="media/courses", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CourseSectionContentModel(models.Model):
    quiz = models.ForeignKey(CourseQuizModel, related_name="CourseSectionContentModel_quiz", on_delete=models.CASCADE, null=True, blank=True)
    video = models.ForeignKey(CourseVideoMediaModel, related_name="CourseSectionContentModel_video", on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CourseSectionModel(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    # media_list = models.ManyToManyField(CourseVideoMediaModel, related_name="CourseSessionModel_media_list", blank=True)
    content = models.ManyToManyField(CourseSectionContentModel, related_name="CourseSectionModel_content", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CourseModel(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    media = models.ManyToManyField(CourseMediaModel, blank=True, related_name="CourseModel_media")
    summary = models.TextField(null=True, blank=True)
    # language = models.ForeignKey(CourseLanguageModel, on_delete=models.CASCADE, related_name="CourseModel_language", null=True, blank=True)
    language = models.CharField(max_length=100,null=True, blank=True)

    
    instructor = models.ManyToManyField(get_user_model(), related_name="CourseModel_instructor", blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name="CourseModel_category", null=True, blank=True)
    sub_category = models.ForeignKey(SubCategoryModel, on_delete=models.CASCADE, related_name="CourseModel_sub_category", null=True, blank=True)
    what_you_will_learn = models.ManyToManyField(CourseWhatYouWillLearnModel, related_name="CourseModel_what_you_will_learn", blank=True)
    user_requirements = models.ManyToManyField(CourseUserRequirementsModel, related_name="CourseModel_user_requirements")
    this_course_include = models.ManyToManyField(CourseThisCourseIncludesModel, blank=True, related_name="CourseModel_this_course_include")
    course_sections = models.ManyToManyField(CourseSectionModel, related_name="CourseModel_course_sections", blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

# user specified course section for tracking user course logs
# class CourseVideoTrackingModel():
#     pass 

# class CourseTrackerModel(models.Model):
#     course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name="CourseTrackerModel_course")
#     status = models.CharField(max_length=100, choices=CourseStatusEnum.choices(), default="NOTSTARTED", blank=True)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)



# class UserCourseContentModel(models.Model):
#     user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="UserCourseContentModel_user")
#     course = models.ManyToManyField(CourseTrackerModel, blank=True, related_name="UserCourseContentModel_course")

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)



