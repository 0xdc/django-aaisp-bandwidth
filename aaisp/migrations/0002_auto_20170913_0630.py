# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 06:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aaisp', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bandwidth',
            unique_together=set([('line', 'time')]),
        ),
    ]