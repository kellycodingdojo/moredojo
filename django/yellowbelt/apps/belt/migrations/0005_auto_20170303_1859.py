# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 02:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0004_quote_fav_quote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='fav_quote',
        ),
        migrations.AddField(
            model_name='fav',
            name='fav_quote',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fav', to='belt.Quote'),
        ),
    ]
