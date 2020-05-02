# Generated by Django 2.2.12 on 2020-05-02 21:15

from django.db import migrations
from django.db.migrations import RunPython


def forward(apps, schema_editor):
    # noinspection PyPep8Naming
    Profile = apps.get_model("users", "Profile")
    for profile in Profile.objects.filter(user__isnull=True).iterator():
        # How do we recognize that there could be a dupe?
        # - Username match from fid and handle?
        # If dupe found:
        # - Do a remote lookup. Check id and guid
        # If found profiles match:
        # - Choose the older version
        # - Re-assign all content
        # - Re-assign followers and following
        # - Set fid or guid, depending on which is missing
        # - Delete the dupe
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0040_repopulate_profile_private_inbox'),
    ]

    operations = [
        RunPython(forward, RunPython.noop)
    ]