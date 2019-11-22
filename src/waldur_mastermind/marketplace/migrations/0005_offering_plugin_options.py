# Generated by Django 2.2.7 on 2019-11-21 22:16

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0004_add_scope_for_offering_component'),
    ]

    operations = [
        migrations.AddField(
            model_name='offering',
            name='plugin_options',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Data used by specific plugin, such as credentials and hooks.'),
        ),
    ]
