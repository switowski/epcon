# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-14 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0011_add_stripepayment_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='vototalk',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='vototalk',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]