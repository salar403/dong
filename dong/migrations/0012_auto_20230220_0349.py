# Generated by Django 3.2.14 on 2023-02-20 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20230218_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='max_traffic',
            field=models.BigIntegerField(default=214748364800),
        ),
        migrations.AlterField(
            model_name='user',
            name='max_traffic',
            field=models.BigIntegerField(default=26843545600),
        ),
    ]