# Generated by Django 2.2.5 on 2019-10-26 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_auto_20191026_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='uploaded_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
