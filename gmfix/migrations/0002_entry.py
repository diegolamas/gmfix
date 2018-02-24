# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-21 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gmfix', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_id', models.CharField(max_length=200, verbose_name='Entry ID')),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gmfix.Playlist')),
            ],
        ),
    ]
