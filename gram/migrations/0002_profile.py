# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-09 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.CharField(max_length=30)),
                ('bio', models.CharField(max_length=30)),
            ],
        ),
    ]
