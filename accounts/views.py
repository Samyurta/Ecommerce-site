from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import LoginForm

# Create your views here.
def register_user(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS,"account created")
            return redirect('/register')
        else:
            messages.add_message(request,messages.ERROR,'failed to create account')
            return render(request, 'account/register.html',{'form':form})
        
    context={
        'form':UserCreationForm
    }
    return render(request,'account/register.html', context)

def login_form(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(request, username=data['username'],password=data['password'])
            if user is not None:
                login(request,user)
                if user.is_staff:
                    return redirect('/admins/dashboard')
                else:
                    return redirect('/')
            else:
                messages.add_message(request, messages.ERROR,'please provide correct credential')
                return render(request,'account/login.html',{'form':form})
        
            
    context={
        'form':LoginForm
    }
    return render(request,'account/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('/login')