# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20150728_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='file_log',
            name='percent',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=0),
        ),
    ]
