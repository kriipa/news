# Generated by Django 4.2.2 on 2023-07-09 01:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portal", "0006_remove_news_comment_delete_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="rank",
            field=models.IntegerField(default=0),
        ),
    ]