# Generated by Django 5.1.2 on 2024-11-23 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0010_alter_phonepro_f_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.TextField(max_length=1000)),
                ('b_name', models.TextField(max_length=1000)),
                ('c_name', models.TextField(max_length=1000)),
                ('d_name', models.TextField(max_length=1000)),
                ('e_name', models.TextField(max_length=1000)),
                ('f_name', models.TextField(max_length=1000)),
                ('g_name', models.TextField(max_length=1000)),
                ('h_name', models.TextField(max_length=1000)),
                ('k_name', models.TextField(max_length=1000)),
                ('l_name', models.TextField(max_length=1000)),
                ('m_name', models.TextField(max_length=1000)),
            ],
        ),
    ]