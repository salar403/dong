# Generated by Django 3.2.14 on 2023-03-03 10:57

import backend.customs.generators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_remove_domain_is_full'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DayCount',
        ),
        migrations.AddField(
            model_name='domain',
            name='reset_at',
            field=models.BigIntegerField(default=backend.customs.generators.get_reset_time),
        ),
    ]