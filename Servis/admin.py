from django.contrib import admin
from .models import Firma

# Register your models here.

class FirmaAdmin(admin.ModelAdmin):

    list_display = ["FirmaAdi","FirmaKayıtTarihi","FirmaLisansAnahtari","FirmaLisansSuresi","FirmaAktiflik"]

    class Meta:
        model = Firma

admin.site.register(Firma, FirmaAdmin)