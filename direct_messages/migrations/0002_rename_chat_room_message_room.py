# Generated by Django 5.1.3 on 2024-12-04 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("direct_messages", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="message",
            old_name="chat_room",
            new_name="room",
        ),
    ]
