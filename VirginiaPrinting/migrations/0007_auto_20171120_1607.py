# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-20 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VirginiaPrinting', '0006_auto_20171114_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspapercitation',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newspaperhistory',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newspapercitation',
            name='variant_number',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='newspaperhistory',
            name='lineage_number',
            field=models.CharField(max_length=200),
        ),
    ]
