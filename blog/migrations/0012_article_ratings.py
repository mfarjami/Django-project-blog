# Generated by Django 3.2.4 on 2021-08-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_myrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='ratings',
            field=models.ManyToManyField(blank=True, related_name='rating', to='blog.MyRating'),
        ),
    ]
