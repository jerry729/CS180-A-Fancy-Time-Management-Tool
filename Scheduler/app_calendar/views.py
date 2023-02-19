from django.shortcuts import render, HttpResponse, redirect
from .myform import HelloForm

# Create your views here.
def index(request):
    return redirect('/login/')

def login(request):
    exform = HelloForm()
    return render(request, 'login.html', {'form': exform})

# html, current-app-dir/templates/ 
# search order as settings.py: INSTALLED_APPS
def cal_main(request):
    return render(request, 'calendar.html')