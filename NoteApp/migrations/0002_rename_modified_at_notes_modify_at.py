# Generated by Django 5.0.4 on 2024-04-08 05:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("NoteApp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="notes",
            old_name="modified_at",
            new_name="modify_at",
        ),
    ]