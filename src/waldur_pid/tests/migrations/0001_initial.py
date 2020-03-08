# Generated by Django 1.11.7 on 2018-03-28 15:49
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Offering',
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
                ('datacite_doi', models.CharField(blank=True, max_length=255)),
            ],
            options={'abstract': False,},
        ),
    ]
