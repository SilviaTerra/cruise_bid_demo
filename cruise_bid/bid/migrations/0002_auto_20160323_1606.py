# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cruise',
            name='bid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
