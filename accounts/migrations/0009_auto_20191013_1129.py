# Generated by Django 2.2.5 on 2019-10-13 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20191009_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='membership_type',
            field=models.CharField(choices=[('FR', 'Free'), ('PR', 'Premium')], max_length=2),
        ),
    ]