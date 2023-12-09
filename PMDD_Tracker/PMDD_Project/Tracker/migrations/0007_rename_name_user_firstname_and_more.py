# Generated by Django 4.2.6 on 2023-12-09 00:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0006_alter_tracker_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='periodtype',
            new_name='lastname',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.AddField(
            model_name='tracker',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Tracker.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tracker',
            name='date',
            field=models.DateField(default=datetime.date(2023, 12, 8)),
        ),
    ]
