# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150727_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_log',
            name='com_time',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='file_log',
            name='status',
            field=models.CharField(default=b'init', max_length=30, blank=True),
        ),
    ]
