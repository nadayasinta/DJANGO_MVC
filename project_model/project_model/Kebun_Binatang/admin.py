from django.contrib import admin
from .models import Hewan, Kandang, Penjaga, Pengunjung
# Register your models here.

# admin.site.register(Hewan)
# admin.site.register(Kandang)
# admin.site.register(Penjaga)
# admin.site.register(Pengunjung)

@admin.register(Hewan)
class Hewan(admin.ModelAdmin):
    list_display = ('id', 'nama', 'species','berat','umur')
    search_fields = ('id', 'nama', 'species','berat','umur')

@admin.register(Kandang)
class Kandang(admin.ModelAdmin):
    list_display = ('id', 'nama', 'isi_kandang','luas_kandang')
    search_fields = ('id', 'nama', 'isi_kandang','luas_kandang')

@admin.register(Penjaga)
class Penjaga(admin.ModelAdmin):
    list_display = ('id', 'nama', 'no_telepon','jadwal_jaga')
    search_fields = ('id', 'nama', 'no_telepon','jadwal_jaga')

@admin.register(Pengunjung)
class Pengunjung(admin.ModelAdmin):
    list_display = ('id', 'nama', 'no_telepon','hari_berkunjung')
    ordering=('hari_berkunjung',)
    search_fields = ('id', 'nama', 'no_telepon','hari_berkunjung')



