# Generated by Django 4.2 on 2023-05-16 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0003_alter_card_date_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Başlık'),
        ),
    ]
