# Generated by Django 3.2.14 on 2023-04-11 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0033_auto_20230411_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ip', models.GenericIPAddressField()),
                ('port', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='domain',
            name='node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domains', to='user.node'),
        ),
    ]
