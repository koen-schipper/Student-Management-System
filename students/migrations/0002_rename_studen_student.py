# Generated by Django 4.1.2 on 2022-10-09 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Studen",
            new_name="Student",
        ),
    ]
