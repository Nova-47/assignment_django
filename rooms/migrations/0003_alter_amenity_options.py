# Generated by Django 5.1.3 on 2024-12-04 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0002_room_name_alter_amenity_description"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="amenity",
            options={"verbose_name_plural": "Amenities"},
        ),
    ]