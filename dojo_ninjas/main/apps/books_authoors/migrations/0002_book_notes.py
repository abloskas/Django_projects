# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-22 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authoors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='notes',
            field=models.TextField(default='some string'),
        ),
    ]