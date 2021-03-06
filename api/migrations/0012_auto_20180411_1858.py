# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-04-11 18:58
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20180411_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='chromosome',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='gene_type',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='gene',
            name='symbol',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='gene',
            name='synonyms',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None),
        ),
    ]
