# Generated by Django 4.1.3 on 2022-12-03 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0002_pet_group"),
        ("traits", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="trait",
            name="pets",
            field=models.ManyToManyField(related_name="traits", to="pets.pet"),
        ),
    ]
