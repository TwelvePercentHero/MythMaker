# Generated by Django 2.2.5 on 2019-11-12 21:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0008_video_video_comment_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(blank=True, upload_to='videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'wmv', 'mov'])]),
        ),
    ]
