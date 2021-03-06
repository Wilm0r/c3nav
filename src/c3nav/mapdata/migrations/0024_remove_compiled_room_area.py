# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 15:51
from __future__ import unicode_literals

from django.db import migrations


def convert_compiled_room_area_to_location_group_category(apps, schema_editor):
    LocationGroupCategory = apps.get_model('mapdata', 'LocationGroupCategory')
    LocationGroup = apps.get_model('mapdata', 'LocationGroup')

    compiled_room = LocationGroupCategory.objects.create(name='compiled_room', titles={
        'en': 'Compiled room',
        'de': 'Zusammengefügter Raum',
    }, single=True, allow_levels=False, allow_spaces=True, allow_areas=True, allow_pois=False, priority=1)
    LocationGroup.objects.filter(compiled_room=True).update(category=compiled_room)

    compiled_area = LocationGroupCategory.objects.create(name='compiled_area', titles={
        'en': 'Compiled area',
        'de': 'Zusammengefügter Bereich',
    }, single=True, allow_levels=False, allow_spaces=True, allow_areas=True, allow_pois=False, priority=2)
    LocationGroup.objects.filter(compiled_area=True).update(category=compiled_area)


class Migration(migrations.Migration):

    dependencies = [
        ('mapdata', '0023_auto_20170711_1741'),
    ]

    operations = [
        migrations.RunPython(convert_compiled_room_area_to_location_group_category),
        migrations.RemoveField(
            model_name='locationgroup',
            name='compiled_area',
        ),
        migrations.RemoveField(
            model_name='locationgroup',
            name='compiled_room',
        ),
    ]
