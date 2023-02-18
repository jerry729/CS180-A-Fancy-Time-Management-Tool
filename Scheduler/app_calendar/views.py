from django.shortcuts import render, HttpResponse, redirect
import MySQLdb

# Create your views here.
def index(request):
    return redirect('http://localhost:8000/login')

def login(request):
    return render(request, 'login.html')

# html, current-app-dir/templates/ 
# search order as settings.py: INSTALLED_APPS
def cal_main(request):
    return render(request, 'calendar.html')