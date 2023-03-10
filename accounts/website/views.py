from rest_framework import generics, status, permissions, authentication
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, ForgotPasswordSendEmailOtpVerifySerializer, ForgotPasswordEmailOTPVerifySerializer, ChangePasswordWithEmailVerificationSerializer, ChangePasswordWithOldPasswordSerializer
from django.contrib.auth import get_user_model
from accounts.models import EmailOtpVerifyModel

class UserRegistrationAPIView(generics.GenericAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "User Registred Successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserForgotPasswordSendEmailOTPAPIView(generics.GenericAPIView):
    queryset = EmailOtpVerifyModel.objects.all()
    serializer_class = ForgotPasswordSendEmailOtpVerifySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "OTP sent successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserForgotPasswordEmailOTPVerifyAPIView(generics.GenericAPIView):
    queryset = EmailOtpVerifyModel.objects.all()
    serializer_class = ForgotPasswordEmailOTPVerifySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({"message" : "OTP verified successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordWithEmailVerificationAPIView(generics.GenericAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = ChangePasswordWithEmailVerificationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "Password Updated Successfully !"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordWithOldPasswordAPIView(generics.GenericAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = ChangePasswordWithOldPasswordSerializer
    permission_classes = [permissions.IsAuthenticated]
    authenticate_class = [authentication.SessionAuthentication, authentication.BasicAuthentication,
                          authentication.TokenAuthentication]

    

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={"request" : request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "Password Updated Successfully !"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 