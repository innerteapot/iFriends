# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager
from django.conf import settings
import django.contrib.sites.managers


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'Title')),
                ('text', models.TextField(max_length=1024, verbose_name=b'Text')),
                ('date', models.DateTimeField(verbose_name=b'Published')),
                ('sites', models.ManyToManyField(to='sites.Site')),
                ('userID', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager(b'sites')),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'Title')),
                ('text', models.TextField(max_length=1024, verbose_name=b'Text')),
                ('date', models.DateTimeField(verbose_name=b'Published')),
                ('site', models.ForeignKey(to='sites.Site')),
                ('userID', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
    ]
