from django.conf.urls import url
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Firmalar,FirmaGetir,FirmaLisansGir

app_name = 'rehber'

urlpatterns = [
    url(r'^firmalar/$', Firmalar, name='firmalar'),
    url(r'^firmagetir/$', FirmaGetir, name='firmagetir'),
    url(r'^firmalisansgir/$', FirmaLisansGir, name='firmalisansgir'),
]
