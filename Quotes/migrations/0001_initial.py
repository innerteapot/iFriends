# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(max_length=200, verbose_name=b'text')),
                ('by', models.CharField(max_length=50, verbose_name=b'by')),
                ('date', models.DateTimeField(auto_now=True, verbose_name=b'Last Modified')),
            ],
        ),
    ]
