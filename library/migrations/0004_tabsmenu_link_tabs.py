# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_tabsmenu'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabsmenu',
            name='link_tabs',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
