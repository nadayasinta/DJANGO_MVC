from django.contrib import admin
from .models import Mentor, Mentee, Blog

# Register your models here.
# admin.site.register(Mentor)
# admin.site.register(Mentee)
# admin.site.register(Blog)


@admin.register(Mentor)
class Mentor(admin.ModelAdmin):
    list_display = ('id', 'name','position','experience','comment','photo')
    search_fields = ('id', 'name', 'position','experience','comment','photo')

@admin.register(Mentee)
class Mentee(admin.ModelAdmin):
    list_display = ('id', 'name', 'comment','photo')
    search_fields = ('id', 'name', 'comment','photo')

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ('title', 'content', 'date_create','photo')
    search_fields = ('title', 'content', 'date_create','photo')
