# Generated by Django 3.2.14 on 2023-05-05 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0037_alter_systembalance_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramadmin',
            name='max_unpaid_value',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='telegramadmin',
            name='unpaid_value',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='telegramadmin',
            name='unpaid_volume',
            field=models.BigIntegerField(default=0),
        ),
    ]
