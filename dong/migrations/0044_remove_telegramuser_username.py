# Generated by Django 3.2.14 on 2023-06-07 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0043_alter_telegramuser_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telegramuser',
            name='username',
        ),
    ]
