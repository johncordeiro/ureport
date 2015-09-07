# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0014_auto_20150722_1419'),
        ('polls', '0023_populate_question_response_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flow', models.CharField(max_length=36)),
                ('ruleset', models.CharField(max_length=36)),
                ('contact', models.CharField(max_length=36)),
                ('completed', models.BooleanField()),
                ('category', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=640)),
                ('state', models.CharField(max_length=255, null=True)),
                ('district', models.CharField(max_length=255, null=True)),
                ('org', models.ForeignKey(related_name='poll_results', to='orgs.Org')),
            ],
        ),
    ]
