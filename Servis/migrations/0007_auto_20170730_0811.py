# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-30 08:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Servis', '0006_auto_20170730_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firma',
            name='FirmaGuncellemeTarihi',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 30, 8, 11, 46, 371050, tzinfo=utc), verbose_name='Firma Guncelleme Tarihi'),
        ),
        migrations.AlterField(
            model_name='firma',
            name='FirmaKayıtTarihi',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 30, 8, 11, 46, 370823, tzinfo=utc), verbose_name='Firma Kayıt Tarihi'),
        ),
    ]
