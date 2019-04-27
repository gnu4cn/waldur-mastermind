# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-26 07:49
from __future__ import unicode_literals

from django.db import migrations, models
import waldur_core.core.validators


def fill_resource_name(apps, schema_editor):
    Resource = apps.get_model('marketplace', 'Resource')

    for resource in Resource.objects.all():
        name = resource.attributes.get('name')

        if name:
            resource.name = name
            resource.save()


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0079_orderitem_old_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='name',
            field=models.CharField(default='', max_length=150, validators=[waldur_core.core.validators.validate_name], verbose_name='name'),
            preserve_default=False,
        ),
        migrations.RunPython(fill_resource_name),
    ]
