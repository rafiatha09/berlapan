from typing import List
from django.db import models
from django.db.models.lookups import PostgresOperatorLookup
from django.http import response
from django.shortcuts import redirect, render

from .forms import DonorDarahForm
from .models import DonorForm, NamaLayanan


def donorPage(request):
    namaLayanan = NamaLayanan.objects.all()
    response = {'namaLayanan' : namaLayanan}
    return render(request, 'donorpage.html', response)

def layananPage(request) :
    namaLayanan = NamaLayanan.objects.all()
    response = {'namaLayanan' : namaLayanan}
    return render(request, 'layananpage.html', response)

def formPage(request) :
    context ={}
    form = DonorDarahForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('outputform/')
    context['form']= form
    return render(request, "form.html", context)

def hasilFormPage(request) :
    allRelawan = DonorForm.objects.all()
    result = DonorForm
    for relawan in allRelawan :
        if relawan.FullName == 'Salsabila Zahra Chinanti' :
            result = relawan

    response = {'result' : result}
    return render(request, 'outputform.html', response)
