# Generated by Django 1.11.1 on 2017-11-23 12:48
import django.db.models.deletion
import django.utils.timezone
import django_fsm
import model_utils.fields
from django.conf import settings
from django.db import migrations, models

import waldur_core.core.fields
import waldur_core.core.models
import waldur_core.core.shims
import waldur_core.core.validators
import waldur_core.logging.loggers
import waldur_core.structure.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('structure', '0001_squashed_0054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
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
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('error_message', models.TextField(blank=True)),
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
                ('backend_id', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to=b'jira_attachments')),
            ],
            options={'abstract': False,},
        ),
        migrations.CreateModel(
            name='Comment',
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
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('error_message', models.TextField(blank=True)),
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
                ('backend_id', models.CharField(max_length=255)),
                ('message', models.TextField(blank=True)),
            ],
            options={'abstract': False,},
            bases=(waldur_core.structure.models.StructureLoggableMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Issue',
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
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('error_message', models.TextField(blank=True)),
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
                ('backend_id', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('summary', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('resolution', models.CharField(blank=True, max_length=255)),
                (
                    'priority',
                    models.SmallIntegerField(
                        choices=[
                            (0, b'n/a'),
                            (1, b'Minor'),
                            (2, b'Major'),
                            (3, b'Critical'),
                        ],
                        default=0,
                    ),
                ),
                (
                    'impact',
                    models.SmallIntegerField(
                        choices=[
                            (0, b'n/a'),
                            (
                                1,
                                b'Small - Partial loss of service, one person affected',
                            ),
                            (2, b'Medium - One department or service is affected'),
                            (
                                3,
                                b'Large - Whole organization or all services are affected',
                            ),
                        ],
                        default=0,
                    ),
                ),
                ('status', models.CharField(max_length=255)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('updated_username', models.CharField(blank=True, max_length=255)),
            ],
            options={'abstract': False,},
            bases=(waldur_core.structure.models.StructureLoggableMixin, models.Model),
        ),
        migrations.CreateModel(
            name='JiraService',
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
                ('uuid', waldur_core.core.fields.UUIDField()),
                (
                    'available_for_all',
                    models.BooleanField(
                        default=False,
                        help_text='Service will be automatically added to all customers projects if it is available for all',
                    ),
                ),
                (
                    'customer',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='structure.Customer',
                        verbose_name='organization',
                    ),
                ),
            ],
            options={'abstract': False,},
            bases=(
                waldur_core.core.models.DescendantMixin,
                waldur_core.logging.loggers.LoggableMixin,
                models.Model,
            ),
        ),
        migrations.CreateModel(
            name='JiraServiceProjectLink',
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
            ],
            options={'abstract': False,},
            bases=(
                waldur_core.core.models.DescendantMixin,
                waldur_core.logging.loggers.LoggableMixin,
                models.Model,
            ),
        ),
        migrations.CreateModel(
            name='Project',
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
                ('impact_field', models.CharField(blank=True, max_length=64)),
                ('reporter_field', models.CharField(blank=True, max_length=64)),
                ('default_issue_type', models.CharField(blank=True, max_length=64)),
                (
                    'available_for_all',
                    models.BooleanField(
                        default=False, help_text=b'Allow access to any user'
                    ),
                ),
                (
                    'service_project_link',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='projects',
                        to='waldur_jira.JiraServiceProjectLink',
                    ),
                ),
                (
                    'tags',
                    waldur_core.core.shims.TaggableManager(
                        related_name='+',
                        blank=True,
                        help_text='A comma-separated list of tags.',
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
                waldur_core.logging.loggers.LoggableMixin,
                models.Model,
            ),
        ),
        migrations.AddField(
            model_name='jiraserviceprojectlink',
            name='project',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='structure.Project'
            ),
        ),
        migrations.AddField(
            model_name='jiraserviceprojectlink',
            name='service',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='waldur_jira.JiraService',
            ),
        ),
        migrations.AddField(
            model_name='jiraservice',
            name='projects',
            field=models.ManyToManyField(
                related_name='jira_services',
                through='waldur_jira.JiraServiceProjectLink',
                to='structure.Project',
            ),
        ),
        migrations.AddField(
            model_name='jiraservice',
            name='settings',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='structure.ServiceSettings',
            ),
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='issues',
                to='waldur_jira.Project',
            ),
        ),
        migrations.AddField(
            model_name='issue',
            name='user',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='comments',
                to='waldur_jira.Issue',
            ),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name='attachment',
            name='issue',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='attachments',
                to='waldur_jira.Issue',
            ),
        ),
        migrations.AddField(
            model_name='attachment',
            name='user',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterUniqueTogether(
            name='jiraserviceprojectlink',
            unique_together=set([('service', 'project')]),
        ),
        migrations.AlterUniqueTogether(
            name='jiraservice', unique_together=set([('customer', 'settings')]),
        ),
    ]
