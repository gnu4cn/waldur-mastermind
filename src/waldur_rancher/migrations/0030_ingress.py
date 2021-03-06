# Generated by Django 2.2.13 on 2020-08-25 11:38

import django.contrib.postgres.fields.jsonb
import django.db.models.deletion
import django.utils.timezone
import django_fsm
import model_utils.fields
from django.db import migrations, models

import waldur_core.core.fields
import waldur_core.core.models
import waldur_core.core.shims
import waldur_core.core.validators
import waldur_core.structure.models


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('structure', '0012_customer_sponsor_number'),
        ('waldur_rancher', '0029_application'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingress',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'created',
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='created',
                    ),
                ),
                (
                    'modified',
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='modified',
                    ),
                ),
                (
                    'description',
                    models.CharField(
                        blank=True, max_length=500, verbose_name='description'
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        max_length=150,
                        validators=[waldur_core.core.validators.validate_name],
                        verbose_name='name',
                    ),
                ),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('error_message', models.TextField(blank=True)),
                (
                    'runtime_state',
                    models.CharField(
                        blank=True, max_length=150, verbose_name='runtime state'
                    ),
                ),
                (
                    'state',
                    django_fsm.FSMIntegerField(
                        choices=[
                            (5, 'Creation Scheduled'),
                            (6, 'Creating'),
                            (1, 'Update Scheduled'),
                            (2, 'Updating'),
                            (7, 'Deletion Scheduled'),
                            (8, 'Deleting'),
                            (3, 'OK'),
                            (4, 'Erred'),
                        ],
                        default=5,
                    ),
                ),
                ('backend_id', models.CharField(blank=True, max_length=255)),
                (
                    'rules',
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=list
                    ),
                ),
                (
                    'cluster',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='waldur_rancher.Cluster',
                    ),
                ),
                (
                    'namespace',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='waldur_rancher.Namespace',
                    ),
                ),
                (
                    'rancher_project',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='waldur_rancher.Project',
                    ),
                ),
                (
                    'service_project_link',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='+',
                        to='waldur_rancher.RancherServiceProjectLink',
                    ),
                ),
                (
                    'settings',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='+',
                        to='structure.ServiceSettings',
                    ),
                ),
                (
                    'tags',
                    waldur_core.core.shims.TaggableManager(
                        blank=True,
                        help_text='A comma-separated list of tags.',
                        related_name='ingress_ingress_waldur_rancher',
                        through='taggit.TaggedItem',
                        to='taggit.Tag',
                        verbose_name='Tags',
                    ),
                ),
            ],
            options={'abstract': False,},
            bases=(
                waldur_core.core.models.DescendantMixin,
                waldur_core.core.models.BackendModelMixin,
                waldur_core.structure.models.StructureLoggableMixin,
                models.Model,
            ),
        ),
    ]
