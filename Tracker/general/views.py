# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from general.forms import (
Status_form, Completion_Date_form, LaunchDateForm
)
from django.views.generic import TemplateView, ListView
from general.models import (
Product, Team, Task, TaskStats,DefaultDevice,Announcements
)
import datetime
from . import extra_utils
from datetime import timedelta
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

class HomepageView(LoginRequiredMixin,TemplateView ):
    template_name = 'general/homepage.html'
    login_url = '/login/auth/'
    def get(self, request):
        extra_utils.update()
        device = Product.objects.all()
        for D in device:
            print(D.Name)
        args = {'Devices': device, }
        return render(request, self.template_name, args)

class DeviceSummaryView(LoginRequiredMixin,TemplateView ):
    template_name = 'general/devicesummary.html'
    login_url = '/login/auth/'
    def get(self, request,pk):
        extra_utils.update()
        selectedDevice = Product.objects.get(pk=pk)
        device = Product.objects.all()
        zipped_data = extra_utils.delayedElements(selectedDevice)
        Delayed = []
        Completed = []
        DueSoon = []
        OnTime = []
        TeamName = []
        for i,j,k,l,m in zipped_data:
            TeamName.append(m)
            Total = i+j+k+l
            if Total != 0:
                PercentI = round(((i/Total)*100),2)
                PercentJ = round(((j/Total)*100),2)
                PercentK = round(((k/Total)*100),2)
                PercentL = round(((l/Total)*100),2)
                Completed.append(PercentI)
                Delayed.append(PercentJ)
                DueSoon.append(PercentK)
                OnTime.append(PercentL)

                print (i,j,k,l)
            else:
                Completed.append(0)
                Delayed.append(0)
                DueSoon.append(0)
                OnTime.append(0)
        args = {'Device':device,'selectedDevice':selectedDevice,'Delayed':Delayed,
                'Completed':Completed, 'DueSoon':DueSoon,'OnTime':OnTime, 'TeamName':TeamName}
        return render(request, self.template_name, args )

class DetailExcelView (LoginRequiredMixin,TemplateView ):
    template_name = 'general/detailexcel.html'
    login_url = '/login/auth/'
    def get(self, request, pk):
        devices = Product.objects.get(pk=pk)
        teams = devices.team_set.all()
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
    template_name = 'general/excel.html'
    login_url = '/login/auth/'
    def get(self, request):
        devices = Product.objects.all().order_by("LaunchDate")
        device_latest = Product.objects.order_by('-id')[0]
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



        args = {'Device': devices, 'teams':teams}
        return render (request, self.template_name, args, )



