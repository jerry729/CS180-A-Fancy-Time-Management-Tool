# Generated by Django 4.1.6 on 2023-03-12 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_calendar', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskinfo',
            name='Task_end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='taskinfo',
            name='Task_owner_scheduler',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='taskinfo',
            name='Task_owner_user',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='taskinfo',
            name='Task_start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
