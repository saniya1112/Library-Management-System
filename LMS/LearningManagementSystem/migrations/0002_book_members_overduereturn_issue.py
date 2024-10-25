# Generated by Django 4.2.7 on 2024-10-25 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("LearningManagementSystem", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                ("book_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
                ("author", models.CharField(max_length=100)),
                ("category", models.CharField(max_length=100)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Available", "Available"),
                            ("Checked Out", "Checked Out"),
                            ("Reserved", "Reserved"),
                        ],
                        default="Available",
                        max_length=12,
                    ),
                ),
                ("cost", models.DecimalField(decimal_places=2, max_digits=8)),
                ("procurement_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Members",
            fields=[
                ("member_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("contact", models.CharField(max_length=15)),
                ("address", models.TextField()),
                ("aadhar", models.CharField(max_length=12, unique=True)),
                ("enroll_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("Active", "Active"), ("Inactive", "Inactive")],
                        default="Active",
                        max_length=8,
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="OverdueReturn",
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
                ("date_of_issue", models.DateField()),
                ("date_of_return", models.DateField()),
                (
                    "fine_per_day",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="LearningManagementSystem.book",
                    ),
                ),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="LearningManagementSystem.members",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Issue",
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
                ("date_of_issue", models.DateField()),
                ("date_of_return", models.DateField(blank=True, null=True)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="LearningManagementSystem.book",
                    ),
                ),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="LearningManagementSystem.members",
                    ),
                ),
            ],
        ),
    ]
