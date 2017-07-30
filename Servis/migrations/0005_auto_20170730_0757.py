# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-30 07:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Servis', '0004_auto_20170729_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='firma',
            name='FirmaMesajDurumu',
            field=models.BooleanField(default=False, verbose_name='Firma Mesaj Durumu'),
        ),
        migrations.AddField(
            model_name='firma',
            name='FirmaMesaji',
            field=models.TextField(blank=True, max_length=250, verbose_name='Firma Mesajı'),
        ),
        migrations.AlterField(
            model_name='firma',
            name='FirmaGuncellemeTarihi',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 30, 7, 57, 49, 49656, tzinfo=utc), verbose_name='Firma Guncelleme Tarihi'),
        ),
        migrations.AlterField(
            model_name='firma',
            name='FirmaKayıtTarihi',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 30, 7, 57, 49, 49474, tzinfo=utc), verbose_name='Firma Kayıt Tarihi'),
        ),
        migrations.AlterField(
            model_name='firma',
            name='FirmaToplamFiyat',
            field=models.CharField(max_length=50, verbose_name='Firma Toplam Fiyat'),
        ),
    ]