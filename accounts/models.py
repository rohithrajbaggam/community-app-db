from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from uuid import uuid1 
from django.contrib.auth import get_user_model
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_employee(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        extra_fields.setdefault('is_staff', True)
        user.is_employee = True 
        return user 

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_employee', True)
        extra_fields.setdefault('is_paid_user', True)
        extra_fields.setdefault('is_instructor', True)
        
        return self.create_user(email, password, **extra_fields) 


# from django.contrib.auth.models import User 
class UserModel(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid1(), editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    
    # Permissions
    is_instructor = models.BooleanField(default=False, null=True, blank=True)
    is_staff = models.BooleanField(default=False, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_employee = models.BooleanField(default=False, null=True, blank=True)
    is_paid_user = models.BooleanField(default=False, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class EmailOtpVerifyModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="EmailOtpVerifyModel_user")
    email = models.CharField(max_length=200, null=True, blank=True)
    otp = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)




