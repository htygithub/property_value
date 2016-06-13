# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_file_log_percent'),
    ]

    operations = [
        migrations.AddField(
            model_name='mrapp',
            name='adv_option_html',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='mrapp',
            name='basic_option_html',
            field=models.TextField(blank=True),
        ),
    ]
