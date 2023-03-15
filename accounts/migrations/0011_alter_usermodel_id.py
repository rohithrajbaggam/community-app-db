# Generated by Django 4.1.7 on 2023-03-13 09:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0010_alter_usermodel_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermodel",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("ea8d34fa-c17f-11ed-be39-46124d953699"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
