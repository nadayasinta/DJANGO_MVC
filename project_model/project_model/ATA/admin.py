from django.contrib import admin
from .models import Direksi, Mentee, Mentor, MataPelajaran, Challenge, LiveCode
# Register your models here.

# admin.site.register(Direksi)
# admin.site.register(Mentee)
# admin.site.register(Mentor)
# admin.site.register(MataPelajaran)
# admin.site.register(Challenge)
# admin.site.register(LiveCode)

@admin.register(Direksi)
class Direksi(admin.ModelAdmin):
    list_display = ('id', 'nama_lengkap', 'no_telepon','jabatan')
    search_fields = ('id', 'nama_lengkap', 'no_telepon','jabatan')

@admin.register(Mentee)
class Mentee(admin.ModelAdmin):
    list_display = ('id','no_absen','nama_lengkap', 'no_telepon','nilai_rata_rata')
    ordering = ('no_absen',)
    search_fields = ('id','no_absen','nama_lengkap', 'no_telepon','nilai_rata_rata')

@admin.register(Mentor)
class Mentor(admin.ModelAdmin):
    list_display = ('id', 'nama_lengkap', 'no_telepon','mata_pelajaran')
    search_fields = ('id', 'nama_lengkap', 'no_telepon','mata_pelajaran')

@admin.register(MataPelajaran)
class MataPelajaran(admin.ModelAdmin):
    list_display = ('id', 'nama_pelajaran', 'jadwal_dimulai','jadwal_berakhir')
    search_fields = ('id', 'nama_pelajaran', 'jadwal_dimulai','jadwal_berakhir')

@admin.register(Challenge)
class Challenge(admin.ModelAdmin):
    list_display = ('id', 'nama_chaleenge', 'banyak_soal','bobot_nilai','mata_pelajaran')
    search_fields = ('id', 'nama_chaleenge', 'banyak_soal','bobot_nilai','mata_pelajaran')

@admin.register(LiveCode)
class LiveCode(admin.ModelAdmin):
    list_display = ('id', 'nama_live_code', 'banyak_soal','bobot_nilai','tanggal_pelaksanaan','mata_pelajaran')
    search_fields = ('id', 'nama_live_code', 'banyak_soal','bobot_nilai','tanggal_pelaksanaan','mata_pelajaran')




