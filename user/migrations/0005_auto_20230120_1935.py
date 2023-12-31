# Generated by Django 3.2.14 on 2023-01-20 19:35

import backend.customs.generators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_max_traffic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='server',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='user.server'),
        ),
        migrations.AddField(
            model_name='user',
            name='uuid',
            field=models.CharField(default=backend.customs.generators.generate_uuid, max_length=50, null=True),
        ),
    ]
