# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-23 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketusers',
            name='head',
            field=models.ImageField(default='head/memtx.png', upload_to='head/%Y%m'),
        ),
        migrations.AlterField(
            model_name='marketusers',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, '男'), (2, '女')], default=2, verbose_name='性别'),
        ),
    ]
