# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-15 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180615_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='aadhar_no',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Aadhar No.'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='acertificate',
            field=models.FileField(default=None, null=True, upload_to='aadhar', verbose_name='Upload Aadhar Card '),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bcertificate',
            field=models.FileField(default=None, null=True, upload_to='blind', verbose_name='Upload Blind Identity Certificate'),
        ),
    ]
