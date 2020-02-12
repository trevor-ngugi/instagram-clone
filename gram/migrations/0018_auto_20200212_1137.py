# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-12 08:37
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0017_auto_20200212_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_caption',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_name',
            field=models.CharField(blank=True, default='Post', max_length=30),
        ),
        migrations.AlterField(
            model_name='image',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]