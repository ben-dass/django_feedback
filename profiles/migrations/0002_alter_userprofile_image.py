# Generated by Django 4.2.17 on 2024-12-09 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="image",
            field=models.ImageField(upload_to="images"),
        ),
    ]