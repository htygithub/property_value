# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_mrapp_shorttext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mrapp',
            name='cmd',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mrapp',
            name='shorttext',
            field=models.CharField(max_length=50),
        ),
    ]
