from django import forms

from .models import *


class DaftarVaksinasiForm(forms.ModelForm):
    class Meta:
        model = PesertaVaksinasi
        fields = '__all__'
        widgets = {
            'nama' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Masukkan nama Anda'}),
            'tanggal_lahir' : forms.DateInput(attrs={'type' : 'date'}),
            'nik' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Masukkan NIK Anda'}),
            'alamat_sentra_vaksinasi' : forms.Select(attrs={'class':'form-control'})  ,
            'tanggal_vaksinasi': forms.Select(attrs={'class':'form-control'}),
            'jam_tersedia' : forms.Select(attrs={'class':'form-control'}),         
            }