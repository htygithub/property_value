# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150727_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_log',
            name='out_time',
            field=models.DateTimeField(blank=True),
        ),
    ]
