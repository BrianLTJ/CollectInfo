# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20)),
                ('phone', models.TextField(max_length=12)),
                ('qq', models.TextField(max_length=12)),
                ('dorm', models.TextField(max_length=50)),
                ('birthday', models.TextField(max_length=50)),
                ('place', models.TextField(max_length=100)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]