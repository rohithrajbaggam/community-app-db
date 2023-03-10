# Generated by Django 4.1.7 on 2023-03-10 09:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_alter_usermodel_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermodel",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("eb3959e0-bf29-11ed-bdea-46124d953699"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
