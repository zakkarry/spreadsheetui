# Generated by Django 3.0.6 on 2020-05-22 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("spreadsheetui", "0003_auto_20200522_1102"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="blocking_job",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="spreadsheetui.Job",
            ),
        ),
    ]
