# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-20 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0011_auto_20180420_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='preferred_team',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]