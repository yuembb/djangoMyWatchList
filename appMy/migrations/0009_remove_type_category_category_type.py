# Generated by Django 4.2 on 2023-05-17 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0008_type_card_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.type', verbose_name='Tür'),
        ),
    ]