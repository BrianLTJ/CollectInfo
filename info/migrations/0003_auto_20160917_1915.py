# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20160917_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='height',
            field=models.TextField(blank=True, default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.TextField(blank=True, default='', max_length=6),
        ),
        migrations.AlterField(
            model_name='person',
            name='size',
            field=models.TextField(blank=True, default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='person',
            name='weight',
            field=models.TextField(blank=True, default='', max_length=10),
        ),
    ]