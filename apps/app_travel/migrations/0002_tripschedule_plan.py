# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_travel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripschedule',
            name='plan',
            field=models.TextField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]
