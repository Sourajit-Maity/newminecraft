# Generated by Django 5.0.6 on 2024-09-16 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="feedback",
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
                (
                    "user",
                    models.CharField(max_length=50, unique=True, verbose_name="User"),
                ),
                (
                    "time",
                    models.CharField(max_length=50, unique=True, verbose_name="Time"),
                ),
                ("x", models.CharField(max_length=50, unique=True, verbose_name="X")),
                ("y", models.CharField(max_length=50, unique=True, verbose_name="Y")),
                ("z", models.CharField(max_length=50, unique=True, verbose_name="Z")),
            ],
            options={
                "verbose_name": "Feedback",
                "verbose_name_plural": "Feedback",
                "db_table": "feedback",
                "managed": True,
            },
        ),
    ]
