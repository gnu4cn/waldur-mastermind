# Generated by Django 1.11.7 on 2018-04-10 07:17
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_squashed_0008'),
    ]

    operations = [
        migrations.RemoveField(model_name='user', name='organization_approved',),
    ]
