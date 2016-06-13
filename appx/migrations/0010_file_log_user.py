# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0009_auto_20150727_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='file_log',
            name='User',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
        ),
    ]
