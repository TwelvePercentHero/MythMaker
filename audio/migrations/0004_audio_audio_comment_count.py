# Generated by Django 2.2.5 on 2019-11-07 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0003_audio_audio_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='audio_comment_count',
            field=models.IntegerField(default=0),
        ),
    ]
