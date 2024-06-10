# Generated by Django 5.0.4 on 2024-06-02 01:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("CarDriveBk", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuarios",
            name="color",
            field=models.CharField(
                max_length=7,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[0-9A-Fa-f]{6}$", "Enter a valid hex color code"
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="usuarios",
            name="fecha",
            field=models.DateField(null=True),
        ),
    ]
