from django.urls import path

from daftar_vaksinasi.views import *


app_name = 'daftar_vaksinasi'

urlpatterns = [ 
    path('', index, name='index'),
    path('forms/tiket_vaksinasi', summary, name='tiket_vaksinasi'),
    path('forms/', form_peserta_vaksinasi, name='forms'),
]
