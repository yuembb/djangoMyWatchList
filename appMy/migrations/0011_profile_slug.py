# Generated by Django 4.2 on 2023-06-05 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0010_remove_category_type_type_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Slug'),
        ),
    ]
