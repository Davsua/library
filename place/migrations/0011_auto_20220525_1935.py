# Generated by Django 3.2 on 2022-05-26 00:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0010_alter_book_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_item',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='shelf',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='library',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='place.library'),
        ),
        migrations.AlterField(
            model_name='book',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('ce75e58c-61d3-48c6-807f-dbcc490d1431')),
        ),
    ]