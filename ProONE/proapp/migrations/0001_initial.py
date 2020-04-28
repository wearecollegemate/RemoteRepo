# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-04-28 08:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CmtData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmt', models.CharField(max_length=1200)),
                ('cpost', models.CharField(max_length=30)),
                ('cdate', models.DateField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FeedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed', models.CharField(max_length=1200)),
                ('fpost', models.CharField(max_length=30)),
                ('fdate', models.DateField(max_length=100)),
                ('ans', models.CharField(max_length=1200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProData',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('rollno', models.BigIntegerField()),
                ('regno', models.BigIntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50)),
                ('college', models.CharField(max_length=20)),
                ('branch', models.CharField(max_length=20)),
                ('user', models.EmailField(max_length=50)),
                ('pwd', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='images')),
                ('date', models.DateField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StoryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=100)),
                ('story', models.CharField(max_length=1200)),
                ('upost', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='cmtdata',
            name='storydata',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='proapp.StoryData'),
        ),
    ]
