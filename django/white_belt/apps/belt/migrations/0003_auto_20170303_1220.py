# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 20:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0002_auto_20170303_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='freind',
        ),
        migrations.AddField(
            model_name='friend',
            name='friends',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friend', to='belt.User'),
        ),
    ]
