# Generated by Django 3.0.5 on 2020-05-15 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_auto_20200515_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectpropertyoption',
            name='name',
            field=models.CharField(choices=[('Жила площа', 'Квартира')], max_length=50, verbose_name='Назва'),
        ),
    ]