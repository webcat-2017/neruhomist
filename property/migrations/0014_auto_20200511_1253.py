# Generated by Django 3.0.5 on 2020-05-11 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20200511_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='meta_title',
        ),
        migrations.RemoveField(
            model_name='objectproperty',
            name='meta_title',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='meta_title',
        ),
    ]
