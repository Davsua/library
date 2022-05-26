# Generated by Django 3.2 on 2022-05-24 01:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_alter_book_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('782d7461-bdeb-443e-948e-a6af0a2f9787')),
        ),
    ]