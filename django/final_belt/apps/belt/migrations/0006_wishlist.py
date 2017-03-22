# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 00:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0005_product_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('wish_products', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wish_product_key', to='belt.Product')),
                ('wish_users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wish_key', to='belt.User')),
            ],
        ),
    ]