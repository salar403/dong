# Generated by Django 3.2.14 on 2023-04-05 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0031_unitprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sent_warn',
            field=models.BooleanField(default=False),
        ),
    ]
