# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-10 08:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0009_auto_20200210_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_photo',
            new_name='profile_pic',
        ),
    ]