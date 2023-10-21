# Generated by Django 3.2.14 on 2023-06-12 07:30

import backend.customs.generators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0048_alter_noderate_node'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoutineTiming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField()),
                ('timestamp', models.BigIntegerField(default=backend.customs.generators.current_int_timestamp)),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timings', to='user.node')),
            ],
        ),
    ]
