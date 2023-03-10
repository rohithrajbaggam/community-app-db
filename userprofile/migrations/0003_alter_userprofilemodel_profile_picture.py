# Generated by Django 4.1.7 on 2023-03-10 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0002_remove_userprofilemodel_contact_info_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofilemodel",
            name="profile_picture",
            field=models.FileField(
                blank=True, null=True, upload_to="media/user_profile/resumes/"
            ),
        ),
    ]
