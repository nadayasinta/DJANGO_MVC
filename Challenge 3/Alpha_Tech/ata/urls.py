#urls ata
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='halaman_home'),
    path('blog/',views.blog,name='halaman_blog'),
    path('mentee/',views.mentee,name='halaman_mentee'),
    path('mentor/',views.mentor,name='halaman_mentor'),
    path('author/',views.author,name='halaman_author'),
    path('mentee/input/',views.inputmentee,name='halaman_input_mentee'),
    path('mentor/input/',views.inputmentor,name='halaman_input_mentor'),
    path('blog/input/',views.inputblog,name='halaman_input_blog'),

]
