from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here

def first(Request):
    return HttpResponse("this is my first view..")

def demo(request):
    return render(request,'demo.html')


def style(request):
    return render(request,'style.html')

def show(request):
    data = Student.objects.all()
    print(data)
   # for i in data:
    #    print(i.email)
    return render(request, 'show.html',{'student':data})


def showimg(request):
    dataimg = Img.objects.all()
    return render(request,'showimg.html',{'dataimg':dataimg}) #Dictionary
    

def storeimg(request):
    if request.method == 'POST' and request.FILES:
        store_image = Img()
        store_image.name = request.POST.get('name')
        store_image.image = request.FILES.get('image')
        store_image.save()
    return render(request,'storeimg.html')

def index(request):
    cat = category.objects.all()
    return render(request,'index.html',{'cat':cat})