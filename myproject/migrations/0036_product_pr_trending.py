# Generated by Django 5.1.2 on 2024-11-29 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0035_ts_pr_quanity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pr_trending',
            field=models.BooleanField(default=False, help_text='0-default, 1-Trending'),
        ),
    ]