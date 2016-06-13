# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150726_0506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file_log',
            old_name='name',
            new_name='fname',
        ),
        migrations.AddField(
            model_name='file_log',
            name='MRAPP',
            field=models.ForeignKey(default=1, to='app.MRAPP'),
            preserve_default=False,
        ),
    ]
