# Generated by Django 2.2.5 on 2019-11-07 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0006_story_story_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='story_comment_count',
            field=models.IntegerField(default=0),
        ),
    ]