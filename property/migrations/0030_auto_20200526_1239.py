# Generated by Django 3.0.5 on 2020-05-26 09:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0029_auto_20200526_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='base_url',
            field=models.URLField(max_length=50, validators=[django.core.validators.URLValidator(schemes=['http', 'https'])], verbose_name='Головне посилання'),
        ),
    ]