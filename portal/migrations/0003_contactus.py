# Generated by Django 4.2.2 on 2023-06-21 16:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portal", "0002_category_name_vid_cont_name_vid_news_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contactus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("phone_num", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=300)),
                ("ad_email", models.EmailField(max_length=300)),
            ],
        ),
    ]
