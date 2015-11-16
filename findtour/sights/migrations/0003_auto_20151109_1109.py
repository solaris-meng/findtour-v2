# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sights', '0002_auto_20151021_0618'),
    ]

    operations = [
        migrations.AddField(
            model_name='sight',
            name='opentime',
            field=models.CharField(default=b'none', max_length=32),
        ),
        migrations.AddField(
            model_name='sight',
            name='photos',
            field=models.TextField(default=b'none', max_length=1024),
        ),
        migrations.AddField(
            model_name='sight',
            name='review',
            field=models.TextField(default=b'none', max_length=1024),
        ),
        migrations.AddField(
            model_name='sight',
            name='ticket',
            field=models.CharField(default=b'none', max_length=32),
        ),
        migrations.AddField(
            model_name='sight',
            name='timeforvisit',
            field=models.CharField(default=b'none', max_length=32),
        ),
        migrations.AddField(
            model_name='sight',
            name='tips',
            field=models.TextField(default=b'none', max_length=1024),
        ),
        migrations.AddField(
            model_name='sight',
            name='wiki',
            field=models.CharField(default=b'none', max_length=128),
        ),
        migrations.AlterField(
            model_name='sight',
            name='description',
            field=models.TextField(default=b'none', max_length=2048),
        ),
    ]
