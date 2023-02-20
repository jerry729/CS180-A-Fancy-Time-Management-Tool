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
    Task_owner_user = models.IntegerField()
    Task_owner_scheduler = models.IntegerField()
    Task_name = models.CharField(max_length=32)
    Task_description = models.CharField(max_length=64)
    Task_start_time = models.DateTimeField()
    Task_end_time = models.DateTimeField()


# class TeamInfo(models.Model):
