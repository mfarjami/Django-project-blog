# Generated by Django 3.2.4 on 2021-07-31 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_article_hist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='hist',
            new_name='hits',
        ),
    ]
