# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-12 08:30
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0016_image_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_caption',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='followers',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='following',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='no_posts',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile/'),
        ),
    ]
