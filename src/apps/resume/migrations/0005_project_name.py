# Generated by Django 3.0.5 on 2020-04-22 20:45

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0004_auto_20200422_2303"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="name",
            field=models.TextField(blank=True, null=True),
        ),
    ]
