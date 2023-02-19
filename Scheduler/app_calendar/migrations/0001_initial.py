# Generated by Django 4.1.6 on 2023-02-19 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchedulerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Scheduler_owner', models.CharField(max_length=32)),
                ('Scheduler_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='TaskInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task_owner', models.CharField(max_length=32)),
                ('Task_name', models.CharField(max_length=32)),
                ('Task_start_time', models.DateTimeField()),
                ('Task_end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=32)),
                ('user_name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
    ]