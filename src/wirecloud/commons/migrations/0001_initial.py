# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-27 12:20
from __future__ import unicode_literals

from django.apps import apps as global_apps
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0008_alter_user_username_max_length'),
    ]
    if global_apps.is_installed('wirecloud.platform'):
        dependencies.append(('platform', '0015_remove_organization_models'))

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'wirecloud_organization',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='name')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commons.Organization')),
                ('users', models.ManyToManyField(blank=True, related_name='teams', to=settings.AUTH_USER_MODEL, verbose_name='users')),
            ],
            options={
                'db_table': 'wirecloud_team',
                'verbose_name': 'team',
                'verbose_name_plural': 'teams',
            },
        ),
        migrations.AlterUniqueTogether(
            name='team',
            unique_together=set([('organization', 'name')]),
        ),
    ]
