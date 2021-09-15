# Generated by Django 3.0.7 on 2021-08-20 11:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20210820_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='facebook_link',
            field=models.URLField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='google_plus_link',
            field=models.URLField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/%Y/%m/%d/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='twitter_link',
            field=models.URLField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]