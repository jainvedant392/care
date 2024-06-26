# Generated by Django 2.2.11 on 2020-09-04 04:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0174_auto_20200903_1836"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalpatientregistration",
            name="emergency_phone_number",
            field=models.CharField(
                default="",
                max_length=14,
                validators=[
                    django.core.validators.RegexValidator(
                        code="invalid_mobile",
                        message="Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>",
                        regex="^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$",
                    )
                ],
            ),
        ),
        migrations.AddField(
            model_name="patientregistration",
            name="emergency_phone_number",
            field=models.CharField(
                default="",
                max_length=14,
                validators=[
                    django.core.validators.RegexValidator(
                        code="invalid_mobile",
                        message="Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>",
                        regex="^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$",
                    )
                ],
            ),
        ),
    ]
