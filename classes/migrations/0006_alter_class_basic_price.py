# Generated by Django 3.2.9 on 2021-11-17 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0005_auto_20211117_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='basic_price',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
