# Generated by Django 3.2.14 on 2023-03-03 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_domain_unreservable_traffic'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='historical_traffic',
            field=models.BigIntegerField(default=0),
        ),
    ]
