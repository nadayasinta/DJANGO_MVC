from django.contrib import admin
from .models import Hewan 
# Register your models here.
# admin.site.register(Hewan)

@admin.register(Hewan)
class Hewan(admin.ModelAdmin):
    list_display = ('id', 'nama', 'species','berat','umur')
    search_fields = ('id', 'nama', 'species','berat','umur')
