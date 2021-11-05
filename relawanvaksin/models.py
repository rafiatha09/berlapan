from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Model_relawan_vaksin(models.Model) :
    # Model untuk pendaftaran relawan vaksin
    Pilihan_peran_relawan_vaksin = [('Vaksinator','Vaksinator'),
    ('Screening','Screening'),
    ('Registrasi', 'Registrasi'),
    ('Pelaporan', 'Pelaporan'),
    ]

    Pilihan_nakes = [('Yes','Yes'),
    ('No','No'),
    ]
    Nama = models.CharField('Nama Lengkap', max_length=30)
    umur = models.IntegerField('Umur',)
    nomor_hp =  models.IntegerField('Nomor Hp')
    nomor_ktp = models.IntegerField('Nomor Ktp')
    email = models.EmailField(max_length=30)

    foto = models.ImageField(upload_to='images/', blank=True)

    alamat = models.TextField('Alamat domisili')

    
    Riwayat_nakes = models.CharField('Apakah Anda Seorang Nakes?',choices= Pilihan_nakes
    , max_length=30)
    
    Peran = models.CharField('Apa peran yang Anda inginkan?',choices= Pilihan_peran_relawan_vaksin,max_length=30)

    def __str__(self):
        return str(self.pk)
