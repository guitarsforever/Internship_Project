# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from others.forms import (
Status_form, Completion_Date_form
)
from django.views.generic import TemplateView, ListView
from others.models import (
Product, Team, Task, TaskStat, category
)
import datetime
from datetime import timedelta
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

class DetailExcelView (LoginRequiredMixin,TemplateView ):
    template_name = 'others/detailexcel.html'
    login_url = '/login/auth/'
    def get(self, request, pk):
        devices = Product.objects.get(pk=pk)
        teams = devices.team_set.all().order_by('id')
        NumberOfTasksArray = []
        TaskInstance = []
        for team in teams:
            tasks = team.task_set.all().order_by('id')
            TaskInstance.append(tasks)
            NumberOfTasks = 1
            for task in tasks:
                NumberOfTasks = NumberOfTasks + 1
            NumberOfTasksArray.append(NumberOfTasks)

        zipped_data = zip(teams, NumberOfTasksArray, TaskInstance)

        args = {'devices':devices, 'teams':teams, 'zip':zipped_data}
        return render(request, self.template_name, args )

class ExcelView (LoginRequiredMixin,TemplateView ):
    template_name = 'others/excel.html'
    login_url = '/login/auth/'
    def get(self, request):
        devices = Product.objects.all().order_by("LaunchDate")
        try:
            device_latest = Product.objects.order_by('-id')[0]
        except:
            print ("Error")
            args = {'Device': devices,}
            return render (request, self.template_name, args, )
        cat = category.objects.all()
        teams = device_latest.team_set.all().order_by('id')

        for device in devices:
            if device.Archive == False:
                teams = device.team_set.all().order_by('id')
                OverallTasks = 0
                OverallCompletedTasks = 0
                for team in teams:
                    today = datetime.date.today()
                    tasks = team.task_set.all().order_by('id')
                    Taskcompleted = 0
                    NumberOfTasks = 0
                    for task in tasks:
                        OverallTasks = OverallTasks+1
                        NumberOfTasks = NumberOfTasks + 1
                        if task.CompleteDate:
                            task.Warning = False
                            task.Alert = False
                            OverallCompletedTasks = OverallCompletedTasks +1
                            Taskcompleted = Taskcompleted + 1
                        if task.EndDate:
                            Time_delta = task.EndDate - today
                            if Time_delta < timedelta(team.Time_Delta_For_Warning) and Time_delta > timedelta(0) and \
                                    not task.CompleteDate:
                                task.Warning = True
                                team.Status = 'At Risk'
                            elif Time_delta < timedelta(0) and not task.CompleteDate:
                                task.Warning = False
                                task.Alert = True
                        else:
                            Time_delta = None
                        task.save()

                    for task in tasks:
                        if task.Alert == True:
                            team.Status = 'Delayed'
                        task.save()

                    if NumberOfTasks != 0:
                        PercentCompleted = int((Taskcompleted * 100) / NumberOfTasks)
                        team.completed = PercentCompleted
                        team.save()
                if OverallTasks!= 0:
                    OverallCompletedPercent = int((OverallCompletedTasks * 100)/OverallTasks)
                    device.completed = OverallCompletedPercent
                    device.save()



        args = {'Device': devices, 'teams':teams, 'cat':cat}
        return render (request, self.template_name, args, )

class ProductView(LoginRequiredMixin,ListView):
    template_name = 'others/summary.html'
    login_url = '/login/auth/'
    def get(self, request):
        devices = Product.objects.all().order_by("LaunchDate")
        cat = category.objects.all()
        try:
            device_latest = Product.objects.order_by('-id')[0]
        except:
            print ("Error")
            args = {'Device': devices,}
            return render (request, self.template_name, args, )
        else:
            print ("Shreyas is here")

        teams = device_latest.team_set.all().order_by('id')

        for device in devices:
            if device.Archive == False:
                teams = device.team_set.all().order_by('id')
                OverallTasks = 0
                OverallCompletedTasks = 0
                for team in teams:
                    today = datetime.date.today()
                    tasks = team.task_set.all().order_by('id')
                    Taskcompleted = 0
                    NumberOfTasks = 0
                    for task in tasks:
                      if task.IsPostLaunch == False:
                        OverallTasks = OverallTasks+1
                        NumberOfTasks = NumberOfTasks + 1
                        if task.CompleteDate:
                            task.Warning = False
                            task.Alert = False
                            OverallCompletedTasks = OverallCompletedTasks +1
                            Taskcompleted = Taskcompleted + 1
                        if task.EndDate:
                            Time_delta = task.EndDate - today
                            if Time_delta < timedelta(team.Time_Delta_For_Warning) and Time_delta > timedelta(0) and \
                                    not task.CompleteDate:
                                task.Warning = True
                                team.Status = 'At Risk'
                            elif Time_delta < timedelta(0) and not task.CompleteDate:
                                task.Warning = False
                                task.Alert = True
                        else:
                            Time_delta = None
                        task.save()
                      else:
                        if task.CompleteDate:
                            task.Warning = False
                            task.Alert = False
                        if task.EndDate:
                            Time_delta = task.EndDate - today
                            if Time_delta < timedelta(team.Time_Delta_For_Warning) and Time_delta > timedelta(0) and \
                                    not task.CompleteDate:
                                task.Warning = True
                                team.Status = 'At Risk'
                            elif Time_delta < timedelta(0) and not task.CompleteDate:
                                task.Warning = False
                                task.Alert = True

                    for task in tasks:
                        if task.Alert == True:
                            team.Status = 'Delayed'
                        task.save()

                    if NumberOfTasks != 0:
                        PercentCompleted = int((Taskcompleted * 100) / NumberOfTasks)
                        team.completed = PercentCompleted
                        team.save()
                if OverallTasks!= 0:
                    OverallCompletedPercent = int((OverallCompletedTasks * 100)/OverallTasks)
                    device.completed = OverallCompletedPercent
                    device.save()



        args = {'Device': devices, 'teams':teams, 'cat':cat}
        return render (request, self.template_name, args, )

