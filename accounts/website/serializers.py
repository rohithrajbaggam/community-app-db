import random 
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.mail import send_mail
from rest_framework import serializers
from accounts.models import EmailOtpVerifyModel
from userprofile.models import UserProfileModel
from myprofile.models import UserCategoryInterestModel, UserSavedPostsModel, UserCourseModel, UserJobApplicationModel, UserExaminationModel

# User Registration View
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ["username","phone_number" ,"email", "password"]
    
    def validate(self, data):
        if get_user_model().objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError({
                "message" : "Email Already Exists"
            })
        if len(data["phone_number"]) != 10:
            raise serializers.ValidationError({
                "message" : "phone_number must contains 10 digits only"
            })
        return data 
    
    def create(self, validated_data):
        user = get_user_model().objects.create(
            email = validated_data["email"],
            username = validated_data["username"],
            phone_number = validated_data["phone_number"]
        )
        user.set_password(validated_data["password"])
        UserProfileModel.objects.create(user=user)
        UserCategoryInterestModel.objects.create(user=user)
        UserSavedPostsModel.objects.create(user=user) 
        UserCourseModel.objects.create(user=user) 
        UserJobApplicationModel.objects.create(user=user) 
        UserExaminationModel.objects.create(user=user)
        user.save()

        return validated_data

# Sending otp to mail view
class ForgotPasswordSendEmailOtpVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailOtpVerifyModel
        fields = ["email"]
    
    def validate(self, data):
        if not get_user_model().objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError({
                "message" : "Email does not exist"
            })
        return data 
    
        
    def forgot_password_send_email(self, subject, message, email, sender):
        try:
            send_mail(
                subject,
                message,
                sender,
                email
            )
            return True 
        except Exception as e:
            print(e)
            return False 

    def create(self, validated_data):
        email = validated_data["email"]
        user = get_user_model().objects.get(email=email)
        otp = random.randint(100000, 999999)
        if self.forgot_password_send_email(
            subject=f"{user.username}, here's your OTP to verify your email address on Community APP",
            message = f"""
                You are receiving this email because a request has been made to reset your password. If you did not make this request, please disregard this email.
                To reset your password, Please verify the OTP
                {otp}
                This otp will expire in few minitues.


            """,
            sender = settings.EMAIL_HOST,
            email = [email]
        ):          
            instance = EmailOtpVerifyModel.objects.create(
                user = user,
                email = email,
                otp = otp 
            )
        else:
            raise serializers.ValidationError({
                "message" : "Something went wrong"
            })
        return validated_data
        
# Otp Verification APIView
class ForgotPasswordEmailOTPVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailOtpVerifyModel
        fields = ["email", "otp"]
    
    def validate(self, data):
        if not get_user_model().objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError({
                "message" : "Email does not exist"
            })
        queryset = EmailOtpVerifyModel.objects.filter(email = data["email"]).last()
        if not queryset.is_active:
            raise serializers.ValidationError({
                "message" : "No Active OTP Found, Request for a new OTP"
            })
        if data["otp"] != queryset.otp:
            raise serializers.ValidationError({
                "message" : "OTP is Incorrect"
            })
        return data
 

# Changing Password After Email verification 
class ChangePasswordWithEmailVerificationSerializer(serializers.Serializer):
    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    

    def validate(self, data):
        if not get_user_model().objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError({
                "message" : "Email does not exist"
            })
        return data 
    
    def create(self, validated_data):
        user = get_user_model().objects.get(email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()
        return validated_data

# Changing Password with Entering Old Password
class ChangePasswordWithOldPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = get_user_model().objects.get(email=self.context["request"].user.email)
        if not user.check_password(data["old_password"]):
            raise serializers.ValidationError({
                "message" : "Old Password is Incorrect"
            })
        return data 
    
    def create(self, validated_data):

        user = get_user_model().objects.get(email=self.context["request"].user.email)
        user.set_password(validated_data["new_password"])
        user.save()
        return validated_data


