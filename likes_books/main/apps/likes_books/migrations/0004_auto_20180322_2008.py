# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-22 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes_books', '0003_remove_book_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='liked_user',
            field=models.ManyToManyField(related_name='liked_books', to='likes_books.User'),
        ),
    ]
