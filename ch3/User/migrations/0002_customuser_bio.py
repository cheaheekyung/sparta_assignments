# Generated by Django 4.2 on 2025-01-14 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="bio",
            field=models.TextField(blank=True, null=True),
        ),
    ]
