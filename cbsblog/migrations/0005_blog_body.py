# Generated by Django 2.2.3 on 2019-07-09 09:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cbsblog', '0004_remove_blog_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
