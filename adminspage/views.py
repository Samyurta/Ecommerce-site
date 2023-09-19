from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.auth import admin_only

# Create your views here.
@login_required
@admin_only

def dashboard(request):
    return render(request,'admins/dashboard.html')