# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20151023_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateTourFormModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('des_beijing', models.BooleanField(default=False)),
                ('des_shanghai', models.BooleanField(default=False)),
                ('car', models.CharField(max_length=100)),
                ('departure', models.CharField(max_length=100)),
                ('nights', models.CharField(max_length=100)),
                ('age1', models.BooleanField(default=False)),
                ('age2', models.BooleanField(default=False)),
                ('service1', models.BooleanField(default=False)),
                ('itinerary', models.TextField(max_length=100)),
            ],
        ),
    ]
