# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-28 13:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0009_project_is_removed'),
        ('waldur_vmware', '0006_cluster'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerCluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waldur_vmware.Cluster')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.Customer')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='customercluster',
            unique_together=set([('customer', 'cluster')]),
        ),
    ]