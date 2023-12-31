# Generated by Django 3.2.14 on 2023-07-01 12:07

import backend.customs.generators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0049_routinetiming'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbsenceStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.BigIntegerField(default=backend.customs.generators.current_int_minute)),
                ('node_map', models.JSONField(default=backend.customs.generators.default_dict)),
            ],
        ),
    ]
