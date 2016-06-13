# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20150727_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_log',
            name='fname',
            field=models.CharField(max_length=50),
        ),
    ]
