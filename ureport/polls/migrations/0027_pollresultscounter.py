# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0014_auto_20150722_1419'),
        ('polls', '0026_pollresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollResultsCounter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ruleset', models.CharField(max_length=36)),
                ('type', models.CharField(max_length=255)),
                ('count', models.IntegerField(default=0, help_text='Number of items with this counter')),
                ('org', models.ForeignKey(related_name='results_counters', to='orgs.Org')),
            ],
        ),
    ]
