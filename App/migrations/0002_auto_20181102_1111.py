# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-02 11:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='wl',
            new_name='Wheel',
        ),
    ]