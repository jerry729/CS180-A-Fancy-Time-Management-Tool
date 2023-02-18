from django.db import models

# Create your models here.


class UserInfo(models.Model):
    user_id = models.CharField(max_length=32)
    user_name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)


class SchedulerInfo(models.Model):
    Scheduler_owner = models.CharField(max_length=32)
    Scheduler_name = models.CharField(max_length=32)


class TaskInfo(models.Model):
    Task_owner = models.CharField(max_length=32)
    Task_name = models.CharField(max_length=32)
    Task_start_time = models.DateTimeField()
    Task_start_time = models.DateTimeField()


