# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-15 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawl', '0002_auto_20171015_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='price',
            field=models.IntegerField(),
        ),
    ]
