# Generated by Django 1.11.7 on 2017-12-28 20:40
import django.db.models.deletion
from django.db import migrations, models

import waldur_core.core.fields
import waldur_core.core.models
import waldur_core.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0001_squashed_0054'),
        ('waldur_jira', '0006_add_parent_for_subtask'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
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
                ('icon_url', models.URLField(blank=True, verbose_name='icon url')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                ('backend_id', models.CharField(db_index=True, max_length=255)),
                (
                    'settings',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='+',
                        to='structure.ServiceSettings',
                    ),
                ),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Priority',
                'verbose_name_plural': 'Priorities',
            },
            bases=(waldur_core.core.models.BackendModelMixin, models.Model),
        ),
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='waldur_jira.Priority'
            ),
        ),
    ]
