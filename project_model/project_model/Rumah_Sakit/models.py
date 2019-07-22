from django.db import models

# Create your models here.
class Dokter(models.Model):
    nama = models.CharField(max_length=255)
    no_telepon =  models.CharField(max_length=17)
    bidang =  models.CharField(max_length=50)
    jadwal_praktek = models.DateTimeField()

class Pasien(models.Model):
    nama = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=17)
    alamat = models.TextField()
    keluhan = models.TextField()

class Resep(models.Model):
    nama = models.CharField(max_length=255)
    total_harga = models.PositiveIntegerField()
    kumpulan_obat = models.TextField()

class Obat(models.Model):
    nama = models.CharField(max_length=255)
    kandungan = models.TextField()
    khasiat = models.TextField()
    
