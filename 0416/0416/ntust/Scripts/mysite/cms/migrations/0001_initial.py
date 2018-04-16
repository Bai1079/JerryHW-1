# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-16 04:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileIntro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=20)),
                ('comment', models.CharField(blank=True, max_length=7000)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Profile')),
            ],
        ),
    ]