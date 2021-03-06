# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-09 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=255, null=True)),
                ('tweet_time', models.DateTimeField()),
                ('user_name', models.CharField(blank=True, max_length=255)),
                ('favorite_count', models.IntegerField()),
                ('retweet_count', models.IntegerField()),
                ('lang', models.CharField(blank=True, max_length=10)),
                ('user_followers_count', models.IntegerField()),
                ('user_screen_name', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
