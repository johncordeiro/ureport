# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_auto_20150508_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollquestion',
            name='response_type',
            field=models.CharField(help_text='The response type for this question', max_length=1, null=True),
        ),
    ]
