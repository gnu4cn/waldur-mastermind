# Generated by Django 2.2.13 on 2020-10-19 10:18

from django.db import migrations

import waldur_core.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('openstack', '0009_subnet_is_connected'),
    ]

    operations = [
        migrations.AddField(
            model_name='router',
            name='fixed_ips',
            field=waldur_core.core.fields.JSONField(default=list),
        ),
    ]
