# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-09 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0005_image_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='comments',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
