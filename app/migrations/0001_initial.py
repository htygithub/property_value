# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docfile', models.FileField(upload_to=b'uploadfile')),
            ],
        ),
        migrations.CreateModel(
            name='file_log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('inp_time', models.DateTimeField(auto_now_add=True)),
                ('out_time', models.DateTimeField()),
                ('com_time', models.DecimalField(max_digits=3, decimal_places=0)),
                ('status', models.CharField(max_length=30, blank=True)),
                ('result_url', models.URLField(blank=True)),
            ],
            options={
                'ordering': ['inp_time'],
            },
        ),
        migrations.CreateModel(
            name='MRAPP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('apptype', models.CharField(max_length=15)),
                ('cmd', models.CharField(max_length=50)),
                ('info_html1', models.TextField(blank=True)),
                ('info_html2', models.TextField(blank=True)),
                ('info_html3', models.TextField(blank=True)),
                ('enable', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('photo', models.URLField(blank=True)),
                ('location', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
