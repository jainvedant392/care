# Generated by Django 2.2.11 on 2020-03-31 09:50

from django.db import migrations, models
import partial_index


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0053_delete_duplicate_diseases'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddIndex(
            model_name='disease',
            index=partial_index.PartialIndex(fields=['patient', 'disease'], name='facility_di_patient_640ef7_partial', unique=True, where=partial_index.PQ(deleted=False)),
        ),
    ]