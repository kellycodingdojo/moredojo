# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 04:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0006_auto_20170303_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fav',
            name='fav_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fav_users', to='belt.User'),
        ),
    ]
