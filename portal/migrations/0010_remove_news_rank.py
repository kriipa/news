# Generated by Django 4.2.2 on 2023-07-11 01:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("portal", "0009_vid_cont_rank"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="news",
            name="rank",
        ),
    ]
