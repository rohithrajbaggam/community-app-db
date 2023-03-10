# Generated by Django 4.1.7 on 2023-03-10 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CompanyAddressModel",
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
            name="CompanyContactInfoModel",
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
                (
                    "contact_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("whatsapp", models.CharField(blank=True, max_length=100, null=True)),
                ("linkedin", models.CharField(blank=True, max_length=200, null=True)),
                ("facebook", models.CharField(blank=True, max_length=200, null=True)),
                ("instagram", models.CharField(blank=True, max_length=200, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="CompanyManagerInfoModel",
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
                ("name", models.CharField(max_length=100)),
                (
                    "designation",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("role", models.CharField(blank=True, max_length=200, null=True)),
                ("gmail", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "contact_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("whatsapp", models.CharField(blank=True, max_length=100, null=True)),
                ("linkedin", models.CharField(blank=True, max_length=200, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="companyMediaModel",
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
                ("title", models.TextField(blank=True, null=True)),
                (
                    "file_field",
                    models.FileField(
                        blank=True, null=True, upload_to="media/advertisement/"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="CompanyDetailsModel",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "company_website",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "address",
                    models.ManyToManyField(
                        blank=True,
                        related_name="CompanyDetailsModel_address",
                        to="company.companyaddressmodel",
                    ),
                ),
                (
                    "contact_info",
                    models.ManyToManyField(
                        blank=True,
                        related_name="CompanyDetailsModel_contact_info",
                        to="company.companycontactinfomodel",
                    ),
                ),
                (
                    "manager_info",
                    models.ManyToManyField(
                        blank=True,
                        related_name="CompanyDetailsModel_manager_info",
                        to="company.companymanagerinfomodel",
                    ),
                ),
                (
                    "media",
                    models.ManyToManyField(
                        blank=True,
                        related_name="CompanyDetailsModel_media",
                        to="company.companymediamodel",
                    ),
                ),
            ],
        ),
    ]
