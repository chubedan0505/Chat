# Generated by Django 4.2.5 on 2023-12-20 17:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]