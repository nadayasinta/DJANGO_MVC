from django.urls import path
from . import views 

urlpatterns =[
    path('1/',views.listHewan, name='daftar_binatang'),
    path('2/',views.listHewan2, name='daftar_binatang2'),
    path('3/',views.listHewan3, name='daftar_binatang3'),
    path('4/',views.listHewan4, name='daftar_binatang4')
]