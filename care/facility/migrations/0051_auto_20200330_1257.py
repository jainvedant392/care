# Generated by Django 2.2.11 on 2020-03-30 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0050_dailyround'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyround',
            name='other_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dailyround',
            name='physical_examination_info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
