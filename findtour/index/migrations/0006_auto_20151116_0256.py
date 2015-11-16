# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20151115_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='privatetourformmodel',
            old_name='age1',
            new_name='age_18_39',
        ),
        migrations.RenameField(
            model_name='privatetourformmodel',
            old_name='age2',
            new_name='age_40_50',
        ),
        migrations.RenameField(
            model_name='privatetourformmodel',
            old_name='des_beijing',
            new_name='age_51_65',
        ),
        migrations.RenameField(
            model_name='privatetourformmodel',
            old_name='des_chengdu',
            new_name='age_65',
        ),
        migrations.RenameField(
            model_name='privatetourformmodel',
            old_name='des_dunhuang',
            new_name='destinaiton_other',
        ),
        migrations.RenameField(
            model_name='privatetourformmodel',
            old_name='des_luoyang',
            new_name='destination_beijing',
        ),
        migrations.RenameField(
            model_name='privatetourformmodel',
            old_name='des_other',
            new_name='destination_dunhuang',
        ),
        migrations.RenameField(
            model_name='privatetourformmodel',
            old_name='des_shanghai',
            new_name='destination_luoyang',
        ),
        migrations.RenameField(
            model_name='privatetourformmodel',
            old_name='des_urumqi',
            new_name='destination_shanghai',
        ),
        migrations.RenameField(
            model_name='privatetourformmodel',
            old_name='des_xian',
            new_name='destination_urumqi',
        ),
        migrations.RenameField(
            model_name='privatetourformmodel',
            old_name='service1',
            new_name='destination_xian',
        ),
        migrations.AddField(
            model_name='privatetourformmodel',
            name='service_activity',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='privatetourformmodel',
            name='service_advise',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='privatetourformmodel',
            name='service_guide',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='privatetourformmodel',
            name='service_luxury',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='privatetourformmodel',
            name='service_transfer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='privatetourformmodel',
            name='itinerary',
            field=models.TextField(default=b'tmp', max_length=1024),
        ),
    ]
