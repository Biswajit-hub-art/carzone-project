# Generated by Django 3.0.7 on 2021-08-20 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20210820_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='team',
            name='facebook_link',
        ),
        migrations.RemoveField(
            model_name='team',
            name='google_plus_link',
        ),
        migrations.RemoveField(
            model_name='team',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='team',
            name='twitter_link',
        ),
    ]
