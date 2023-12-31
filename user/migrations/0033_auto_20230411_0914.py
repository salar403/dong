# Generated by Django 3.2.14 on 2023-04-11 09:14

import backend.customs.generators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0032_user_sent_warn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminbill',
            name='created_vol',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='domain',
            name='historical_traffic',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='domain',
            name='max_traffic',
            field=models.BigIntegerField(default=214748364800),
        ),
        migrations.AlterField(
            model_name='domain',
            name='reserved_traffic',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='domain',
            name='reset_at',
            field=models.BigIntegerField(default=backend.customs.generators.get_reset_time),
        ),
        migrations.AlterField(
            model_name='domain',
            name='unreservable_traffic',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='domain',
            name='used_traffic',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='telegramadmin',
            name='telegram_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='telegramblacklist',
            name='telegram_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='telegrammessagetrottle',
            name='telegram_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='telegram_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='trafficusage',
            name='timestamp',
            field=models.BigIntegerField(default=backend.customs.generators.current_int_timestamp),
        ),
        migrations.AlterField(
            model_name='trafficusage',
            name='usage',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='unitprice',
            name='price',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='expire_at',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='historical_traffic',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='max_traffic',
            field=models.BigIntegerField(default=26843545600),
        ),
        migrations.AlterField(
            model_name='user',
            name='used_traffic',
            field=models.BigIntegerField(default=0),
        ),
    ]
