# Generated by Django 3.2 on 2022-05-24 01:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0004_alter_book_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('d454c930-d9ec-4e3c-8b8d-1c7de4052186')),
        ),
    ]
