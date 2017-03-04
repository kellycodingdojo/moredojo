# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 01:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=45)),
                ('alias', models.CharField(max_length=45)),
                ('date', models.DateField()),
                ('password', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='friend',
            name='joins',
            field=models.ManyToManyField(related_name='add_freinds', to='belt.User'),
        ),
        migrations.AddField(
            model_name='friend',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_key', to='belt.User'),
        ),
    ]
