# Generated by Django 3.0.6 on 2020-07-07 13:14

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('property', '0030_auto_20200526_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectproperty',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_object_total', to=settings.FILER_IMAGE_MODEL, verbose_name='Головне зображення'),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Назва')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Опис')),
                ('meta_description', models.TextField(blank=True, max_length=160, null=True, verbose_name='Мета опис')),
                ('published', models.DateField(auto_now_add=True, db_index=True, verbose_name='Створено')),
                ('menu', models.BooleanField(default=False, verbose_name='Меню')),
                ('footer', models.BooleanField(default=False, verbose_name='Підвал')),
                ('status', models.BooleanField(default=True, verbose_name='Статус')),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_page_total', to=settings.FILER_IMAGE_MODEL, verbose_name='Головне зображення')),
            ],
            options={
                'verbose_name': 'Сторінка',
                'verbose_name_plural': 'Сторінки',
                'ordering': ['-published'],
            },
        ),
    ]
