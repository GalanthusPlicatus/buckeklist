# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 08:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dream',
            old_name='visiblity',
            new_name='visibility',
        ),
    ]
