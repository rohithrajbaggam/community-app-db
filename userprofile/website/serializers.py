from rest_framework import serializers
from userprofile.models import UserProfileModel, UserResumeModel, UserContactInfoModel, UserExperienceDetailsModel, UserEducationDetailsModel, UserAddressModel, UserCertificatesModel, UserPostModel, UserPostMediaModel
from django.contrib.auth import get_user_model

class UserPostMediaModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPostMediaModel
        fields = "__all__"

class UserPostModelImageSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = UserPostModel
        fields = "__all__"

    def get_media(self, obj):
        try:
            media =UserPostMediaModelListSerializer(obj.media.all(), many=True).data 
        except:
            media = [ ]
        return media

class UserPostModelCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    media = serializers.SerializerMethodField(read_only=True)
    post_media = serializers.FileField()

    class Meta:
        model = UserPostModel
        fields = "__all__"
    
    def create(self, validated_data):
        user = get_user_model().objects.get(email = self.context["request"].user.email)
        user_post = UserPostModel.objects.create( 
            user = user,
            title = validated_data["title"],
            description = validated_data["description"],
            category = validated_data["category"],
            sub_category = validated_data["sub_category"])
        post_media_list = self.context["request"].data.getlist("post_media")
        if len(post_media_list) > 0:
            for i in post_media_list:
                instance = UserPostMediaModel.objects.create( 
                    file_field = i 
                )
                user_post.media.add(instance.pk)
                user_post.save()
        return validated_data
    
    def get_likes(self, obj):
        return 1
    
    def get_media(self, obj):
        return 1

# Certificates serializer
class UserCertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCertificatesModel
        fields = "__all__" 

    def create(self, validated_data):
        query = UserCertificatesModel.objects.create(**validated_data)
        userprofile = UserProfileModel.objects.get(user=self.context["request"].user)
        userprofile.certificates.add(query.pk)
        return validated_data

# Resume serializer
class UserResumeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResumeModel
        fields = "__all__"
    
    def create(self, validated_data):
        query = UserResumeModel.objects.create(**validated_data)
        userprofile = UserProfileModel.objects.get(user=self.context["request"].user)
        userprofile.resume.add(query.pk)
        return validated_data

# Address serializer
class UserAddressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddressModel
        fields = "__all__"
    
    def create(self, validated_data):
        query = UserAddressModel.objects.create(**validated_data)
        userprofile = UserProfileModel.objects.get(user=self.context["request"].user)
        userprofile.address.add(query.pk)
        return validated_data

# Education Details serializer
class UserEducationDetailsModelModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEducationDetailsModel
        fields = "__all__"
    
    def create(self, validated_data):
        query = UserEducationDetailsModel.objects.create(**validated_data)
        userprofile = UserProfileModel.objects.get(user=self.context["request"].user)
        userprofile.education.add(query.pk)
        return validated_data

# Experience serializer
class UserExperienceDetailsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExperienceDetailsModel
        fields = "__all__"
    
    def create(self, validated_data):
        query = UserExperienceDetailsModel.objects.create(**validated_data)
        userprofile = UserProfileModel.objects.get(user=self.context["request"].user)
        userprofile.experiences.add(query.pk)
        return validated_data


# Contact Info serializer
class UserContactInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContactInfoModel
        fields = "__all__"
    
    def create(self, validated_data):
        query = UserContactInfoModel.objects.create(**validated_data)
        userprofile = UserProfileModel.objects.get(user=self.context["request"].user)
        userprofile.contact_info.add(query.pk)
        return validated_data


# User Profile Listing Serializer
class UserProfileListSerializer(serializers.ModelSerializer):
    resume = serializers.SerializerMethodField(read_only=True)
    address = serializers.SerializerMethodField(read_only=True)
    education = serializers.SerializerMethodField(read_only=True)
    experiences = serializers.SerializerMethodField(read_only=True)
    contact_info = serializers.SerializerMethodField(read_only=True)
    certificates = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = UserProfileModel
        fields = "__all__"

    def get_certificates(self, obj):
        try:
            data = UserCertificatesSerializer(obj.certificates.all(), many=True).data 
        except:
            data = []
        return data

    def get_contact_info(self, obj):
        try:
            data = UserContactInfoModelSerializer(obj.contact_info.all(), many=True).data 
        except:
            data = []
        return data

    def get_experiences(self, obj):
        try:
            data = UserExperienceDetailsModelSerializer(obj.experiences.all(), many=True).data 
        except:
            data = []
        return data 

    def get_education(self, obj):
        try:
            data = UserEducationDetailsModelModelSerializer(obj.education.all(), many=True).data 
        except:
            data = []
        return data 
    
    def get_address(self, obj):
        try:
            data = UserAddressModelSerializer(obj.address.all(), many=True).data 
        except:
            data = []
        return data 

    def get_resume(self, obj):
        try:
            data = UserResumeModelSerializer(obj.resume.all(), many=True).data
        except:
            data = []
        return data

# User Profile Create Serializer
class UserProfileCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = UserProfileModel
        exclude = ("resume", "address", "education", "experiences", "contact_info", "certificates")

    def create(self, validated_data):
        # user = User
        return validated_data