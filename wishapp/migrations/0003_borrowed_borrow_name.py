# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishapp', '0002_auto_20170904_0658'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowed',
            name='borrow_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='名称'),
        ),
    ]
