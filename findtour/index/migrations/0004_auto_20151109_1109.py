# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_privatetourformmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='privatetourformmodel',
            name='des_chengdu',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='privatetourformmodel',
            name='des_dunhuang',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='privatetourformmodel',
            name='des_guilin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='privatetourformmodel',
            name='des_luoyang',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='privatetourformmodel',
            name='des_urumqi',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='privatetourformmodel',
            name='des_xian',
            field=models.BooleanField(default=False),
        ),
    ]
