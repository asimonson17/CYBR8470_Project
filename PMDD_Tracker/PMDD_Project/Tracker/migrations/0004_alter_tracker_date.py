# Generated by Django 4.2.6 on 2023-11-20 23:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0003_rename_pmddf_pmdd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='date',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000)]),
        ),
    ]
