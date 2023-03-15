from rest_framework import generics, status, permissions, authentication, pagination
from rest_framework.response import Response
from userprofile.models import UserProfileModel, UserResumeModel, UserContactInfoModel, UserExperienceDetailsModel, UserEducationDetailsModel, UserAddressModel, UserCertificatesModel, UserPostModel
from .serializers import UserProfileCreateSerializer, UserProfileListSerializer, UserResumeModelSerializer, UserAddressModelSerializer, UserEducationDetailsModelModelSerializer, UserExperienceDetailsModelSerializer, UserContactInfoModelSerializer, UserCertificatesSerializer, UserPostModelCreateSerializer, UserPostModelImageSerializer
from myprofile.models import UserCategoryInterestModel

# User Post List/Create APIView
class UserPostModelCreateAPIView(generics.GenericAPIView):
    queryset = UserPostModel.objects.all()
    serializer_class = UserPostModelCreateSerializer
    # pagination_class = [pagination.LimitOffsetPagination]
    permission_classes = [permissions.IsAuthenticated]
    authenticate_class = [authentication.SessionAuthentication, authentication.BasicAuthentication,
                          authentication.TokenAuthentication]

    # def list(self, request, *args, **kwargs):
    #     serializer = UserPostModelImageSerializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True)
    #     return self.get_paginated_response(serializer.data)

    # def list(self, request):
    #     quersey = self.queryset.filter(user=request.user)
    #     serializer = UserPostModelImageSerializer(quersey, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

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

# User's homepage view Posts
class UserPostModelHomePageListAPIView(generics.ListAPIView):
    queryset = UserPostModel.objects.all()
    serializer_class = UserPostModelImageSerializer
    # pagination_class = [pagination.LimitOffsetPagination]
    permission_classes = [permissions.IsAuthenticated]
    authenticate_class = [authentication.SessionAuthentication, authentication.BasicAuthentication,
                          authentication.TokenAuthentication]

    def get_queryset(self):
        user_category_instance = UserCategoryInterestModel.objects.get(user=self.request.user)
        category_instance = user_category_instance.category.all()
        
        category_id_list = []
        for i in category_instance:
            category_id_list.append(i.pk)
        return self.queryset.filter(category__in=category_id_list)

# Login User's Posts List Api
class UserPostModelListAPIView(generics.ListAPIView):
    queryset = UserPostModel.objects.all()
    serializer_class = UserPostModelImageSerializer
    # pagination_class = [pagination.LimitOffsetPagination]
    permission_classes = [permissions.IsAuthenticated]
    authenticate_class = [authentication.SessionAuthentication, authentication.BasicAuthentication,
                          authentication.TokenAuthentication]
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    # def list(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True)
    #     return self.get_paginated_response(serializer.data)

# Adding a new user certification view
class UserCertificatesModelCreateAPIView(generics.GenericAPIView):
    queryset = UserCertificatesModel.objects.all()
    serializer_class = UserCertificatesSerializer
    permission_classes = [permissions.IsAuthenticated]
    authenticate_class = [authentication.SessionAuthentication, authentication.BasicAuthentication,
                          authentication.TokenAuthentication]

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
    permission_classes = [permissions.IsAuthenticated]
    authenticate_class = [authentication.SessionAuthentication, authentication.BasicAuthentication,
                          authentication.TokenAuthentication]

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
    permission_classes = [permissions.IsAuthenticated]
    authenticate_class = [authentication.SessionAuthentication, authentication.BasicAuthentication,
                          authentication.TokenAuthentication]

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
    permission_classes = [permissions.IsAuthenticated]
    authenticate_class = [authentication.SessionAuthentication, authentication.BasicAuthentication,
                          authentication.TokenAuthentication]

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
    permission_classes = [permissions.IsAuthenticated]
    authenticate_class = [authentication.SessionAuthentication, authentication.BasicAuthentication,
                          authentication.TokenAuthentication]

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
    permission_classes = [permissions.IsAuthenticated]
    authenticate_class = [authentication.SessionAuthentication, authentication.BasicAuthentication,
                          authentication.TokenAuthentication]

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
    permission_classes = [permissions.IsAuthenticated]
    authenticate_class = [authentication.SessionAuthentication, authentication.BasicAuthentication,
                          authentication.TokenAuthentication]

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
    permission_classes = [permissions.IsAuthenticated]
    authenticate_class = [authentication.SessionAuthentication, authentication.BasicAuthentication,
                          authentication.TokenAuthentication]

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
    permission_classes = [permissions.IsAuthenticated]
    authenticate_class = [authentication.SessionAuthentication, authentication.BasicAuthentication,
                          authentication.TokenAuthentication]

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
    permission_classes = [permissions.IsAuthenticated]
    authenticate_class = [authentication.SessionAuthentication, authentication.BasicAuthentication,
                          authentication.TokenAuthentication]

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
    permission_classes = [permissions.IsAuthenticated]
    authenticate_class = [authentication.SessionAuthentication, authentication.BasicAuthentication,
                          authentication.TokenAuthentication]

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
    permission_classes = [permissions.IsAuthenticated]
    authenticate_class = [authentication.SessionAuthentication, authentication.BasicAuthentication,
                          authentication.TokenAuthentication]

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


