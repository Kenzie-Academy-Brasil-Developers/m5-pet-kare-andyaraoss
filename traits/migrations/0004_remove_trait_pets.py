# Generated by Django 4.1.3 on 2022-12-04 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("traits", "0003_trait_created_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trait",
            name="pets",
        ),
    ]
