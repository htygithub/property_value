# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_file_log_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_log',
            name='User',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
