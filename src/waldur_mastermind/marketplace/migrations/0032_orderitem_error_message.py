# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-06 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0031_plan_component'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='error_message',
            field=models.TextField(blank=True),
        ),
    ]