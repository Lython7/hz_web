# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20180115_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_center',
            name='news_image',
            field=models.ImageField(upload_to='index/news_pic', verbose_name='新闻照片'),
        ),
    ]
