from django.db import models

# Create your models here.
class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=17)
    jabatan = models.CharField(max_length=35)

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=17)
    no_absen = models.PositiveIntegerField()
    nilai_rata_rata = models.FloatField()

class MataPelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=35)
    jadwal_dimulai = models.DateTimeField()
    jadwal_berakhir = models.DateTimeField()
    def __str__(self):
        return self.nama_pelajaran

class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=17)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

class Challenge(models.Model):
    nama_chaleenge = models.CharField(max_length=35)
    banyak_soal = models.PositiveIntegerField()
    bobot_nilai = models.FloatField()
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

class LiveCode(models.Model):
    nama_live_code = models.CharField(max_length=35)
    banyak_soal = models.PositiveIntegerField()
    bobot_nilai = models.FloatField()
    tanggal_pelaksanaan = models.DateField()
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)