# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 23:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0002_auto_20170305_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]
