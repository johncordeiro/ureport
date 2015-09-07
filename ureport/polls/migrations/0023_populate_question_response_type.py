# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings

from django.db import models, migrations
from temba import TembaClient


class Migration(migrations.Migration):

    def populate_question_response_type(apps, schema_editor):
        PollQuestion = apps.get_model('polls', "PollQuestion")
        Org = apps.get_model('orgs', "Org")
        host = '%s/api/v1' % settings.API_ENDPOINT

        for org in Org.objects.all():
            temba_client = TembaClient(str(host), org.api_token, user_agent=str("Ureport-migrations"))
            flows = temba_client.get_flows()

            for flow in flows:
                for ruleset in flow.rulesets:
                    PollQuestion.objects.filter(ruleset_uuid=ruleset.uuid).update(response_type=ruleset.response_type)

        # remove questions that no longer have rulesets on rapidpro, polls deactivated
        PollQuestion.objects.filter(response_type=None, poll__is_active=False).delete()

    dependencies = [
        ('polls', '0022_pollquestion_response_type'),
    ]

    operations = [
        migrations.RunPython(populate_question_response_type)
    ]
