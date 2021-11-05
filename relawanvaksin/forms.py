from django import forms
from django.forms import widgets
from .models import Model_relawan_vaksin
#Membuat form Friend form dengan 


class Form_relawan_vaksin(forms.ModelForm) :
    class Meta :
        model = Model_relawan_vaksin
        fields = ('Nama','umur','nomor_ktp','nomor_hp','email','alamat','Peran','Riwayat_nakes','foto')

        widgets= {
            'Nama': forms.TextInput(attrs={'class':'form-control'}),
            'umur': forms.DateInput(attrs={'type':'number','class':'form-control'}),
            'nomor_ktp': forms.TextInput(attrs={'type':'number','class':'form-control'}),
            'nomor_hp': forms.TextInput(attrs={'type':'number','class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'alamat': forms.Textarea(attrs={'class':'form-control'}),
            'Peran': forms.Select(attrs={'class':'form-control'}),
            'Riwayat_nakes': forms.Select(attrs={'class':'form-control'}),
            'foto':  forms.FileInput(attrs={'class':'form-control'}),

        }
