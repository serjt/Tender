# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-11 15:00
from __future__ import unicode_literals

from django.db import migrations, models
import simple_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_app', '0011_auto_20160709_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='rulesofincomingky',
            name='image',
            field=models.ImageField(null=True, upload_to=simple_app.models.image_upload_to, verbose_name='\u0421\u04af\u0440\u04e9\u0442'),
        ),
        migrations.AddField(
            model_name='rulesofmigrationky',
            name='image',
            field=models.ImageField(null=True, upload_to=simple_app.models.image_upload_to, verbose_name='\u0421\u04af\u0440\u04e9\u0442'),
        ),
    ]