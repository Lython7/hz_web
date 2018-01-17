# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 10:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Uprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=32, null=True, verbose_name='身份证姓名')),
                ('ucellphone', models.CharField(max_length=11, null=True, verbose_name='手机号码')),
                ('uposition', models.CharField(max_length=32, null=True, verbose_name='工作岗位')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户拓展表',
                'verbose_name_plural': '用户拓展表',
            },
        ),
    ]
