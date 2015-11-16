# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20151109_1109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='privatetourformmodel',
            old_name='des_guilin',
            new_name='des_other',
        ),
    ]
