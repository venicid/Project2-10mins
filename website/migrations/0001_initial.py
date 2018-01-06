# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-01-05 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('content', models.TextField(null=True)),
                ('url_image', models.URLField(blank=True, null=True)),
                ('new_choice', models.BooleanField(default=False)),
                ('editors_choice', models.BooleanField(default=False)),
            ],
        ),
    ]
