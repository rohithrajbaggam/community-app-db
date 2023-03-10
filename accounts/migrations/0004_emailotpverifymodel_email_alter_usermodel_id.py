# Generated by Django 4.1.7 on 2023-03-10 05:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_usermodel_id_emailotpverifymodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="emailotpverifymodel",
            name="email",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="usermodel",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("66070712-bf02-11ed-a3b0-46124d953699"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
