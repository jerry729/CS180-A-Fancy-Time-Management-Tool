from django.shortcuts import render, HttpResponse, redirect
from .models import UserInfo, SchedulerInfo
from .myform import HelloForm
import MySQLdb


# Create your views here.
def index(request):
    return redirect('/login/')


def login(request):
    exform = HelloForm()
    if request.method == "GET":
        return render(request, 'login.html', {"form": exform})
    Username = request.POST.get("Username")
    Password = request.POST.get("Password")
    Search_user = UserInfo.objects.filter(user_name=Username, password=Password)
    if Search_user:
        return HttpResponse("Login success")
    else:
        return HttpResponse("Login fail")

# html, current-app-dir/templates/
# search order as settings.py: INSTALLED_APPS
def cal_main(request, null=None):
    # user_id = ''
    data_list = SchedulerInfo.objects.all()  # filter()
    if request.method == "GET":
        return render(request, 'calendar.html', {"data_list": data_list})
    Scheduler_name = request.POST.get("Scheduler name")
    Scheduler_owner = "123"
    Operation_type = request.POST.get("type")

    if Operation_type == "add":
        SchedulerInfo.objects.create(Scheduler_name=Scheduler_name, Scheduler_owner=Scheduler_owner)
        return HttpResponse("add success")

    if Operation_type == "delete":
        Search_Scheduler = SchedulerInfo.objects.filter(Scheduler_owner=Scheduler_owner, Scheduler_name=Scheduler_name)
        if Search_Scheduler:
            SchedulerInfo.objects.filter(Scheduler_owner=Scheduler_owner, Scheduler_name=Scheduler_name).delete()
            return HttpResponse("delete success")
        else:
            return HttpResponse("This Scheduler does not exist")


# user template
def user_template(request):
    UserInfo.objects.create(user_id='123', user_name='123', password='123')

    UserInfo.objects.filter(user_id=1).delete()  # delete data

    data_list = UserInfo.objects.all()  # return type:QuerySet .first()
    for obj in data_list:
        print(obj.user_id, obj.user_name, obj.user_password)

    UserInfo.objects.filter(user_id=1).update()  # update data

    return HttpResponse("success")
