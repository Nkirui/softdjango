# Generated by Django 2.2.3 on 2019-07-08 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='wewe', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company_owner', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=12)),
                ('about_company', models.CharField(max_length=200)),
            ],
        ),
    ]
