# Generated by Django 3.2.14 on 2023-01-20 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_delete_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daycount',
            name='last_date',
            field=models.DateField(null=True),
        ),
    ]
