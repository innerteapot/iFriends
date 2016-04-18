# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event', models.CharField(max_length=30, verbose_name=b'Event')),
                ('date', models.DateTimeField(verbose_name=b'Date')),
                ('addr', models.CharField(max_length=20, verbose_name=b'IP Address')),
                ('url', models.CharField(max_length=80, verbose_name=b'Url')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]