# Generated by Django 3.2.14 on 2023-05-05 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0039_auto_20230505_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramadmin',
            name='untrusted',
            field=models.BooleanField(default=False),
        ),
    ]
