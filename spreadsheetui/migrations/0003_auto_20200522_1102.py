# Generated by Django 3.0.6 on 2020-05-22 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("spreadsheetui", "0002_auto_20200522_0752"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="job",
            name="source_client",
        ),
        migrations.AddField(
            model_name="job",
            name="can_execute",
            field=models.BooleanField(default=False),
        ),
    ]
