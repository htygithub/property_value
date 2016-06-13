# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_file_log_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_log',
            name='user',
            field=models.CharField(default=b'not set', max_length=20),
        ),
    ]
