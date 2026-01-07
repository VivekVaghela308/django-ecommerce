from django.shortcuts import *
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



def register(request):
    if request.method == 'POST':
        sign_up = Registration(email = request.POST['email'],
                               name = request.POST['name'], 
                               mob = request.POST['mob'],
                               add = request.POST['add'],
                               password = request.POST['password'])
        already_reg = Registration.objects.filter(email = request.POST['email'])
        if already_reg:
            return render(request,'register.html',{'already':"Email already exictas..."})  
        else:
            sign_up.save()
            return render(request,'register.html',{'registration':"Registrations Successfull."})    
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        try:
            is_present = Registration.objects.get(email = request.POST['email']) #check Reg table data 
            if is_present:
                if request.POST['password'] == is_present.password:
                   request.session['login'] = is_present.email
                   return redirect('index')
                else:
                    return render(request,'login.html',{'wrong_pass':"password is incorrect..."})
        except:
            return render(request,'login.html',{'not_registered':"this email does not exists..."})
    else:
        return render(request,'login.html')



def index(request):
    cat = category.objects.all()
    if 'login' in request.session: #user login is success after to open category
        return render(request,'index.html',{'cat':cat,'logged_in':True})
    else:
        return render(request,'index.html',{'cat':cat})

    
def logout(request):
    del request.session['login']
    return redirect('index')
