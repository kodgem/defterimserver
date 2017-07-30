from django.shortcuts import render,HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import *
from .models import Firma

# Create your views here.

@api_view(['GET', 'POST'])
def Firmalar(request):
    if request.method == 'GET':
        firmalar = Firma.objects.all()
        serializer = FirmaSerializer(firmalar, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def FirmaGetir(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        firmaid = data.get('FirmaID')
        firma = Firma.objects.filter(FirmaID=firmaid).first()
        if firma:
            kalangunsayisi = (firma.FirmaLisansBitisTarihi - firma.FirmaLisansBaslangicTarihi).days

            sonucfirma = {
                'FirmaID':firma.FirmaID,
                'FirmaAdi':firma.FirmaAdi,
                'FirmaAktiflik':firma.FirmaAktiflik,
                'FirmaLisansSuresi':firma.FirmaLisansSuresi,
                'FirmaLisansAnahtari':firma.FirmaLisansAnahtari,
                'FirmaMesajDurumu':firma.FirmaMesajDurumu,
                'FirmaMesaj':firma.FirmaMesaji,
                'FirmaLisansKalanGunSayisi':kalangunsayisi
            }
            sonuc_json = {'Sonuc': 'Bsşsrılı', 'KOD': status.HTTP_200_OK, 'Firma':sonucfirma}
            return Response(sonuc_json, status=status.HTTP_200_OK)
        else:
            sonuc_json = {'Sonuc': 'Sonuç Bulunamadı', 'KOD': status.HTTP_404_NOT_FOUND, 'Firma': None}
            return Response(sonuc_json, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def FirmaLisansGir(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        firmaid = data.get('FirmaID')
        firmalisansanahtari = data.get('FirmaLisansAnahtari')

        if firmaid and firmalisansanahtari:
            firma = Firma.objects.filter(FirmaID=firmaid).first()
            if firma:
                if firma.FirmaLisansKayitSayisi < firma.FirmaLisansSayisi:
                    # lisans başarılı
                    firma.FirmaLisansKayitSayisi = firma.FirmaLisansKayitSayisi + 1
                    firma.save()
                    kalangunsayisi = (firma.FirmaLisansBitisTarihi - firma.FirmaLisansBaslangicTarihi).days
                    sonucfirma = {
                        'FirmaID': firma.FirmaID,
                        'FirmaAdi': firma.FirmaAdi,
                        'FirmaAktiflik': firma.FirmaAktiflik,
                        'FirmaLisansSuresi': firma.FirmaLisansSuresi,
                        'FirmaLisansAnahtari': firma.FirmaLisansAnahtari,
                        'FirmaMesajDurumu': firma.FirmaMesajDurumu,
                        'FirmaMesaj': firma.FirmaMesaji,
                        'FirmaLisansKalanGunSayisi': kalangunsayisi
                    }
                    sonucjson = {'Sonuc': 'Başarılı', 'KOD': status.HTTP_200_OK, 'Firma': sonucfirma}
                    return Response(sonucjson)
                else:
                    sonucjson = {'Sonuc': 'Lisans Kayıt Sayısı Dolmuş', 'KOD': status.HTTP_400_BAD_REQUEST,
                                 'Firma': None}
                    return Response(sonucjson)
            else:
                sonucjson = {'Sonuc': 'Firma Bulunamadı', 'KOD': status.HTTP_404_NOT_FOUND,
                             'Firma': None}
                return Response(sonucjson)

        else:
            sonucjson = {'Sonuc': 'Geçersiz Bilgi', 'KOD': status.HTTP_400_BAD_REQUEST, 'Firma': None}
            return Response(sonucjson)