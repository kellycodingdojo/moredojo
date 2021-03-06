# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 00:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friend',
            name='friend_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friend',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
