from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserRegistrationAPIView, UserForgotPasswordSendEmailOTPAPIView, UserForgotPasswordEmailOTPVerifyAPIView, ChangePasswordWithEmailVerificationAPIView, ChangePasswordWithOldPasswordAPIView, DummyAPIView

urlpatterns = [
    path("dummy-api/", DummyAPIView.as_view(), name="DummyAPIView"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("register/", UserRegistrationAPIView.as_view(), name="UserRegistrationAPIView"),
    path("forgot-password-send-otp/", UserForgotPasswordSendEmailOTPAPIView.as_view(), name="UserForgotPasswordSendEmailOTPAPIView"),
    path("forgot-password-verify-otp/", UserForgotPasswordEmailOTPVerifyAPIView.as_view(), name="UserForgotPasswordEmailOTPVerifyAPIView"),

    path("create-new-password/", ChangePasswordWithEmailVerificationAPIView.as_view(), name="ChangePasswordWithEmailVerificationAPIView"),
    path("change-password/", ChangePasswordWithOldPasswordAPIView.as_view(), name="ChangePasswordWithOldPasswordAPIView"),


]
