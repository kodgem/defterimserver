from django.db import models
from django.utils import timezone
# Create your models here.

class Firma(models.Model):
    FirmaID = models.AutoField(primary_key=True)
    FirmaAdi = models.CharField(max_length=250,verbose_name="Firma Adı")
    FirmaEposta = models.CharField(blank=True, verbose_name="Firma Eposta",max_length=250)
    FirmaTelefonu = models.CharField(blank=True, max_length=13,verbose_name="Firma Telefonu")
    FirmaAdresi = models.TextField(blank=True, verbose_name="Firma Adresi")
    FirmaAktiflik = models.BooleanField(default =True,verbose_name="Firma Aktiflik")
    FirmaLisansSuresi = models.IntegerField(null=True,verbose_name="Firma Lisans Süresi")
    FirmaLisansAnahtari = models.CharField(max_length=250, verbose_name="Firma Lisans Anahtarı")
    FirmaLisansBaslangicTarihi = models.DateTimeField(default=timezone.now(),verbose_name="Firma Lisans Başlangıç Tarihi")
    FirmaLisansBitisTarihi = models.DateTimeField(default=timezone.now(),verbose_name="Firma Lisans bitiş Tarihi")
    FirmaKayıtTarihi = models.DateTimeField(default=timezone.now(),verbose_name="Firma Kayıt Tarihi")
    FirmaGuncellemeTarihi = models.DateTimeField(default=timezone.now(),verbose_name="Firma Guncelleme Tarihi")
    FirmaToplamFiyat = models.CharField(verbose_name="Firma Toplam Fiyat", max_length=50)
    FirmaMesajDurumu = models.BooleanField(default=False, verbose_name="Firma Mesaj Durumu")
    FirmaMesaji = models.TextField(blank=True, max_length=250, verbose_name="Firma Mesajı")



