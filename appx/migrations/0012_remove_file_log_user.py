# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20150727_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file_log',
            name='User',
        ),
    ]
