from django.db import models

# Create your models here.
class Hewan(models.Model):
    nama = models.CharField(max_length=255)
    species  = models.CharField(max_length=35)
    berat = models.PositiveIntegerField()
    umur = models.PositiveIntegerField()

class Kandang(models.Model):
    nama = models.CharField(max_length=255)
    isi_kandang = models.CharField(max_length=255)
    luas_kandang = models.PositiveIntegerField()

class Penjaga(models.Model):
    nama = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=17)
    jadwal_jaga = models.DateField()

class Pengunjung(models.Model):
    nama = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=17)
    hari_berkunjung = models.DateField()