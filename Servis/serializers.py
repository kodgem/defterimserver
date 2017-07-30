from rest_framework import serializers
from .models import Firma

class FirmaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Firma
        fields = ('__all__')

class FirmaTekSerializer(serializers.ModelSerializer):

    class Meta:
        model = Firma
        fields = ('FirmaID', 'FirmaAdi', 'FirmaAktiflik', 'FirmaLisansSuresi', 'FirmaLisansAnahtari', 'FirmaMesajDurumu', 'FirmaMesaj')