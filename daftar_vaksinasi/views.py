from django.shortcuts import render, HttpResponse

from .models import *
from .forms import DaftarVaksinasiForm
from .models import *


def index(request):
    return render(request, 'index_daftar_vaksinasi.html')


def summary(request):
    list_of_peserta = PesertaVaksinasi.objects.all()
    user = request.user
    result = PesertaVaksinasi
    for peserta in list_of_peserta:
        if peserta.nama == user.name:
            result = peserta

    response = {'result':result}
    return render(request, 'tiket_vaksinasi.html', response)


def form_peserta_vaksinasi(request):
    peserta_vaksinasi_form = DaftarVaksinasiForm(request.POST or None)
    if peserta_vaksinasi_form.is_valid():
        peserta_vaksinasi_form.save()
        
    response = {'peserta_vaksinasi_form' : peserta_vaksinasi_form}
    return render(request, 'forms.html', response)



def create(request):
    if request.method == 'POST':
        nama = request.POST['nama']
        tanggal_lahir = request.POST['tanggalLahir']
        nik = request.POST['nik']
        alamat_sentra_vaksinasi = request.POST['alamatSentraVaksinasi']
        tanggal_vaksinasi = request.POST['tanggalVaksinasi']
        jam_vaksinasi = request.POST['jamVaksinasi']
        vaksinasi_ke = request.POST['vaksinasiKe']

        new_peserta_vaksinasi = PesertaVaksinasi(nama=nama, tanggal_lahir=tanggal_lahir, nik=nik, alamat_sentra_vaksinasi=alamat_sentra_vaksinasi, tanggal_vaksinasi=tanggal_vaksinasi, jam_vaksinasi=jam_vaksinasi, vaksinasi_ke=vaksinasi_ke)
        new_peserta_vaksinasi.save()

        success = nama + " telah terdaftar sebagai peserta vaksinasi di " + alamat_sentra_vaksinasi
        return HttpResponse(success)
