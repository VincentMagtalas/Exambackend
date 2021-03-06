# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-20 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FBUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FBID', models.CharField(blank=True, default='', max_length=100)),
                ('Name', models.CharField(blank=True, default='', max_length=250)),
                ('Email', models.CharField(blank=True, default='', max_length=250)),
                ('DateRegistered', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('FBID', 'Name', 'Email', 'DateRegistered'),
            },
        ),
    ]
