# Generated by Django 4.2 on 2025-01-15 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Post", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="message",
            new_name="content",
        ),
    ]
