# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='join',
            field=models.ManyToManyField(related_name='jointravels', to='travel.User'),
        ),
    ]
