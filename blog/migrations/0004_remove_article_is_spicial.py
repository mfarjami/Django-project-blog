# Generated by Django 3.2.4 on 2021-07-24 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210724_1011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='is_spicial',
        ),
    ]
