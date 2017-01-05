# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-05 04:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resolwe_bio', '0004_add_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='modified',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
    ]
