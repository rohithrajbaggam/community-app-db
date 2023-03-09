# Generated by Django 4.1.7 on 2023-02-23 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserAddressModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address_1", models.CharField(blank=True, max_length=500, null=True)),
                ("address_2", models.CharField(blank=True, max_length=500, null=True)),
                ("pincode", models.CharField(blank=True, max_length=10, null=True)),
                ("city", models.CharField(blank=True, max_length=500, null=True)),
                ("state", models.CharField(blank=True, max_length=500, null=True)),
                ("country", models.CharField(blank=True, max_length=500, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserContactInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("gmail", models.CharField(blank=True, max_length=200, null=True)),
                ("whatsapp", models.CharField(blank=True, max_length=20, null=True)),
                ("linkedin", models.CharField(blank=True, max_length=200, null=True)),
                ("facebook", models.CharField(blank=True, max_length=200, null=True)),
                ("instagram", models.CharField(blank=True, max_length=200, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserEducationDetailsModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "university_name",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("degree", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "percentage",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("start_date", models.DateField(blank=True, null=True)),
                ("end_date", models.DateField(blank=True, null=True)),
                ("is_pursuing", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserExperienceDetailsModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "designation",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("role", models.CharField(blank=True, max_length=500, null=True)),
                ("technology", models.CharField(blank=True, max_length=500, null=True)),
                ("start_date", models.DateField(blank=True, null=True)),
                ("end_date", models.DateField(blank=True, null=True)),
                ("currently_working", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserProfileModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "profile_picture",
                    models.FileField(upload_to="media/user_profile/resumes/"),
                ),
                ("first_name", models.CharField(blank=True, max_length=100, null=True)),
                ("last_name", models.CharField(blank=True, max_length=100, null=True)),
                ("bio", models.TextField(blank=True, null=True)),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("MALE", "MALE"),
                            ("FEMALE", "FEMALE"),
                            ("OTHER", "OTHER"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                ("resume", models.FileField(upload_to="media/user_profile/resumes/")),
                (
                    "cover_letter",
                    models.FileField(upload_to="media/user_profile/cover_letter/"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "address",
                    models.ManyToManyField(
                        blank=True,
                        related_name="UserProfileModel_address",
                        to="userprofile.useraddressmodel",
                    ),
                ),
                (
                    "contact_info",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="UserProfileModel_contact_info",
                        to="userprofile.usercontactinfo",
                    ),
                ),
                (
                    "education",
                    models.ManyToManyField(
                        blank=True,
                        related_name="UserProfileModel_education",
                        to="userprofile.usereducationdetailsmodel",
                    ),
                ),
                (
                    "experiences",
                    models.ManyToManyField(
                        blank=True,
                        related_name="UserProfileModel_experiences",
                        to="userprofile.userexperiencedetailsmodel",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="UserProfileModel_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]