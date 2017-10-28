# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-28 02:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VirginiaPrinting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pdf_location', models.FilePathField()),
            ],
        ),
        migrations.CreateModel(
            name='ImprintRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('sequence_number', models.IntegerField()),
                ('short_title', models.CharField(max_length=200)),
                ('pdf_location', models.FilePathField()),
            ],
        ),
        migrations.CreateModel(
            name='NewspaperCitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('num_variants', models.IntegerField()),
                ('pdf_location', models.FilePathField()),
            ],
        ),
        migrations.CreateModel(
            name='NewspaperHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_location', models.FilePathField()),
                ('newspaper_citation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VirginiaPrinting.NewspaperCitation')),
            ],
        ),
        migrations.DeleteModel(
            name='Record',
        ),
    ]