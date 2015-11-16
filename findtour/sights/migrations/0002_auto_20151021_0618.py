# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sights', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='slug',
            field=models.CharField(default=b'none', max_length=32),
        ),
        migrations.AddField(
            model_name='sight',
            name='slug',
            field=models.CharField(default=b'none', max_length=32),
        ),
    ]
