# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-09 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simple_app', '0009_auto_20160708_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='translit',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='simple_app.FAQky'),
        ),
        migrations.AddField(
            model_name='hotline',
            name='translit',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='simple_app.HotlineKy'),
        ),
        migrations.AddField(
            model_name='rulesofmigration',
            name='translit',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='simple_app.RulesOfMigrationKy'),
        ),
    ]
