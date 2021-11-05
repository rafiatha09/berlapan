from django.db import models
from django.db.models.fields import CharField, DateField, EmailField, TextField, TimeField, URLField


class NamaLayanan(models.Model) :
    GOLDAR_CHOICES = [  ('A','A'),
                        ('B','B'),
                        ('AB','AB'),
                        ('O','O'),
                        ]
    PROVINSI_CHOICES = [ ('Aceh','Aceh'),
                            ('Sumatera Utara','Sumatera Utara'),
                            ('Sumatera Barat','Sumatera Barat'),
                            ('Riau','Riau'),
                            ('Kepulauan Riau','Kepulauan Riau'),
                            ('Jambi','Jambi'),
                            ('Sumatera Selatan','Sumatera Selatan'),
                            ('Kepulauan Bangka Belitung','Kepulauan Bangka Belitung'),
                            ('Lampung','Lampung'),
                            ('DKI Jakarta','DKI Jakarta'),
                            ('Bengkulu','Bengkulu'),
                            ('Banten','Banten'), 
                            ('Jawa Barat','Jawa Barat'),
                            ('Jawa Tengah','Jawa Tengah'),
                            ('DI Yogyakarta','DI Yogyakarta'),
                            ('Jawa Timur','Jawa Timur'),
                            ('Bali','Bali'),
                            ('Nusa Tenggara Barat','Nusa Tenggara Barat'),
                            ('Nusa Tenggara Timur','Nusa Tenggara Timur'),
                            ('Kalimantan Barat','Kalimantan Barat'),
                            ('Kalimantan Tengah','Kalimantan Tengah'),
                            ('Kalimantan Selatan','Kalimantan Selatan'),
                            ('Kalimantan Timur','Kalimantan Timur'),
                            ('Kalimantan Utara','Kalimantan Utara'),
                            ('Sulawesi Utara','Sulawesi Utara'),
                            ('Gorontalo','Gorontalo'),
                            ('Sulawesi Tengah','Sulawesi Tengah'),
                            ('Sulawesi Barat','Sulawesi Barat'),
                            ('Sulawesi Selatan','Sulawesi Selatan'),
                            ('Sulawesi Tenggara','Sulawesi Tenggara'),
                            ('Maluku','Maluku'),
                            ('Maluku Utara','Maluku Utara'),
                            ('Papua Barat','Papua Barat'),
                            ('Papua','Papua'),
                            ]
    Number = models.IntegerField()
    Name = models.CharField(max_length=30)
    City = models.CharField(max_length=20)
    Province = models.CharField('Provinsi', choices=(PROVINSI_CHOICES), default=1 ,max_length=25)
    Goldar = models.CharField('Golongan Darah', choices=(GOLDAR_CHOICES), default=1 ,max_length=2)
    
class DonorForm(models.Model) :

    GOLDAR_CHOICES = [('Pilih','Pilih'),
                        ('A','A'),
                        ('B','B'),
                        ('AB','AB'),
                        ('O','O'),
                        ]
    FullName = models.CharField('Nama Lengkap', max_length=30)
    BirthDate = models.DateField('Tanggal Lahir')
    NIK = models.CharField('Nomor Induk Kependudukan (NIK)', max_length=16)
    Goldar = models.CharField('Golongan Darah', choices=(GOLDAR_CHOICES), default=1, max_length=5)
    Sentra = models.CharField('Sentra Layanan Donor Darah', max_length=30)
    Date = models.DateField('Tanggal Donor Darah')
    Time = models.TimeField('Waktu Donor Darah')
    