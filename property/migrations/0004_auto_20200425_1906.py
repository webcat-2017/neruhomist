# Generated by Django 3.0.5 on 2020-04-25 16:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('property', '0003_settings_site'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Settings_site',
            new_name='Setting',
        ),
    ]