# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratings',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
