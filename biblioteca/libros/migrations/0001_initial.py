# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=50)),
                ('editorial', models.CharField(max_length=100)),
                ('ISBN', models.CharField(max_length=32)),
                ('precio', models.IntegerField()),
                ('creado', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]