# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('People', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('opinion', models.CharField(max_length=50, verbose_name=b'Opinion')),
                ('votes', models.IntegerField(verbose_name=b'Vote Count')),
            ],
        ),
        migrations.CreateModel(
            name='UserPoll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=100, verbose_name=b'Question')),
                ('date', models.DateTimeField(verbose_name=b'Creation Date')),
                ('person', models.ForeignKey(to='People.Person')),
            ],
        ),
        migrations.AddField(
            model_name='opinion',
            name='poll',
            field=models.ForeignKey(to='Poll.UserPoll'),
        ),
    ]
