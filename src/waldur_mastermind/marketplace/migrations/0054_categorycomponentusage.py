# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-22 16:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('marketplace', '0053_add_category_component'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryComponentUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('date', models.DateField()),
                ('reported_usage', models.PositiveIntegerField(null=True)),
                ('fixed_usage', models.PositiveIntegerField(null=True)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.CategoryComponent')),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]