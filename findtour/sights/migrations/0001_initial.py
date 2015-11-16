# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'none', max_length=32)),
                ('main_pic', models.CharField(default=b'none', max_length=32)),
                ('description', models.TextField(default=b'none', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Sight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'none', max_length=32)),
                ('city', models.CharField(default=b'none', max_length=32)),
                ('main_pic', models.CharField(default=b'none', max_length=32)),
                ('main_pic_small', models.CharField(default=b'none', max_length=32)),
                ('description', models.TextField(default=b'none', max_length=512)),
                ('area', models.ForeignKey(to='sights.Area')),
            ],
        ),
    ]
