# Generated by Django 5.1.2 on 2024-12-02 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0047_remove_myphone_pr_id_remove_myphone_pr_quanity'),
    ]

    operations = [
        migrations.AddField(
            model_name='myphone',
            name='pr_quanity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
