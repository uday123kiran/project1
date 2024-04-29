from django.shortcuts import render,redirect,HttpResponse
from.models import lenovo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='signin')
def fun(request):
    if request.method=='POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        foodtype=request.POST.get('foodtype')
        image=request.FILES.get('image')
        video=request.FILES.get('video')
        lenovo.objects.create(name=name,price=price,foodtype=foodtype,image=image,video=video)
    data=lenovo.objects.all()
    return render(request,'about.html',{'data':data})
def delete(request,id):
    lenovo.objects.filter(id=id).delete()
    return redirect('fun')

def edit(request,id):
    item=lenovo.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        foodtype=request.POST.get('foodtype')
        image=request.FILES.get('image')
        video=request.FILES.get('video')
        item.name=name
        item.price=price
        item.foodtype=foodtype
        item.image=image 
        item.video=video
        item.save()
        return redirect('fun')
    return render( request,'about.html',{'item':item})




def signup(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        secondname=request.POST.get('secondname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password==cpassword:
            user=User.objects.create_user(username=username,password=password,email=email)
            return redirect('signin')
        else:
            return redirect('signup')
    return render(request,'signup.html')
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('item')
    return render(request,'signin.html')
def veg(request):
    return render(request,'vegitem.html')
        
def nonveg(request):
    return render(request,'nonveg.html')

def item(request):
    return render(request,'items.html')

def tiffen(request):
    return render(request,'tiffen.html')

def chai(request):
    return render(request,'chai.html')
def signout(request):
    logout(request)
    return redirect('signin')

def teaorder(request):
    return render(request,'teaorder.html')

        





    

