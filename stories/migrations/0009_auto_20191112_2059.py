# Generated by Django 2.2.5 on 2019-11-12 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0008_auto_20191112_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='story_thumbnail',
            field=models.ImageField(blank=True, upload_to='story_thumbnails'),
        ),
    ]
