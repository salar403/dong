# Generated by Django 3.2.14 on 2023-06-11 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0046_auto_20230611_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noderate',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vote', to='user.user'),
        ),
    ]