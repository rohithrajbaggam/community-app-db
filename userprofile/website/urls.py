from .views import UserProfileGenericAPIView, UserResumeModelCreateAPIView, UserResumeModelUpdateAPIView, UserAddressModelCreateAPIView, UserAddressModelUpdateAPIView, UserEducationDetailsModelCreateAPIView, UserEducationDetailsModelUpdateAPIView, UserExperienceDetailsModelCreateAPIView, UserExperienceDetailsModelUpdateAPIView, UserContactInfoModelCreateAPIView, UserContactInfoModelUpdateAPIView, UserCertificatesModelUpdateAPIView, UserCertificatesModelCreateAPIView
from django.urls import path 

urlpatterns = [
    path("user-profile/", UserProfileGenericAPIView.as_view(), name="UserProfileGenericAPIView"),

    path("user-resume/", UserResumeModelCreateAPIView.as_view(), name="UserResumeModelCreateAPIView"),
    path("user-resume/<id>/", UserResumeModelUpdateAPIView.as_view(), name="UserResumeModelUpdateAPIView"),

    path("user-address/", UserAddressModelCreateAPIView.as_view(), name="UserAddressModelCreateAPIView"),
    path("user-address/<id>/", UserAddressModelUpdateAPIView.as_view(), name="UserAddressModelUpdateAPIView"),

    path("user-education/", UserEducationDetailsModelCreateAPIView.as_view(), name="UserEducationDetailsModelCreateAPIView"),
    path("user-education/<id>/", UserEducationDetailsModelUpdateAPIView.as_view(), name="UserEducationDetailsModelUpdateAPIView"),

    path("user-experiences/", UserExperienceDetailsModelCreateAPIView.as_view(), name="UserExperienceDetailsModelModelCreateAPIView"),
    path("user-experiences/<id>/", UserExperienceDetailsModelUpdateAPIView.as_view(), name="UserExperienceDetailsModelUpdateAPIView"),

    path("user-contact-info/", UserContactInfoModelCreateAPIView.as_view(), name="UserContactInfoModelCreateAPIView"),
    path("user-contact-info/<id>/", UserContactInfoModelUpdateAPIView.as_view(), name="UserContactInfoModelUpdateAPIView"),

    path("user-certificate/", UserCertificatesModelCreateAPIView.as_view(), name="UserCertificatesModelCreateAPIView"),
    path("user-certificate/<id>/", UserCertificatesModelUpdateAPIView.as_view(), name="UserCertificatesModelUpdateAPIView")


    
]
