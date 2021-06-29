# Generated by Django 3.0.5 on 2020-05-26 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0025_auto_20200516_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='link_facebook',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Посилання Facebook'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='link_instagram',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Посилання Instagram'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='link_telegram',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Посилання Telegram'),
        ),
    ]