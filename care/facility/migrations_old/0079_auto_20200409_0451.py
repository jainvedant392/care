# Generated by Django 2.2.11 on 2020-04-08 23:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0078_auto_20200409_0436"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalpatientregistration",
            name="created_date",
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="historicalpatientregistration",
            name="modified_date",
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="patientregistration",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="patientregistration",
            name="modified_date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
