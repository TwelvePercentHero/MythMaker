# Generated by Django 2.2.5 on 2019-11-06 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_auto_20191029_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='story_likes',
            field=models.IntegerField(default=0),
        ),
    ]