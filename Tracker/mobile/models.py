# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from django.db import models

# Create your models here.

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class SpecialProduct(models.Model):
    Name = models.CharField(max_length=100, default = '')
    ProductDescription = models.CharField(max_length=100, default='')
    LaunchDate = models.DateField()
    completed = IntegerRangeField(min_value=0, max_value=100, default=0)
    On_Time = 'On Time'
    At_Risk = 'At Risk'
    Delayed = 'Delayed'
    Status_Choice = (
        (On_Time, 'On Time'),
        (At_Risk, 'At Risk'),
        (Delayed, 'Delayed'),
    )

    Status = models.CharField(max_length=10, choices=Status_Choice, default='On_Time')
    Archive = models.BooleanField(default=False)

    class Meta:
        permissions = (
            ("is_strategic", "Is Strategic"),
        )


    def __str__(self):
        return self.Name

class Team(models.Model):
    TeamName = models.CharField(max_length=100, blank=True, default = '')
    Poc1 = models.CharField(max_length=100,blank=True, default='')
    Poc1_email = models.EmailField(max_length=100,blank=True, default='')
    Poc2 = models.CharField(max_length=100,blank=True, default='')
    Poc2_email = models.EmailField(max_length=100,blank=True, default='')
    Time_Delta_For_Warning = models.IntegerField(blank=True,default=7)
    completed = IntegerRangeField(min_value=0, max_value=100, default=0)
    On_Time = 'On Time'
    At_Risk = 'At Risk'
    Delayed = 'Delayed'
    Status_Choice = (
        (On_Time, 'On Time'),
        (At_Risk, 'At Risk'),
        (Delayed, 'Delayed'),
    )

    Status = models.CharField(max_length=10, choices=Status_Choice, default='On_Time')
    Product = models.ForeignKey(SpecialProduct, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.TeamName

class Task(models.Model):
    TaskName = models.CharField(max_length=100,blank=True, default='')
    StartDate = models.DateField(blank=True, null=True)
    EndDate = models.DateField(blank=True, null=True)
    CompleteDate = models.DateField(blank=True, null=True)
    DependentTask = models.CharField(max_length=250,blank=True, default='')
    Warning = models.BooleanField(default=False)
    Alert = models.BooleanField(default=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.TaskName

class TaskStatus(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.post

class DefaultDevice(models.Model):
    Name = models.CharField(max_length=100, default='Default')

    def __str__(self):
        return self.Name

class DefaultTeam(models.Model):
    Name = models.CharField(max_length=100, blank=True, default = '')
    Poc1 = models.CharField(max_length=100,blank=True, default='')
    Poc1_email = models.EmailField(max_length=100,blank=True, default='')
    Poc2 = models.CharField(max_length=100,blank=True, default='')
    Poc2_email = models.EmailField(max_length=100,blank=True, default='')
    Device = models.ForeignKey(DefaultDevice, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Name

class DefaultTask(models.Model):
    Name = models.CharField(max_length=100, blank=True, default='')
    StartDelta = models.IntegerField(default=0,blank=True, null=True)
    EndDelta = models.IntegerField(default=0,blank=True,null=True)
    IsPostLaunch = models.BooleanField(default=False)
    AssignedUser = models.CharField(max_length=250, blank=True, default='')
    Team = models.ForeignKey(DefaultTeam, on_delete=models.CASCADE, null=True)
    Team = models.ForeignKey(DefaultTeam, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Name

class Announcements(models.Model):
    post = models.TextField(blank=True,default='')
    information = 'information'
    warning = 'warning'
    alert = 'alert'
    Status_Choice = (
        (information, 'information'),
        (warning, 'warning'),
        (alert, 'alert'),
    )

    Severity = models.CharField(max_length=20, choices=Status_Choice, default='information')