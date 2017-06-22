# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-06 02:00
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField()),
                ('results', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'classifiers',
            },
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('acronym', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'diseases',
            },
        ),
        migrations.CreateModel(
            name='Mutation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
            ],
            options={
                'db_table': 'mutations',
            },
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('sample_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('age_diagnosed', models.IntegerField()),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Disease')),
            ],
            options={
                'db_table': 'samples',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('random_slugs', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=25), size=None)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(max_length=2048, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='mutation',
            name='sample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mutations', to='api.Sample'),
        ),
        migrations.AddField(
            model_name='classifier',
            name='diseases',
            field=models.ManyToManyField(to='api.Disease'),
        ),
        migrations.AddField(
            model_name='classifier',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
    ]
