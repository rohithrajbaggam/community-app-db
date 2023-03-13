from rest_framework import generics, status, permissions, authentication
from rest_framework.response import Response
from userprofile.models import UserProfileModel, UserResumeModel, UserContactInfoModel, UserExperienceDetailsModel, UserEducationDetailsModel, UserAddressModel, UserCertificatesModel
from .serializers import UserProfileCreateSerializer, UserProfileListSerializer, UserResumeModelSerializer, UserAddressModelSerializer, UserEducationDetailsModelModelSerializer, UserExperienceDetailsModelSerializer, UserContactInfoModelSerializer, UserCertificatesSerializer


# Adding a new user certification view
class UserCertificatesModelCreateAPIView(generics.GenericAPIView):
    queryset = UserCertificatesModel.objects.all()
    serializer_class = UserCertificatesSerializer

    def get(self, request):
        user_profile = UserProfileModel.objects.get(user=request.user)
        queryset = user_profile.contact_info.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data, context={"request" : request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message" : "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

# Updating and deleting user Certificate info
class UserCertificatesModelUpdateAPIView(generics.GenericAPIView):
    queryset = UserCertificatesModel.objects.all()
    serializer_class = UserCertificatesModel

    def get(self, request, id):
        try:
            user_profile = UserProfileModel.objects.get(user=request.user)
            if user_profile.user != request.user:
                return Response({"message" : "Only Owner as Permission to edit"}, status=status.HTTP_401_UNAUTHORIZED)
            queryset = user_profile.certificates.all().get(pk=id)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"message" : "please request for a valid Id"}, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, id):
        try:
            user_profile = UserProfileModel.objects.get(user=request.user)
            if user_profile.user != request.user:
                return Response({"message" : "Only Owner as Permission to edit"}, status=status.HTTP_401_UNAUTHORIZED)
            queryset = user_profile.certificates.all().get(pk=id)
            serializer = self.serializer_class(data=request.data,instance=queryset ,context={"request" : request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message" : f"Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            user_profile = UserProfileModel.objects.get(user=request.user)
            if user_profile.user != request.user:
                return Response({"message" : "Only Owner as Permission to edit"}, status=status.HTTP_401_UNAUTHORIZED)
            queryset = user_profile.certificates.all().get(pk=id).delete()
            return Response({"message" : "Deleted Successfully"}, status=status.HTTP_200_OK)
        except:
            return Response({"message" : f"Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)


# Adding a new Contact Info
class UserContactInfoModelCreateAPIView(generics.GenericAPIView):
    queryset = UserContactInfoModel.objects.all()
    serializer_class = UserContactInfoModelSerializer

    def get(self, request):
        user_profile = UserProfileModel.objects.get(user=request.user)
        queryset = user_profile.contact_info.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data, context={"request" : request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message" : "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)


# Updating and deleting Contact Info
class UserContactInfoModelUpdateAPIView(generics.GenericAPIView):
    queryset = UserContactInfoModel.objects.all()
    serializer_class = UserContactInfoModelSerializer

    def get(self, request, id):
        try:
            user_profile = UserProfileModel.objects.get(user=request.user)
            if user_profile.user != request.user:
                return Response({"message" : "Only Owner as Permission to edit"}, status=status.HTTP_401_UNAUTHORIZED)
            queryset = user_profile.contact_info.all().get(pk=id)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"message" : "please request for a valid Id"}, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, id):
        try:
            user_profile = UserProfileModel.objects.get(user=request.user)
            if user_profile.user != request.user:
                return Response({"message" : "Only Owner as Permission to edit"}, status=status.HTTP_401_UNAUTHORIZED)
            queryset = user_profile.contact_info.all().get(pk=id)
            serializer = self.serializer_class(data=request.data,instance=queryset ,context={"request" : request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message" : f"Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            user_profile = UserProfileModel.objects.get(user=request.user)
            if user_profile.user != request.user:
                return Response({"message" : "Only Owner as Permission to edit"}, status=status.HTTP_401_UNAUTHORIZED)
            queryset = user_profile.contact_info.all().get(pk=id).delete()
            return Response({"message" : "Deleted Successfully"}, status=status.HTTP_200_OK)
        except:
            return Response({"message" : f"Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)


# Adding a new Experience
class UserExperienceDetailsModelCreateAPIView(generics.GenericAPIView):
    queryset = UserExperienceDetailsModel.objects.all()
    serializer_class = UserExperienceDetailsModelSerializer

    def get(self, request):
        user_profile = UserProfileModel.objects.get(user=request.user)
        queryset = user_profile.experiences.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data, context={"request" : request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message" : "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

# Updating and deleting the Experience
class UserExperienceDetailsModelUpdateAPIView(generics.GenericAPIView):
    queryset = UserExperienceDetailsModel.objects.all()
    serializer_class = UserExperienceDetailsModelSerializer

    def get(self, request, id):
        try:
            user_profile = UserProfileModel.objects.get(user=request.user)
            if user_profile.user != request.user:
                return Response({"message" : "Only Owner as Permission to edit"}, status=status.HTTP_401_UNAUTHORIZED)
            queryset = user_profile.experiences.all().get(pk=id)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"message" : "please request for a valid Id"}, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, id):
        try:
            user_profile = UserProfileModel.objects.get(user=request.user)
            if user_profile.user != request.user:
                return Response({"message" : "Only Owner as Permission to edit"}, status=status.HTTP_401_UNAUTHORIZED)
            queryset = user_profile.experiences.all().get(pk=id)
            serializer = self.serializer_class(data=request.data,instance=queryset ,context={"request" : request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message" : f"Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            user_profile = UserProfileModel.objects.get(user=request.user)
            if user_profile.user != request.user:
                return Response({"message" : "Only Owner as Permission to edit"}, status=status.HTTP_401_UNAUTHORIZED)
            queryset = user_profile.experiences.all().get(pk=id).delete()
            return Response({"message" : "Deleted Successfully"}, status=status.HTTP_200_OK)
        except:
            return Response({"message" : "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)


# Adding a new Education
class UserEducationDetailsModelCreateAPIView(generics.GenericAPIView):
    queryset = UserEducationDetailsModel.objects.all()
    serializer_class = UserEducationDetailsModelModelSerializer

    def get(self, request):
        user_profile = UserProfileModel.objects.get(user=request.user)
        queryset = user_profile.education.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data, context={"request" : request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message" : "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)


# Updating and deleting the Education
class UserEducationDetailsModelUpdateAPIView(generics.GenericAPIView):
    queryset = UserEducationDetailsModel.objects.all()
    serializer_class = UserEducationDetailsModelModelSerializer

    def get(self, request, id):
        try:
            user_profile = UserProfileModel.objects.get(user=request.user)
            if user_profile.user != request.user:
                return Response({"message" : "Only Owner as Permission to edit"}, status=status.HTTP_401_UNAUTHORIZED)
            queryset = user_profile.education.all().get(pk=id)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"message" : "please request for a valid Id"}, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, id):
        try:
            user_profile = UserProfileModel.objects.get(user=request.user)
            if user_profile.user != request.user:
                return Response({"message" : "Only Owner as Permission to edit"}, status=status.HTTP_401_UNAUTHORIZED)
            queryset = user_profile.education.all().get(pk=id)
            serializer = self.serializer_class(data=request.data,instance=queryset ,context={"request" : request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message" : f"Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            user_profile = UserProfileModel.objects.get(user=request.user)
            if user_profile.user != request.user:
                return Response({"message" : "Only Owner as Permission to edit"}, status=status.HTTP_401_UNAUTHORIZED)
            queryset = user_profile.education.all().get(pk=id).delete()
            return Response({"message" : "Deleted Successfully"}, status=status.HTTP_200_OK)
        except:
            return Response({"message" : "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)






# Adding a new Address
class UserAddressModelCreateAPIView(generics.GenericAPIView):
    queryset = UserAddressModel.objects.all()
    serializer_class = UserAddressModelSerializer

    def get(self, request):
        user_profile = UserProfileModel.objects.get(user=request.user)
        queryset = user_profile.address.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data, context={"request" : request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message" : "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)


# Updating and deleting the Address
class UserAddressModelUpdateAPIView(generics.GenericAPIView):
    queryset = UserAddressModel.objects.all()
    serializer_class = UserAddressModelSerializer

    def get(self, request, id):
        try:
            user_profile = UserProfileModel.objects.get(user=request.user)
            if user_profile.user != request.user:
                return Response({"message" : "Only Owner as Permission to edit"}, status=status.HTTP_401_UNAUTHORIZED)
            queryset = user_profile.address.all().get(pk=id)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"message" : "please request for a valid Id"}, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, id):
        try:
            user_profile = UserProfileModel.objects.get(user=request.user)
            if user_profile.user != request.user:
                return Response({"message" : "Only Owner as Permission to edit"}, status=status.HTTP_401_UNAUTHORIZED)
            queryset = user_profile.address.all().get(pk=id)
            serializer = self.serializer_class(data=request.data,instance=queryset ,context={"request" : request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message" : f"Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            user_profile = UserProfileModel.objects.get(user=request.user)
            if user_profile.user != request.user:
                return Response({"message" : "Only Owner as Permission to edit"}, status=status.HTTP_401_UNAUTHORIZED)
            queryset = user_profile.address.all().get(pk=id).delete()
            return Response({"message" : "Deleted Successfully"}, status=status.HTTP_200_OK)
        except:
            return Response({"message" : "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)




# Adding a new Resume
class UserResumeModelCreateAPIView(generics.GenericAPIView):
    queryset = UserResumeModel.objects.all()
    serializer_class = UserResumeModelSerializer

    def get(self, request):
        user_profile = UserProfileModel.objects.get(user=request.user)
        queryset = user_profile.resume.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data, context={"request" : request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message" : "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

# Updating and deleting the resume
class UserResumeModelUpdateAPIView(generics.GenericAPIView):
    queryset = UserResumeModel.objects.all()
    serializer_class = UserResumeModelSerializer

    def get(self, request, id):
        try:
            user_profile = UserProfileModel.objects.get(user=request.user)
            if user_profile.user != request.user:
                return Response({"message" : "Only Owner as Permission to edit"}, status=status.HTTP_401_UNAUTHORIZED)
            queryset = user_profile.resume.all().get(pk=id)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"message" : "please request for a valid Id"}, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, id):
        try:
            user_profile = UserProfileModel.objects.get(user=request.user)
            if user_profile.user != request.user:
                return Response({"message" : "Only Owner as Permission to edit"}, status=status.HTTP_401_UNAUTHORIZED)
            queryset = user_profile.resume.all().get(pk=id)
            serializer = self.serializer_class(data=request.data,instance=queryset ,context={"request" : request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message" : f"Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            user_profile = UserProfileModel.objects.get(user=request.user)
            if user_profile.user != request.user:
                return Response({"message" : "Only Owner as Permission to edit"}, status=status.HTTP_401_UNAUTHORIZED)
            queryset = user_profile.resume.all().get(pk=id).delete()
            return Response({"message" : "Deleted Successfully"}, status=status.HTTP_200_OK)
        except:
            return Response({"message" : "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

# User Profile GET/PUT request
class UserProfileGenericAPIView(generics.GenericAPIView):
    queryset = UserProfileModel.objects.all()
    serializer_class = UserProfileCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    authenticate_class = [authentication.SessionAuthentication, authentication.BasicAuthentication,
                          authentication.TokenAuthentication]
    def get(self, request):
        quersey = self.queryset.get(user=request.user)
        serializer = UserProfileListSerializer(quersey, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        try:
            query = self.queryset.get(user=request.user)
            serializer = self.serializer_class(data=request.data,instance=query, context={"request" : request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message" : "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request):
        try:
            quersey = self.queryset.get(user=request.user)
            return Response({"message" : "Deleted Successfully"}, status=status.HTTP_200_OK)
        except:
            return Response({"message" : "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)


