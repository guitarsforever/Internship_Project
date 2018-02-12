# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from hahe.forms import (
Status_form, Completion_Date_form, LaunchDateForm,assignedUser
)
from django.views.generic import TemplateView, ListView
from hahe.models import (
Product, Team, Task, TaskSta, DashboardControlDevice,Announcements, DefaultDevice
)
import datetime
from . import extra_utils
from datetime import timedelta
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

class HomepageHAView(LoginRequiredMixin,TemplateView ):
    template_name = 'hahe/homepageHA.html'
    login_url = '/login/auth/'
    def get(self, request):
        device = Product.objects.filter(Device_Category='HA')
        for D in device:
            print(D.Name)
        args = {'Devices': device, }
        return render(request, self.template_name, args)

class HomepageHEView(LoginRequiredMixin,TemplateView ):
    template_name = 'hahe/homepageHE.html'
    login_url = '/login/auth/'
    def get(self, request):
        device = Product.objects.filter(Device_Category='HE')
        for D in device:
            print(D.Name)
        args = {'Devices': device, }
        return render(request, self.template_name, args)

class DeviceSummaryHAView(LoginRequiredMixin,TemplateView ):
    template_name = 'hahe/devicesummaryHA.html'
    login_url = '/login/auth/'
    def get(self, request,pk):
        extra_utils.update()
        selectedDevice = Product.objects.get(pk=pk)
        device = Product.objects.filter(Device_Category='HA')
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

class DeviceSummaryHEView(LoginRequiredMixin,TemplateView ):
    template_name = 'hahe/devicesummaryHE.html'
    login_url = '/login/auth/'
    def get(self, request,pk):
        extra_utils.update()
        selectedDevice = Product.objects.get(pk=pk)
        device = Product.objects.filter(Device_Category='HE')
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

class DeviceSummaryView(LoginRequiredMixin,TemplateView ):
    template_name = 'hahe/devicesummary.html'
    login_url = '/login/auth/'
    def get(self, request,pk):
        extra_utils.update()
        selectedDevice = Product.objects.get(pk=pk)
        MainDevices = DashboardControlDevice.objects.all().order_by("id")
        device = Product.objects.all().order_by("LaunchDate")
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
        args = {'Device':device, 'MainDevices':MainDevices,'selectedDevice':selectedDevice,'Delayed':Delayed,
                'Completed':Completed, 'DueSoon':DueSoon,'OnTime':OnTime, 'TeamName':TeamName}
        return render(request, self.template_name, args )

class HomepageView(LoginRequiredMixin,TemplateView ):
    template_name = 'hahe/homepage.html'
    login_url = '/login/auth/'
    def get(self, request):
        extra_utils.update()
        MainDevices = DashboardControlDevice.objects.all().order_by("id")
        device = Product.objects.all().order_by("LaunchDate")
        args = {'Device':device, 'MainDevices':MainDevices, }
        return render(request, self.template_name, args )

