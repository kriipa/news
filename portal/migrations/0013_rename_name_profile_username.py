# Generated by Django 4.2.2 on 2023-07-13 09:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("portal", "0012_contact"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="name",
            new_name="username",
        ),
    ]