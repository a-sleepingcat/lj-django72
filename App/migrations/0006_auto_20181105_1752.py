# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-05 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_goods_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='potol',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='goods',
            name='total',
            field=models.CharField(max_length=100),
        ),
    ]