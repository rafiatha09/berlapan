from django import forms
from django.db.models import fields
from django.db.models.fields import TimeField, files
from django.forms import widgets

from donordarah.models import DonorForm


class DonorDarahForm(forms.ModelForm):
    class Meta:
        model = DonorForm
        fields = ('FullName', 'BirthDate', 'NIK', 'Goldar', 'Sentra', 'Date','Time')
        
        widgets = {
            'FullName' : forms.TextInput(attrs={'id':'namaForm', 'type':'text', 'class' : 'form-control', 'placeholder' : 'Masukkan Nama Lengkap'}),
            'BirthDate': forms.DateInput(attrs={'id':"tglForm", 'type':'date', 'class' : 'form-control'}),
            'NIK': forms.NumberInput(attrs={'id':'nikForm', 'type':'text', 'class' : 'form-control', 'placeholder' : 'Masukkan NIK'}),
            'Goldar' : forms.Select(attrs={'id':'goldarForm', 'name':'goldar','class':'form-control'}),
            'Sentra' : forms.TextInput(attrs={'id':'sentraForm', 'name':'sentra','class':'form-control'}),
            'Date' : forms.DateInput(attrs={'id':"dateForm", 'type':'date', 'class' : 'form-control'}),
            'Time' : forms.TimeInput(attrs={'id':"timeForm", 'type':'time', 'class' : 'form-control'})
        }
