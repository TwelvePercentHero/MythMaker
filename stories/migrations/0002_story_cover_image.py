# Generated by Django 2.2.5 on 2019-10-28 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to='cover_images'),
        ),
    ]