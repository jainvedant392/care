# Generated by Django 2.2.11 on 2020-03-25 19:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0009_auto_20200325_1908"),
        ("facility", "0024_auto_20200325_0311"),
    ]

    operations = [
        migrations.AddField(
            model_name="ambulance",
            name="new_primary_district",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="primary_ambulances",
                to="users.District",
            ),
        ),
        migrations.AddField(
            model_name="ambulance",
            name="new_secondary_district",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="secondary_ambulances",
                to="users.District",
            ),
        ),
        migrations.AddField(
            model_name="ambulance",
            name="new_third_district",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="third_ambulances",
                to="users.District",
            ),
        ),
        migrations.AddField(
            model_name="facility",
            name="local_body",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="users.LocalBody",
            ),
        ),
        migrations.AddField(
            model_name="facility",
            name="new_district",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="users.District",
            ),
        ),
    ]
