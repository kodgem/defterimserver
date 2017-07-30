# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-29 14:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Servis', '0002_auto_20170729_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firma',
            name='FirmaAktiflik',
            field=models.BooleanField(default=True, verbose_name='Firma Aktiflik'),
        ),
        migrations.AlterField(
            model_name='firma',
            name='FirmaGuncellemeTarihi',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 29, 14, 37, 38, 736805, tzinfo=utc), verbose_name='Firma Guncelleme Tarihi'),
        ),
        migrations.AlterField(
            model_name='firma',
            name='FirmaKayıtTarihi',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 29, 14, 37, 38, 736592, tzinfo=utc), verbose_name='Firma Kayıt Tarihi'),
        ),
    ]