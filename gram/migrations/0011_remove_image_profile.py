# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-10 08:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0010_auto_20200210_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='profile',
        ),
    ]
