from django.shortcuts import render
from .models import Hewan
from .forms import inputbinatang
from django.http import HttpResponseRedirect
from django.shortcut import redirect

# Create your views here.
def daftar_binatang(request):
    return render (request, 'daftar_binatang.html',{})

def listHewan(request):
    list_hewan= Hewan.objects.all()
    return render(request, 'daftar_binatang.html',{'list_hewan':list_hewan})

def listHewan2(request):
    list_hewan= Hewan.objects.all()
    return render(request, 'binatang.html',{'list_hewan':list_hewan})

def listHewan3(request):
    if request.method == 'POST':
        form = inputbinatang(request.POST)
        if form.is_valid():
            post =form.save(commit=False)
            post.save()
    else:
        form = inputbinatang()
    return render(request, 'input_binatang.html',{'form':form})

def listHewan4(request):
    list_hewan= Hewan.objects.all()
    if request.method == 'POST':
        form = inputbinatang(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            return HttpResponseRedirect('')
    else:
        form = inputbinatang()
    return render(request, 'binatangbinatang.html',{'list_hewan':list_hewan,'form':form})
    