class AddDeviceView (UserPassesTestMixin,TemplateView ):
    template_name = 'general/DefaultTemplate.html'
    raise_exception = True
    def test_func(self):
        return self.request.user.is_staff

    def get(self, request):
        form = LaunchDateForm()
        args = {'form':form,}
        return render(request, self.template_name, args)

    def post(self, request):
        if 'Submit' in request.POST:
            form = LaunchDateForm(request.POST)
            if form.is_valid():
                launchdate = form.cleaned_data['Launchdate']
            try:
                Defaultdevice = DefaultDevice.objects.order_by('-id')[0]
            except:
                NewProduct = Product(Name="Default Mobile product", LaunchDate=launchdate,
                                     ProductDescription="Default Description", )
                NewProduct.save()
                return redirect('/admin/general/product/')
            NewProduct = Product (Name = "Default Mobile product",LaunchDate = launchdate,
                                  ProductDescription = "Default Description",)
            NewProduct.save()
            Defaultteam = Defaultdevice.defaultteam_set.all().order_by('id')
            for team in Defaultteam:
                NewTeam = Team(TeamName=team.Name, Poc1 = team.Poc1, Poc2 = team.Poc2, Product = NewProduct)
                NewTeam.save()
                Defaulttask = team.defaulttask_set.all().order_by('id')
                for task in Defaulttask:
                    if task.StartDelta != None and task.EndDelta != None:
                        NewTask = Task (TaskName = task.Name ,StartDate= launchdate+ timedelta(task.StartDelta),
                                    EndDate=launchdate+timedelta(task.EndDelta),DependentTask =task.DependentTask,
                                        IsPostLaunch=task.IsPostLaunch, AssignedUser=task.AssignedUser, team = NewTeam)
                    else:
                        NewTask = Task (TaskName = task.Name, team = NewTeam)
                    NewTask.save()
            # NewProduct = Product (Name = "Default special product",LaunchDate = datetime.date.today(),
            #                              ProductDescription = "Default Description",)
            # NewProduct.save()
            # Team1 = Team (TeamName = "Product Readiness", Poc1 = "Sergio Viana", Product=NewProduct)
            # Team1.save()
            # Team2 = Team (TeamName = "Tools", Poc1 = "John Song", Product=NewProduct)
            # Team2.save()
            # Team3 = Team (TeamName = "Repair Setup", Poc1 = "John Song", Product=NewProduct)
            # Team3.save()
            # Team4 = Team (TeamName = "Customer Engineering", Poc1 = "John Song", Product=NewProduct)
            # Team4.save()
            # Team5 = Team (TeamName = "Training", Poc1 = "Dennis Prock",Poc2 = "Casey Cribbin", Product=NewProduct)
            # Team5.save()
            # Team6 = Team (TeamName = "Carrier Training", Poc1 = "Heather Darnell", Product=NewProduct)
            # Team6.save()
            # Team7 = Team (TeamName = "Parts", Poc1 = "Earl Kim",Poc2 = "Tanja Lonac" ,Product=NewProduct)
            # Team7.save()
            # Team8 = Team (TeamName = "Pricing", Poc1 = "Kun Ro", Product=NewProduct)
            # Team8.save()
            # Team9 = Team (TeamName = "Digital", Poc1 = "Jessie Trochez",Poc2 = "Allison" , Product=NewProduct)
            # Team9.save()
            # Team10 = Team (TeamName = "EnR", Poc1 = "Marco Castro", Product=NewProduct)
            # Team10.save()
            # Team11 = Team (TeamName = "SAM", Product=NewProduct)
            # Team11.save()
            # Team12 = Team (TeamName = "Premium Care", Product=NewProduct)
            # Team12.save()
            #
            #
            # Task1_Team1 = Task (TaskName = "PPD Document Received", team = Team1)
            # Task1_Team1.save()
            # Task2_Team1 = Task(TaskName="Specification Sheet Received", team=Team1)
            # Task2_Team1.save()
            # Task3_Team1 = Task(TaskName="In box BOM Received", team=Team1)
            # Task3_Team1.save()
            # Task4_Team1 = Task(TaskName="Return Process Defined", team=Team1)
            # Task4_Team1.save()
            # Task5_Team1 = Task(TaskName="Promotion Details Received", team=Team1)
            # Task5_Team1.save()
            # Task6_Team1 = Task(TaskName="Messaging Tool Kit Received", team=Team1)
            # Task6_Team1.save()
            # Task7_Team1 = Task(TaskName="PRF Completed", team=Team1)
            # Task7_Team1.save()
            # Task8_Team1 = Task(TaskName="PRF Distributed", team=Team1)
            # Task8_Team1.save()
            #
            # Task1_Team2 = Task (TaskName = "SW", team = Team2)
            # Task1_Team2.save()
            # Task2_Team2 = Task(TaskName="Repair Jigs", team=Team2)
            # Task2_Team2.save()
            #
            # Task1_Team3 = Task (TaskName = "RSI", team = Team3)
            # Task1_Team3.save()
            # Task2_Team3 = Task(TaskName="iQor", team=Team3)
            # Task2_Team3.save()
            # Task3_Team3 = Task(TaskName="BBY", team=Team3)
            # Task3_Team3.save()
            # Task4_Team3 = Task(TaskName="UBIF", team=Team3)
            # Task4_Team3.save()
            # Task5_Team3 = Task(TaskName="NY/NJ/LA", team=Team3)
            # Task5_Team3.save()
            #
            # Task1_Team4 = Task (TaskName = "Samples Ordered", team = Team4)
            # Task1_Team4.save()
            # Task2_Team4 = Task(TaskName="Samples Received", team=Team4)
            # Task2_Team4.save()
            # Task3_Team4 = Task(TaskName="Tooling Validation Completed", team=Team4)
            # Task3_Team4.save()
            # Task4_Team4 = Task(TaskName="Service Manual Received", team=Team4)
            # Task4_Team4.save()
            # Task5_Team4 = Task(TaskName="GSPN Setup", team=Team4)
            # Task5_Team4.save()
            #
            # Task1_Team5 = Task (TaskName = "E-learning Document Updated", team = Team5)
            # Task1_Team5.save()
            # Task2_Team5 = Task(TaskName="Call Center", team=Team5)
            # Task2_Team5.save()
            #
            # Task1_Team6 = Task (TaskName = "Product Overview", team = Team6)
            # Task1_Team6.save()
            #
            # Task1_Team7 = Task (TaskName = "SVC BOM", team = Team7)
            # Task1_Team7.save()
            # Task2_Team7 = Task(TaskName="BOM in GSPN", team=Team7)
            # Task2_Team7.save()
            # Task3_Team7 = Task(TaskName="Forecasting", team=Team7)
            # Task3_Team7.save()
            # Task4_Team7 = Task(TaskName="Initial Order", team=Team7)
            # Task4_Team7.save()
            # Task5_Team7 = Task(TaskName="SEA Warehouse Received", team=Team7)
            # Task5_Team7.save()
            # Task6_Team7 = Task(TaskName="PO s placed", team=Team7)
            # Task6_Team7.save()
            #
            # Task1_Team8 = Task (TaskName = "IW / OOW - MI", team = Team8)
            # Task1_Team8.save()
            # Task2_Team8 = Task(TaskName="IW/ OOW - WIS", team=Team8)
            # Task2_Team8.save()
            # Task3_Team8 = Task(TaskName="Parts ASC", team=Team8)
            # Task3_Team8.save()
            # Task4_Team8 = Task(TaskName="Parts WIS", team=Team8)
            # Task4_Team8.save()
            # Task5_Team8 = Task(TaskName="Fixed ASC Pricing setup", team=Team8)
            # Task5_Team8.save()
            #
            #
            # Task1_Team9 = Task (TaskName = "Answers", team = Team9)
            # Task1_Team9.save()
            # Task2_Team9 = Task(TaskName="Simulator", team=Team9)
            # Task2_Team9.save()
            # Task3_Team9 = Task(TaskName="Agent TSG", team=Team9)
            # Task3_Team9.save()
            # Task4_Team9 = Task(TaskName="Add SKU to FastLink", team=Team9)
            # Task4_Team9.save()
            # Task5_Team9 = Task(TaskName="Video", team=Team9)
            # Task5_Team9.save()
            # Task6_Team9 = Task(TaskName="ITB", team=Team9)
            # Task6_Team9.save()
            #
            #
            # Task1_Team10 = Task (TaskName = "Forecasting", team = Team10)
            # Task1_Team10.save()
            # Task2_Team10 = Task(TaskName="Ordering", team=Team10)
            # Task2_Team10.save()
            # Task3_Team10 = Task(TaskName="Received ", team=Team10)
            # Task3_Team10.save()
            #
            # Task1_Team11 = Task (TaskName = "Seed Stock Ordered", team = Team11)
            # Task1_Team11.save()
            # Task2_Team11 = Task(TaskName="Seed Stock Received", team=Team11)
            # Task2_Team11.save()
            #
            # Task1_Team12 = Task (TaskName = "Eligiblity ", team = Team12)
            # Task1_Team12.save()
            # Task2_Team12 = Task(TaskName="Training", team=Team12)
            # Task2_Team12.save()
            # Task3_Team12 = Task(TaskName="Seed Stock Delivery", team=Team12)
            # Task3_Team12.save()


            return redirect('/admin/general/product/')


class ProductView(LoginRequiredMixin,ListView):
    template_name = 'general/summary.html'
    login_url = '/login/auth/'
    def get(self, request):
        devices = Product.objects.all().order_by("LaunchDate")
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

        announcement = 1
        try:
            announcement = Announcements.objects.order_by("-id")[0]
        except:
            print ("Error")
        else:
            print(announcement.post)

        args = {'Device': devices, 'teams':teams,'announcement':announcement}
        return render (request, self.template_name, args, )

class IntermediateView(LoginRequiredMixin,ListView):
    template_name = 'general/intermediate.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        devices = Product.objects.get(pk=pk)
        teams = devices.team_set.all().order_by('id')
        args = {'devices':devices, 'teams':teams}
        return render(request, self.template_name, args )

class DetailView (LoginRequiredMixin,TemplateView):
    template_name = 'general/detail.html'
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
                    return redirect('/general/teams/' + id)
                else:
                    return redirect('/general/teams/' + id)
            counter = counter +1
        print("came out of the loop")
        return redirect('/general/teams/' + id)
