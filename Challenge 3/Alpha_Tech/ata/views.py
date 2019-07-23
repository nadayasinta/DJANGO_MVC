from django.shortcuts import render
from .models import Mentor, Mentee, Blog
from .forms import Input_Mentor, Input_Mentee, Input_Blog
# from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.

def home(request):
    return render (request, 'home.html',{})

def blog(request):
    list_blog=Blog.objects.all()
    return render (request, 'blog.html',{'list_blog':list_blog})

def mentee(request):
    list_mentee=Mentee.objects.all()
    return render (request, 'mentee.html',{'list_mentee':list_mentee})

def mentor(request):
    list_mentor=Mentor.objects.all()
    return render (request, 'mentor.html',{'list_mentor':list_mentor})

def author(request):
    return render (request, 'author.html',{})


def inputmentor(request):
    if request.method == 'POST':
        form = Input_Mentor(request.POST)
        if form.is_valid():
            post =form.save(commit=False)
            post.save()
            return redirect('halaman_mentor')

    else:
        form = Input_Mentor()
    return render(request, 'input_mentor.html',{'form':form})

def inputmentee(request):
    if request.method == 'POST':
        form = Input_Mentee(request.POST)
        if form.is_valid():
            post =form.save(commit=False)
            post.save()
            return redirect('halaman_mentee')
    else:
        form = Input_Mentee()
    return render(request, 'input_mentee.html',{'form':form})

def inputblog(request):
    if request.method == 'POST':
        form = Input_Blog(request.POST)
        if form.is_valid():
            post =form.save(commit=False)
            post.save()
            return redirect('halaman_blog')
    else:
        form = Input_Blog()
    return render(request, 'input_blog.html',{'form':form})
