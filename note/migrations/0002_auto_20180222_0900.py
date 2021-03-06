# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-22 01:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ('FBID', 'NoteTitle', 'NoteContent', 'DateCreated', 'Status')},
        ),
        migrations.AddField(
            model_name='note',
            name='Status',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='note',
            name='FBID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Notes', to='fbuser.FBUser'),
        ),
    ]
