# Generated by Django 4.2.7 on 2024-10-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("LearningManagementSystem", "0002_book_members_overduereturn_issue"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="book_id",
            new_name="BookID",
        ),
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="book",
            name="cost",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="book",
            name="name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="book",
            name="status",
            field=models.CharField(max_length=50),
        ),
    ]
