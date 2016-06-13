# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150726_0456'),
    ]

    operations = [
        migrations.AddField(
            model_name='mrapp',
            name='OS',
            field=models.CharField(default=b'Linux', max_length=30),
        ),
        migrations.AlterField(
            model_name='mrapp',
            name='shorttext',
            field=models.CharField(max_length=100),
        ),
    ]
