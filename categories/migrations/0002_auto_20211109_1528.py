# Generated by Django 3.2.9 on 2021-11-09 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
