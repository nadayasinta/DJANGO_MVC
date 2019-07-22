from django.contrib import admin
from .models import Dokter,Pasien,Resep,Obat
# Register your models here.

# admin.site.register(Dokter)
# admin.site.register(Pasien)
# admin.site.register(Resep)
# admin.site.register(Obat)

@admin.register(Dokter)
class Dokter(admin.ModelAdmin):
    list_display = ('id', 'nama', 'no_telepon','bidang','jadwal_praktek')
    search_fields = ('id', 'nama', 'no_telepon','bidang','jadwal_praktek')

@admin.register(Pasien)
class Pasien(admin.ModelAdmin):
    list_display = ('id', 'nama', 'no_telepon','alamat','keluhan')
    search_fields = ('id', 'nama', 'no_telepon','alamat','keluhan')

@admin.register(Resep)
class Resep(admin.ModelAdmin):
    list_display = ('id', 'nama', 'total_harga','kumpulan_obat')
    search_fields = ('id', 'nama', 'total_harga','kumpulan_obat')

@admin.register(Obat)
class Obat(admin.ModelAdmin):
    list_display = ('id', 'nama', 'kandungan','khasiat')
    search_fields = ('id', 'nama', 'kandungan','khasiat')