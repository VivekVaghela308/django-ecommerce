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
    

def store(request):
    if request.method == 'POST':
        print("this is first line after post method ")
        store_data = Student() #call to model.py Student class
        store_data.email = request.POST['email']
        store_data.name = request.POST['uname']
        store_data.save()
    return render(request,'store.html')


def storeget(request):
    if request.method == 'GET':
        # store_data = Student()
        email = request.GET.get('email')
        name =  request.GET.get('uname')
        # store_data.save()
        print(name,email)
    return render(request,'storeget.html')

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


def register(request):
    if request.method == 'POST':
        sign_up = Registration(email = request.POST['email'],
                               name = request.POST['name'], 
                               mob = request.POST['mob'],
                               add = request.POST['add'],
                               password = request.POST['password'])
        sign_up.save()
        return render(request,'register.html',{'registration':"Registrations Successfull."})    
    else:
        return render(request,'register.html')
