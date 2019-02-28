# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-28 20:27
from __future__ import unicode_literals

from django.db import migrations

def forward(apps, schema_editor):
    Area = apps.get_model('guides','Area')
    for area in [
        'ART: Applications and Real-Time',
        'INT: Internet',
        'OPS: Operations and Management',
        'RTG: Routing',
        'SEC: Security',
        'TSG: Transport',
        "UNKNOWN: I don't know yet",
    ]:
        Area.objects.create(area=area)

def reverse(apps, schema_editor):
    Area.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0006_make_area_a_class'),
    ]

    operations = [
        migrations.RunPython(forward, reverse)
    ]
