# Generated by Django 3.2.14 on 2023-03-03 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_user_historical_traffic'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='unreservable_traffic',
            field=models.BigIntegerField(default=0),
        ),
    ]