class DetailExcelView (LoginRequiredMixin,TemplateView ):
    template_name = 'hahe/detailexcel.html'
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
    template_name = 'hahe/excel.html'
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
    template_name = 'hahe/DefaultTemplate.html'
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

            Defaultdevice = DefaultDevice.objects.order_by('-id')[0]
            NewProduct = Product (Name = "Default HA/HE product",LaunchDate = launchdate,
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
                                        IsPostLaunch=task.IsPostLaunch, AssignedUser=task.AssignedUser, team = NewTeam, )
                    else:
                        NewTask = Task (TaskName = task.Name, team = NewTeam)
                    NewTask.save()

            # Team1 = Team (TeamName = "Product Readiness", Poc1 = "Michael Vigliotti",Poc2 = "Patrick Koo" , Product=NewProduct)
            # Team1.save()
            # Team2 = Team (TeamName = "Video Content", Poc1 ="Allison Graham",Poc2 = "Nicole Cantwell", Product=NewProduct)
            # Team2.save()
            # Team3 = Team (TeamName = "Digital Content", Poc1 = "Joseph Suplicki",Poc2 = "Jessie Trochez", Product=NewProduct)
            # Team3.save()
            # Team4 = Team (TeamName = "Call Center Training", Poc1 = "Ly Nguyen",Poc2 = "Casey Cribbin", Product=NewProduct)
            # Team4.save()
            # Team5 = Team (TeamName = "Call Center Operation", Poc1 = "Martha Lee",Poc2 = "Seung Yeon Cho", Product=NewProduct)
            # Team5.save()
            # Team6 = Team (TeamName = "Product Support", Poc1 = "Scott Whitman",Poc2 = "Khaled Abuali", Product=NewProduct)
            # Team6.save()
            # Team7 = Team (TeamName = "Warehouse", Poc1 = "Hyuk Dae Kwon",Poc2 = "James Kim" ,Product=NewProduct)
            # Team7.save()
            # Team8 = Team (TeamName = "Field Service", Poc1 = "Andrew Yoo",Poc2 = "Ted Lee", Product=NewProduct)
            # Team8.save()
            # Team9 = Team (TeamName = "Tech Support", Poc1 = "Jeffrey Brutman",Poc2 = "Rick Heal" , Product=NewProduct)
            # Team9.save()
            # Team10 = Team (TeamName = "Service Marketing", Poc1 = "Jessica Yu",Poc2 = "Mohsen Sheikh", Product=NewProduct)
            # Team10.save()
            # Team11 = Team (TeamName = "Service Training",Poc1 = "Nicholas Webert",Poc2 = "Michael Yelo",  Product=NewProduct)
            # Team11.save()
            # Team12 = Team (TeamName = "Parts",Poc1 = "David Caldwell",Poc2 = "Gregory Pak",  Product=NewProduct)
            # Team12.save()
            #
            #
            # Task1_Team1 = Task (TaskName = "Project Kickoff Meeting",StartDate= launchdate+ timedelta(-100),
            #                     EndDate=launchdate+timedelta(-90), team = Team1)
            # Task1_Team1.save()
            # Task2_Team1 = Task(TaskName="Receive PR Samples from HQ",StartDate= launchdate- timedelta(100),
            #                     EndDate=launchdate-timedelta(85), team=Team1)
            # Task2_Team1.save()
            # Task3_Team1 = Task(TaskName="Develop Schedule and requirements",StartDate= launchdate- timedelta(90),
            #                     EndDate=launchdate-timedelta(80), team=Team1)
            # Task3_Team1.save()
            # Task4_Team1 = Task(TaskName="Determine Field Test requirements",StartDate= launchdate- timedelta(80),
            #                     EndDate=launchdate-timedelta(70), team=Team1)
            # Task4_Team1.save()
            # Task5_Team1 = Task(TaskName="Marketing Deck Distribution",StartDate= launchdate- timedelta(75),
            #                     EndDate=launchdate-timedelta(65), team=Team1)
            # Task5_Team1.save()
            # Task6_Team1 = Task(TaskName="User Manual Distribution",StartDate= launchdate- timedelta(75),
            #                     EndDate=launchdate-timedelta(45), team=Team1)
            # Task6_Team1.save()
            # Task7_Team1 = Task(TaskName="Distribute Full list of SKUs",StartDate= launchdate- timedelta(60),
            #                     EndDate=launchdate-timedelta(45), team=Team1)
            # Task7_Team1.save()
            # Task8_Team1 = Task(TaskName="Production Samples (order/send)",StartDate= launchdate- timedelta(30),
            #                     EndDate=launchdate-timedelta(14), team=Team1)
            # Task8_Team1.save()
            # Task9_Team1 = Task(TaskName="User Manuals (on .com) (received)",StartDate= launchdate- timedelta(14),
            #                     EndDate=launchdate-timedelta(0), team=Team1)
            # Task9_Team1.save()
            #
            # Task1_Team2 = Task (TaskName = "Topic Lists",StartDate= launchdate- timedelta(45),
            #                     EndDate=launchdate-timedelta(14), team = Team2)
            # Task1_Team2.save()
            # Task2_Team2 = Task(TaskName="Scripts",StartDate= launchdate- timedelta(0),
            #                     EndDate=launchdate+timedelta(14), team=Team2)
            # Task2_Team2.save()
            # Task3_Team2 = Task(TaskName="Finalize Video",StartDate= launchdate+ timedelta(14),
            #                     EndDate=launchdate+timedelta(60), team=Team2)
            # Task3_Team2.save()
            #
            # Task1_Team3 = Task (TaskName = "Samples (received)",StartDate= launchdate- timedelta(75),
            #                     EndDate=launchdate-timedelta(14), team = Team3)
            # Task1_Team3.save()
            # Task2_Team3 = Task(TaskName="Pre-Sales FAQ (received/posted)",StartDate= launchdate- timedelta(60),
            #                     EndDate=launchdate-timedelta(45), team=Team3)
            # Task2_Team3.save()
            # Task3_Team3 = Task(TaskName="Customer Content (Samsung.com)",StartDate= launchdate- timedelta(60),
            #                     EndDate=launchdate-timedelta(14), team=Team3)
            # Task3_Team3.save()
            # Task4_Team3 = Task(TaskName="Agent Content: (Decision Tree)",StartDate= launchdate- timedelta(60),
            #                     EndDate=launchdate-timedelta(14), team=Team3)
            # Task4_Team3.save()
            # Task5_Team3 = Task(TaskName="Application: Samsung+ (content)",StartDate= launchdate- timedelta(60),
            #                     EndDate=launchdate-timedelta(30), team=Team3)
            # Task5_Team3.save()
            # Task6_Team3 = Task(TaskName="Simulators",StartDate= launchdate- timedelta(60),
            #                     EndDate=launchdate-timedelta(14), team=Team3)
            # Task6_Team3.save()
            #
            # Task1_Team4 = Task (TaskName = "Create Training: Agents",StartDate= launchdate- timedelta(60),
            #                     EndDate=launchdate-timedelta(30), team = Team4)
            # Task1_Team4.save()
            # Task2_Team4 = Task(TaskName="Training Expectation Rollout",StartDate= launchdate- timedelta(45),
            #                     EndDate=launchdate-timedelta(30), team=Team4)
            # Task2_Team4.save()
            # Task3_Team4 = Task(TaskName="Train the Trainer",StartDate= launchdate- timedelta(30),
            #                     EndDate=launchdate-timedelta(20), team=Team4)
            # Task3_Team4.save()
            # Task4_Team4 = Task(TaskName="Train: Agents",StartDate= launchdate- timedelta(30),
            #                     EndDate=launchdate-timedelta(0), team=Team4)
            # Task4_Team4.save()
            #
            # Task1_Team5 = Task (TaskName = "Sales Forecast (received)",StartDate= launchdate- timedelta(75),
            #                     EndDate=launchdate-timedelta(60), team = Team5)
            # Task1_Team5.save()
            # Task2_Team5 = Task(TaskName="Define Support Hours (received)",StartDate= launchdate- timedelta(75),
            #                     EndDate=launchdate-timedelta(60), team=Team5)
            # Task2_Team5.save()
            # Task3_Team5 = Task(TaskName="Contact Volume Forecast",StartDate= launchdate- timedelta(40),
            #                     EndDate=launchdate-timedelta(30), team=Team5)
            # Task3_Team5.save()
            # Task4_Team5 = Task(TaskName="Staffing Plan (Voice & Digital)",StartDate= launchdate- timedelta(30),
            #                     EndDate=launchdate-timedelta(20), team=Team5)
            # Task4_Team5.save()
            #
            # Task1_Team6 = Task (TaskName = "PV/PR Sample (received)",StartDate= launchdate- timedelta(100),
            #                     EndDate=launchdate-timedelta(85), team = Team6)
            # Task1_Team6.save()
            # Task2_Team6 = Task(TaskName="Serviceability Test",StartDate= launchdate- timedelta(90),
            #                     EndDate=launchdate-timedelta(85), team=Team6)
            # Task2_Team6.save()
            # Task3_Team6 = Task(TaskName="Doc Review: Service Manual",StartDate= launchdate- timedelta(90),
            #                     EndDate=launchdate-timedelta(80), team=Team6)
            # Task3_Team6.save()
            # Task4_Team6 = Task(TaskName="Doc Review: Box Art",StartDate= launchdate- timedelta(90),
            #                     EndDate=launchdate-timedelta(70), team=Team6)
            # Task4_Team6.save()
            # Task5_Team6 = Task(TaskName="PR Evaluation", team=Team6)
            # Task5_Team6.save()
            # Task6_Team6 = Task(TaskName="UL/FCC/Agency Testing (received)", team=Team6)
            # Task6_Team6.save()
            # Task7_Team6 = Task(TaskName="OBE / Functionality Test",StartDate= launchdate- timedelta(0),
            #                     EndDate=launchdate+timedelta(30), team=Team6)
            # Task7_Team6.save()
            # Task8_Team6 = Task(TaskName="OBE / Performance Test",StartDate= launchdate- timedelta(0),
            #                     EndDate=launchdate+timedelta(30), team=Team6)
            # Task8_Team6.save()
            # Task9_Team6 = Task(TaskName="update STG",StartDate= launchdate- timedelta(0),
            #                     EndDate=launchdate+timedelta(30), team=Team6)
            # Task9_Team6.save()
            #
            # Task1_Team7 = Task (TaskName = "Packing Test(Pre-Production)", team = Team7)
            # Task1_Team7.save()
            # Task2_Team7 = Task(TaskName="Cross Inspection (Factory)", team=Team7)
            # Task2_Team7.save()
            # Task3_Team7 = Task(TaskName="Customer Experience Test", team=Team7)
            # Task3_Team7.save()
            #
            # Task1_Team8 = Task (TaskName = "Determine service Category", team = Team8)
            # Task1_Team8.save()
            # Task2_Team8 = Task(TaskName="Warranty Review", team=Team8)
            # Task2_Team8.save()
            # Task3_Team8 = Task(TaskName="Develop New Service Procedure", team=Team8)
            # Task3_Team8.save()
            #
            # Task1_Team9 = Task (TaskName = "User Manual Received", team = Team9)
            # Task1_Team9.save()
            # Task2_Team9 = Task(TaskName="User Manual Review and Revisions", team=Team9)
            # Task2_Team9.save()
            # Task3_Team9 = Task(TaskName="User Manual Completion and Approval", team=Team9)
            # Task3_Team9.save()
            #
            #
            # Task1_Team10 = Task (TaskName = "Determine VIP Status",StartDate= launchdate- timedelta(90),
            #                     EndDate=launchdate-timedelta(80), team = Team10)
            # Task1_Team10.save()
            # Task2_Team10 = Task(TaskName="Flag GCIC, Develop content",StartDate= launchdate- timedelta(80),
            #                     EndDate=launchdate-timedelta(60), team=Team10)
            # Task2_Team10.save()
            # Task3_Team10 = Task(TaskName="Train Agents ",StartDate= launchdate- timedelta(60),
            #                     EndDate=launchdate-timedelta(30), team=Team10)
            # Task3_Team10.save()
            # Task4_Team10 = Task(TaskName="Train Network (Demo Checklist)",StartDate= launchdate- timedelta(60),
            #                     EndDate=launchdate-timedelta(30), team=Team10)
            # Task4_Team10.save()
            #
            # Task1_Team11 = Task (TaskName = "Doc Review: Training Manual",StartDate= launchdate- timedelta(60),
            #                     EndDate=launchdate-timedelta(30), team = Team11)
            # Task1_Team11.save()
            # Task2_Team11 = Task(TaskName="TV Certification Training Guide", team=Team11)
            # Task2_Team11.save()
            # Task3_Team11 = Task(TaskName="Update eLearning", team=Team11)
            # Task3_Team11.save()
            # Task4_Team11 = Task(TaskName="Train Tech Support",StartDate= launchdate+ timedelta(15),
            #                     EndDate=launchdate+timedelta(30), team=Team11)
            # Task4_Team11.save()
            # Task5_Team11 = Task(TaskName="Train the Trainer", team=Team11)
            # Task5_Team11.save()
            # Task6_Team11 = Task(TaskName="Fast Track", team=Team11)
            # Task6_Team11.save()
            #
            # Task1_Team12 = Task (TaskName = "BOM review ",StartDate= launchdate- timedelta(90),
            #                     EndDate=launchdate-timedelta(30), team = Team12)
            # Task1_Team12.save()
            # Task2_Team12 = Task(TaskName="Initial Parts Ordering",StartDate= launchdate- timedelta(60),
            #                     EndDate=launchdate-timedelta(30), team=Team12)
            # Task2_Team12.save()
            # Task3_Team12 = Task(TaskName="Parts Available: Panel  (BN95*)",StartDate= launchdate- timedelta(14),
            #                     EndDate=launchdate-timedelta(4), team=Team12)
            # Task3_Team12.save()
            # Task4_Team12 = Task(TaskName="Parts Available: TV/Main (BN94*)",StartDate= launchdate- timedelta(14),
            #                     EndDate=launchdate-timedelta(4), team=Team12)
            # Task4_Team12.save()
            # Task5_Team12 = Task(TaskName="Parts Available: OCB/OCM  (BN91*)",StartDate= launchdate- timedelta(14),
            #                     EndDate=launchdate-timedelta(4), team=Team12)
            # Task5_Team12.save()
            # Task6_Team12 = Task(TaskName="Parts Available: SMPS (BN44*)",StartDate= launchdate- timedelta(14),
            #                     EndDate=launchdate-timedelta(4), team=Team12)
            # Task6_Team12.save()
            # Task7_Team12 = Task(TaskName="Parts Available: Light Dimming",StartDate= launchdate- timedelta(14),
            #                     EndDate=launchdate-timedelta(4), team=Team12)
            # Task7_Team12.save()


            return redirect('/admin/hahe/product/')


