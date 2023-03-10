# Generated by Django 4.1.4 on 2023-01-20 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("MakerSpace", "0003_delete_member_space_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Generate",
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
                ("name", models.CharField(db_index=True, max_length=200)),
            ],
            options={
                "verbose_name": "generate",
                "verbose_name_plural": "generates",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="PromptBase",
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
                ("keyword", models.CharField(db_index=True, max_length=200)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="promptbase",
                        to="MakerSpace.generate",
                    ),
                ),
            ],
            options={"ordering": ("category",),},
        ),
    ]
