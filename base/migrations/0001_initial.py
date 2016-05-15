# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 12:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('visiblity', models.PositiveSmallIntegerField(choices=[(0, b'unknown'), (1, b'public'), (2, b'private'), (3, b'shared')], default=0)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, b'unknown'), (1, b'created'), (2, b'planned'), (3, b'prosessing'), (4, b'postponed'), (5, b'achieved'), (6, b'dropped')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dreamer', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
