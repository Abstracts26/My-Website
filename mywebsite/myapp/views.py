from django.shortcuts import render , redirect
from .forms import *
from .filters import MobileFilter
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

@login_required(login_url='login')


# Create your views here.

def home(request):

    mobiles = MobilePhone.objects.all()
    form= MobileFilter(request.GET, queryset=mobiles)
    mobiles = form.qs
    context = {'mobiles':mobiles, 'form':form}
    return render(request,'myapp/home.html', context)

def read(request,pk):
    mobile = MobilePhone.objects.get(id=pk)
    context = {'mobile':mobile}
    return render(request,'myapp/read.html',context)

def about(request):
    return render(request,'myapp/about.html')

def CreateMobile(request):
    form = CUmodel()
    if request.method == 'POST':
        form = CUmodel(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'myapp/mobile_form.html',context)

def update(request,pk):
    item = MobilePhone.objects.get(id=pk)
    form= CUmodel (instance=item)

    if request.method == 'POST':
        form = CUmodel (request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context={'form': form}
    return render (request,'myapp/mobile_form.html',context)

def delete (request,pk):
    item = MobilePhone.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context={'item':item}
    return render (request,'myapp/delete.html',context)

def loginPage(request):
    if request.method== 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user= authenticate(request, username=username, password=password)
        if user is None:
            return HttpResponse('user not found')
        else:
            login(request,user)
            return redirect('home')
    return render(request,'myapp/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    form = UserCreationForm()
    if request.method== 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user= User.objects.get(username=request.POST.get('username'))
            login(request,user)
            return redirect('home')   
    context = {'form':form}
    return render(request,'myapp/register.html',context)
