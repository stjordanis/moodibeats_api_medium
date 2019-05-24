# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-24 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewVideoDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('video_title', models.TextField(blank=True, null=True)),
                ('video_description', models.TextField(blank=True, null=True)),
                ('predicted_moods', models.CharField(blank=True, max_length=17, null=True)),
            ],
        ),
    ]