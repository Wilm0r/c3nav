# Generated by Django 2.2.8 on 2019-12-24 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapdata', '0078_reports'),
        ('control', '0007_userpermissions_manage_map_updates'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpermissions',
            name='review_all_reports',
            field=models.BooleanField(default=False, verbose_name='can review all reports'),
        ),
        migrations.AddField(
            model_name='userpermissions',
            name='review_group_reports',
            field=models.ManyToManyField(blank=True, limit_choices_to={'access_restriction': None}, related_name='permissions', to='mapdata.LocationGroup', verbose_name='can review reports belonging to'),
        ),
    ]
