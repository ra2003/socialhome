# Generated by Django 2.0.8 on 2019-02-04 19:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0032_make_content_uuid_editable_false'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
