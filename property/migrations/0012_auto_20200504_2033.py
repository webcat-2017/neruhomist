# Generated by Django 3.0.5 on 2020-05-04 17:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20200504_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='phone_1',
            field=models.CharField(error_messages={'invalid': 'некоректний формат телефону'}, max_length=30, validators=[django.core.validators.RegexValidator(regex='^[0-9]{10}$')], verbose_name='Телефон №1'),
        ),
    ]
