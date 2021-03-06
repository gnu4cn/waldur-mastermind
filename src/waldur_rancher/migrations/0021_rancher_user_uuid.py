# Generated by Django 2.2.10 on 2020-06-05 07:50

import uuid

from django.db import migrations, models

import waldur_core.core.fields


def gen_uuid(apps, schema_editor):
    RancherUser = apps.get_model('waldur_rancher', 'RancherUser')
    for row in RancherUser.objects.all():
        row.uuid = uuid.uuid4().hex
        row.save(update_fields=['uuid'])


class Migration(migrations.Migration):

    dependencies = [
        ('waldur_rancher', '0020_extend_icon_url_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='rancheruser', name='uuid', field=models.UUIDField(null=True),
        ),
        migrations.RunPython(gen_uuid, elidable=True),
        migrations.AlterField(
            model_name='rancheruser',
            name='uuid',
            field=waldur_core.core.fields.UUIDField(),
        ),
        migrations.AlterModelOptions(
            name='rancheruser', options={'ordering': ('user__username',)},
        ),
    ]
