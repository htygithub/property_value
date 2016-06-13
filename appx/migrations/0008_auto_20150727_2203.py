# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150727_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_log',
            name='out_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
