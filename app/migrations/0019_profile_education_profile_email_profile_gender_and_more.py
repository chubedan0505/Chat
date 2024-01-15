# Generated by Django 4.2.5 on 2024-01-14 17:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0018_alter_confirmationcode_expiration_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="education",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")],
                max_length=10,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="relationship_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Single", "Single"),
                    ("In a relationship", "In a relationship"),
                    ("Married", "Married"),
                    ("Other", "Other"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="religion",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="confirmationcode",
            name="expiration_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 1, 14, 17, 40, 53, 681044, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]