class ProductView(LoginRequiredMixin,ListView):
    template_name = 'hahe/summary.html'
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

        teams1 = device_latest.team_set.all().order_by('id')

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

        args = {'Device': devices, 'teams':teams1, 'announcement':announcement}
        return render (request, self.template_name, args, )

class IntermediateView(LoginRequiredMixin,ListView):
    template_name = 'hahe/intermediate.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        devices = Product.objects.get(pk=pk)
        teams = devices.team_set.all().order_by('id')
        teamnames = []
        teamid = []
        poc1 = []
        poc2 = []
        completed = []
        for team in teams:
            teamnames.append(team.TeamName)
            teamid.append(team.id)
            poc1.append(team.Poc1)
            poc2.append(team.Poc2)
            completed.append(team.completed)
        args = {'devices':devices, 'teams':teams, 'teamnames':teamnames, 'poc1':poc1, 'poc2':poc2,'completed':completed
                ,'teamid':teamid}
        return render(request, self.template_name, args )

class DetailView (LoginRequiredMixin,TemplateView):
    template_name = 'hahe/detail.html'
    login_url = '/login/auth/'

    def get(self, request, id):

        teams = Team.objects.get(pk=id)
        device = teams.Product
        DeviceTeam = device.team_set.all().order_by('id')
        tasks = teams.task_set.all().order_by('id')
        today = datetime.date.today()
        form = []
        userassigned = []
        dateform = []
        taskTimeDelta = []
        Taskcompleted = 0
        NumberOfTasks = 0
        PercentCompleted = 0
        for task in tasks:
          if task.IsPostLaunch == False:
            userassigned.append(assignedUser(instance=task))
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


        zipped_data = zip(tasks,form,dateform, taskTimeDelta,userassigned)
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
            userassigned = assignedUser(request.POST,instance=task)
            assign = str(counter) + "Assign"
            button = str(counter) + "submit"
            if button in request.POST:
                if form.is_valid() and dateform.is_valid():
                    post = form.save(commit=False)
                    post.user = request.user
                    post.Task = task
                    dateform.save()
                    post.save()
                    return redirect('/hahe/teams/' + id)
                else:
                    return redirect('/hahe/teams/' + id)
            if assign in request.POST:
                print(assign)
                if userassigned.is_valid():
                    userassigned.save()
                    return redirect('/hahe/teams/' + id)
                else:
                    return redirect('/hahe/teams/' + id)
            counter = counter +1
        print("came out of the loop")
        return redirect('/hahe/teams/' + id)
