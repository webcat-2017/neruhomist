# Generated by Django 3.0.5 on 2020-04-28 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20200425_1906'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='setting',
            options={'verbose_name': 'Налаштування'},
        ),
        migrations.AlterField(
            model_name='setting',
            name='phone_1',
            field=models.CharField(max_length=30, verbose_name='Телефон №1'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='pthon_2',
            field=models.CharField(max_length=30, verbose_name='Телефон №1'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='site_image_description',
            field=models.CharField(max_length=50, verbose_name='Текст Зображення №2'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='site_image_title',
            field=models.CharField(max_length=30, verbose_name='Текст Зображення №1'),
        ),
    ]