class IntermediateView(LoginRequiredMixin,ListView):
    template_name = 'others/intermediate.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        devices = Product.objects.get(pk=pk)
        teams = devices.team_set.all().order_by('id')
        args = {'devices':devices, 'teams':teams}
        return render(request, self.template_name, args )

class DetailView (LoginRequiredMixin,TemplateView):
    template_name = 'others/detail.html'
    login_url = '/login/auth/'

    def get(self, request, id):

        teams = Team.objects.get(pk=id)
        device = teams.Product
        DeviceTeam = device.team_set.all().order_by('id')
        tasks = teams.task_set.all().order_by('id')
        today = datetime.date.today()
        form = []
        dateform = []
        taskTimeDelta = []
        Taskcompleted = 0
        NumberOfTasks = 0
        PercentCompleted = 0
        for task in tasks:
          if task.IsPostLaunch == False:
            form.append (Status_form())
            dateform.append(Completion_Date_form(instance=task))
            NumberOfTasks = NumberOfTasks + 1
            if task.CompleteDate:
                task.Warning = False
                task.Alert = False
                Taskcompleted = Taskcompleted + 1
            if task.EndDate:
                Time_delta = task.EndDate - today
                if Time_delta < timedelta(teams.Time_Delta_For_Warning) and Time_delta > timedelta(0) and \
                    not task.CompleteDate:
                    task.Warning = True
                    teams.Status = 'At Risk'
                elif Time_delta < timedelta(0) and not task.CompleteDate:
                    task.Warning = False
                    task.Alert = True
            else:
                Time_delta = None
            taskTimeDelta.append (Time_delta)
            task.save()
          else:
            if task.CompleteDate:
                task.Warning = False
                task.Alert = False
            if task.EndDate:
                Time_delta = task.EndDate - today
                if Time_delta < timedelta(teams.Time_Delta_For_Warning) and Time_delta > timedelta(0) and \
                        not task.CompleteDate:
                    task.Warning = True
                    teams.Status = 'At Risk'
                elif Time_delta < timedelta(0) and not task.CompleteDate:
                    task.Warning = False
                    task.Alert = True

        for task in tasks:
            if task.Alert == True:
                teams.Status = 'Delayed'
            task.save()
        if NumberOfTasks != 0:
            PercentCompleted = int((Taskcompleted *100)/NumberOfTasks)
            teams.completed = PercentCompleted
            teams.save()


        zipped_data = zip(tasks,form,dateform, taskTimeDelta)
        args = {'device':device,'DeviceTeam':DeviceTeam,'teams':teams, 'tasks':tasks, 'forms':form,
                'dateforms':dateform, 'zipped_data':zipped_data, 'PercentCompleted':PercentCompleted}
        return render(request, self.template_name, args)

    def post(self,request, id):
        teams = Team.objects.get(pk=id)
        tasks = teams.task_set.all().order_by('id')
        form = []
        dateform = []
        counter =1
        for task in tasks:
            form = Status_form(request.POST)
            dateform = Completion_Date_form(request.POST,instance=task)
            button = str(counter) + "submit"
            print (button)
            if button in request.POST:
                if form.is_valid() and dateform.is_valid():
                    post = form.save(commit=False)
                    post.user = request.user
                    post.Task = task
                    dateform.save()
                    post.save()
                    return redirect('/others/teams/' + id)
                else:
                    return redirect('/others/teams/' + id)
            counter = counter +1
        print("came out of the loop")
        return redirect('/others/teams/' + id)
