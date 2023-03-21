# Generated by Django 4.1.7 on 2023-03-13 05:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0008_alter_usermodel_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermodel",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("cb0b4260-c15d-11ed-b1b1-46124d953699"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]