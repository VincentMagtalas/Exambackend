# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-20 01:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fbuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NoteTitle', models.CharField(blank=True, default='', max_length=100)),
                ('NoteContent', models.TextField()),
                ('DateCreated', models.DateTimeField(auto_now_add=True)),
                ('FBID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='fbuser.FBUser')),
            ],
            options={
                'ordering': ('FBID', 'NoteTitle', 'NoteContent', 'DateCreated'),
            },
        ),
    ]
