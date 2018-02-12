# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from mobile.forms import (
Status_form, Completion_Date_form, LaunchDateForm
)
from django.views.generic import TemplateView, ListView
from mobile.models import (
SpecialProduct, Team, Task, TaskStatus, DefaultDevice,Announcements
)
import datetime
from datetime import timedelta
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.

class DetailExcelView (LoginRequiredMixin,PermissionRequiredMixin,TemplateView ):
    permission_required = ('mobile.is_strategic')
    template_name = 'mobile/detailexcel.html'
    raise_exception = True
    # login_url = '/login/auth/'
    def get(self, request, pk):
        devices = SpecialProduct.objects.get(pk=pk)
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

class ExcelView (LoginRequiredMixin,PermissionRequiredMixin,TemplateView ):
    permission_required = ('mobile.is_strategic')
    template_name = 'mobile/excel.html'
    raise_exception = True
    # login_url = '/login/auth/'
    def get(self, request):
        devices = SpecialProduct.objects.all().order_by("LaunchDate")
        device_latest = SpecialProduct.objects.order_by('-id')[0]
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



class AddDeviceView (UserPassesTestMixin,PermissionRequiredMixin,TemplateView ):
    template_name = 'mobile/SpecialDefaultTemplate.html'
    permission_required = ('mobile.is_strategic')
    raise_exception = True
    def test_func(self):
        return self.request.user.is_superuser

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
                print("shreyas")
                NewProduct = SpecialProduct(Name="Default strategic product", LaunchDate=launchdate,
                                     ProductDescription="Default Description", )
                NewProduct.save()
                return redirect('/admin/mobile/specialproduct/')
            NewProduct = SpecialProduct (Name = "Default Mobile product",LaunchDate = launchdate,
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
            # NewProduct = SpecialProduct (Name = "Default special product",LaunchDate = datetime.date.today(),
            #                              ProductDescription = "Default Description",)
            # NewProduct.save()
            # Team1 = Team (TeamName = "Product Readiness", Poc1 = "Jasper Morse", Product=NewProduct)
            # Team1.save()
            # Team2 = Team (TeamName = "Forcasting & Planning", Poc1 = "Tanja Lonac", Product=NewProduct)
            # Team2.save()
            # Team3 = Team (TeamName = ".com - Digital Content", Poc1 = "Jiovanies Duperoy", Product=NewProduct)
            # Team3.save()
            # Team4 = Team (TeamName = ".com - Video Content", Poc1 = "Nikki Cantwell", Product=NewProduct)
            # Team4.save()
            # Team5 = Team (TeamName = "(.com) - ITB (In the Box)", Poc1 = "Nikki Cantwell", Product=NewProduct)
            # Team5.save()
            # Team6 = Team (TeamName = "Call Center Training", Poc1 = "Casey Cribbin", Product=NewProduct)
            # Team6.save()
            # Team7 = Team (TeamName = "Call Center Operations", Poc1 = "Seung(John) Yeon Cho", Product=NewProduct)
            # Team7.save()
            # Team8 = Team (TeamName = "NPI - Tools and Testing", Poc1 = "Hyungoo Lee", Product=NewProduct)
            # Team8.save()
            # Team9 = Team (TeamName = "Service Engineering - Repair", Poc1 = "Edhir Tukric",Poc2 = "Paul Walker" , Product=NewProduct)
            # Team9.save()
            # Team10 = Team (TeamName = "Parts Forecasting", Poc1 = "Paul Walker", Poc2 = "Edhir Tukric", Product=NewProduct)
            # Team10.save()
            # Team11 = Team (TeamName = "Service Engineering - Training", Poc1 = "Bob Nelson",Poc2 = "Mike Babbar", Product=NewProduct)
            # Team11.save()
            # Team12 = Team (TeamName = "Advanced Exchange", Poc1 = "Kyle Walker",Poc2 = "Marco Castro", Product=NewProduct)
            # Team12.save()
            # Team13 = Team (TeamName = "Service Training (In-store and WIS)", Poc1 = "Pascha Keller",Poc2 = "Mike Babbar", Product=NewProduct)
            # Team13.save()
            # Team14 = Team (TeamName = "Technical Training", Poc1 = "Nicholas",Poc2 = "Dennis Prock", Product=NewProduct)
            # Team14.save()
            # Team15 = Team (TeamName = "MPC Material Management", Poc1 = "Euiho Jung",Poc2 = "Tanja Lonac", Product=NewProduct)
            # Team15.save()
            # Team16 = Team (TeamName = "Sam - Carrier Center", Poc1 = "Maliaki Rodgers/Amy Freeman",Poc2 = "Scott Spiegel", Product=NewProduct)
            # Team16.save()
            # Team17 = Team (TeamName = "MPC - QA", Poc1 = "Justin Leon", Poc2 = "Sean O'Brien", Product=NewProduct)
            # Team17.save()
            # Team18 = Team (TeamName = "Premium Service", Poc1 = "Scott Sherrod", Poc2 = "Teresa Ignacio", Product=NewProduct)
            # Team18.save()
            # Team19 = Team (TeamName = "Product Liability", Poc1 = "Juni", Product=NewProduct)
            # Team19.save()
            # Team20 = Team (TeamName = "E-Commerce", Poc1 = "Russel Wilkins", Product=NewProduct)
            # Team20.save()
            #
            # Task1_Team1 = Task (TaskName = "Project Kickoff Meeting", team = Team1)
            # Task1_Team1.save()
            # Task2_Team1 = Task(TaskName="Obtain In Box BOM", team=Team1)
            # Task2_Team1.save()
            # Task3_Team1 = Task(TaskName="Obtain SKU's", team=Team1)
            # Task3_Team1.save()
            # Task4_Team1 = Task(TaskName="Receive PR Samples", team=Team1)
            # Task4_Team1.save()
            # Task5_Team1 = Task(TaskName="Verify LDU Order has been Placed", team=Team1)
            # Task5_Team1.save()
            # Task6_Team1 = Task(TaskName="Develop Schedule and requirements", team=Team1)
            # Task6_Team1.save()
            # Task7_Team1 = Task(TaskName="Marketing Deck Distribution (PPD)", team=Team1)
            # Task7_Team1.save()
            # Task8_Team1 = Task(TaskName="User Manual Distribution", team=Team1)
            # Task8_Team1.save()
            # Task9_Team1 = Task(TaskName="Distribute Full list of SKUs", team=Team1)
            # Task9_Team1.save()
            # Task10_Team1 = Task(TaskName="Distribute SBOM & Exploded parts view to team", team=Team1)
            # Task10_Team1.save()
            # Task11_Team1 = Task(TaskName="Production Samples IR (Request)", team=Team1)
            # Task11_Team1.save()
            #
            # Task1_Team2 = Task (TaskName = "Prepare the initial Forecast", team = Team2)
            # Task1_Team2.save()
            # Task2_Team2 = Task(TaskName="Update the weekly Forecast", team=Team2)
            # Task2_Team2.save()
            # Task3_Team2 = Task(TaskName="Post the weekly Forecast", team=Team2)
            # Task3_Team2.save()
            #
            # Task1_Team3 = Task (TaskName = "Production Information (received)", team = Team3)
            # Task1_Team3.save()
            # Task2_Team3 = Task(TaskName="Samples (received)", team=Team3)
            # Task2_Team3.save()
            # Task3_Team3 = Task(TaskName="Pre-Sales FAQ (received/posted)", team=Team3)
            # Task3_Team3.save()
            # Task4_Team3 = Task(TaskName="Agent Content: (Decision Tree)", team=Team3)
            # Task4_Team3.save()
            # Task5_Team3 = Task(TaskName="Application: Samsung+(content)", team=Team3)
            # Task5_Team3.save()
            # Task6_Team3 = Task(TaskName="Answers.com", team=Team3)
            # Task6_Team3.save()
            # Task7_Team3 = Task(TaskName="Simulators.com", team=Team3)
            # Task7_Team3.save()
            #
            # Task1_Team4 = Task (TaskName = "Pre-Production Sample (Received)", team = Team4)
            # Task1_Team4.save()
            # Task2_Team4 = Task(TaskName="Topic Lists", team=Team4)
            # Task2_Team4.save()
            # Task3_Team4 = Task(TaskName="Pre-Scripting", team=Team4)
            # Task3_Team4.save()
            # Task4_Team4 = Task(TaskName="Production Sample w/FFW(received)", team=Team4)
            # Task4_Team4.save()
            # Task5_Team4 = Task(TaskName="Scripting Finals", team=Team4)
            # Task5_Team4.save()
            # Task6_Team4 = Task(TaskName="Videos, onboarding", team=Team4)
            # Task6_Team4.save()
            # Task7_Team4 = Task(TaskName="Video Phase 1", team=Team4)
            # Task7_Team4.save()
            # Task8_Team4 = Task(TaskName="Video Phase 2", team=Team4)
            # Task8_Team4.save()
            #
            # Task1_Team5 = Task (TaskName = "Production Sample received", team = Team5)
            # Task1_Team5.save()
            # Task2_Team5 = Task(TaskName="User Manual R0", team=Team5)
            # Task2_Team5.save()
            # Task3_Team5 = Task(TaskName="User Manual R1", team=Team5)
            # Task3_Team5.save()
            # Task4_Team5 = Task(TaskName="User Manual R2", team=Team5)
            # Task4_Team5.save()
            # Task5_Team5 = Task(TaskName="User Manual R3", team=Team5)
            # Task5_Team5.save()
            # Task6_Team5 = Task(TaskName="User Manual Final Candidate", team=Team5)
            # Task6_Team5.save()
            # Task7_Team5 = Task(TaskName="User Manual Final + Source", team=Team5)
            # Task7_Team5.save()
            # Task8_Team5 = Task(TaskName="Accessibility", team=Team5)
            # Task8_Team5.save()
            # Task9_Team5 = Task(TaskName="In Box Guide R0", team=Team5)
            # Task9_Team5.save()
            # Task10_Team5 = Task(TaskName="In Box Guide R1", team=Team5)
            # Task10_Team5.save()
            # Task11_Team5 = Task(TaskName="In Box Guide R2", team=Team5)
            # Task11_Team5.save()
            # Task12_Team5 = Task(TaskName="In Box Guide R3", team=Team5)
            # Task12_Team5.save()
            # Task13_Team5 = Task(TaskName="In Box Guide Final Candidate", team=Team5)
            # Task13_Team5.save()
            # Task14_Team5 = Task(TaskName="In Box Guide Final + Source", team=Team5)
            # Task14_Team5.save()
            # Task15_Team5 = Task(TaskName="HSW R0", team=Team5)
            # Task15_Team5.save()
            # Task16_Team5 = Task(TaskName="HSW R1", team=Team5)
            # Task16_Team5.save()
            # Task17_Team5 = Task(TaskName="HSW R2", team=Team5)
            # Task17_Team5.save()
            # Task18_Team5 = Task(TaskName="HSW R3", team=Team5)
            # Task18_Team5.save()
            # Task19_Team5 = Task(TaskName="HSW Final Candidate", team=Team5)
            # Task19_Team5.save()
            # Task20_Team5 = Task(TaskName="HSW Final + Source", team=Team5)
            # Task20_Team5.save()
            #
            # Task1_Team6 = Task (TaskName = "Sample (received)", team = Team6)
            # Task1_Team6.save()
            # Task2_Team6 = Task(TaskName="Training Expectation Rollout (T1,T3-CS, L&R)", team=Team6)
            # Task2_Team6.save()
            # Task3_Team6 = Task(TaskName="Train the Trainer (T3)", team=Team6)
            # Task3_Team6.save()
            # Task4_Team6 = Task(TaskName="Agent Training - Alorica DR", team=Team6)
            # Task4_Team6.save()
            # Task5_Team6 = Task(TaskName="Agent Training - Alorica GVL", team=Team6)
            # Task5_Team6.save()
            # Task6_Team6 = Task(TaskName="Agent Training - HH Austin", team=Team6)
            # Task6_Team6.save()
            # Task7_Team6 = Task(TaskName="Agent Training - HH Manilla", team=Team6)
            # Task7_Team6.save()
            # Task8_Team6 = Task(TaskName="Agent Training - Knoah India", team=Team6)
            # Task8_Team6.save()
            # Task9_Team6 = Task(TaskName="Agent Training - Transcom", team=Team6)
            # Task9_Team6.save()
            # Task10_Team6 = Task(TaskName="Agent Training - Teleperformance TOR", team=Team6)
            # Task10_Team6.save()
            # Task11_Team6 = Task(TaskName="eLearning", team=Team6)
            # Task11_Team6.save()
            #
            # Task1_Team7 = Task (TaskName = "Production Information (received)", team = Team7)
            # Task1_Team7.save()
            # Task2_Team7 = Task(TaskName="Sales Forecast (received)", team=Team7)
            # Task2_Team7.save()
            # Task3_Team7 = Task(TaskName="Define Support Hours (received)", team=Team7)
            # Task3_Team7.save()
            # Task4_Team7 = Task(TaskName="Contact Volume Forecast", team=Team7)
            # Task4_Team7.save()
            # Task5_Team7 = Task(TaskName="Final Version Training Material Completed", team=Team7)
            # Task5_Team7.save()
            # Task6_Team7 = Task(TaskName="Consultant Guide from HQ (VOC team will receive first)", team=Team7)
            # Task6_Team7.save()
            # Task7_Team7 = Task(TaskName="Localize Consultant Guide from HQ", team=Team7)
            # Task7_Team7.save()
            # Task8_Team7 = Task(TaskName="Staffing Plan (Voice & Digital)", team=Team7)
            # Task8_Team7.save()
            #
            # Task1_Team8 = Task (TaskName = "Design for care (TMO)", team = Team8)
            # Task1_Team8.save()
            # Task2_Team8 = Task(TaskName="Update DFC Checklist w/new Model Info", team=Team8)
            # Task2_Team8.save()
            # Task3_Team8 = Task(TaskName="Create a DFC Report including Design Changes", team=Team8)
            # Task3_Team8.save()
            # Task4_Team8 = Task(TaskName="Tool Validation - MDL", team=Team8)
            # Task4_Team8.save()
            # Task5_Team8 = Task(TaskName="Tool Validation - IMEI Rewriting", team=Team8)
            # Task5_Team8.save()
            # Task6_Team8 = Task(TaskName="Tool Validation - Label", team=Team8)
            # Task6_Team8.save()
            # Task7_Team8 = Task(TaskName="Tool Validation - U400", team=Team8)
            # Task7_Team8.save()
            # Task8_Team8 = Task(TaskName="Tool Validation - CAL ADJ", team=Team8)
            # Task8_Team8.save()
            # Task9_Team8 = Task(TaskName="Tool Validation - Unlock Tool", team=Team8)
            # Task9_Team8.save()
            # Task10_Team8 = Task(TaskName="Tool Validation - WPC", team=Team8)
            # Task10_Team8.save()
            # Task11_Team8 = Task(TaskName="Verify DFC", team=Team8)
            # Task11_Team8.save()
            # Task12_Team8 = Task(TaskName="Request Samples for Tools and Parts Validation", team=Team8)
            # Task12_Team8.save()
            # Task13_Team8 = Task(TaskName="Receive Samples", team=Team8)
            # Task13_Team8.save()
            # Task14_Team8 = Task(TaskName="EDF files posted", team=Team8)
            # Task14_Team8.save()
            # Task15_Team8 = Task(TaskName="Create Parts Verification Document", team=Team8)
            # Task15_Team8.save()
            # Task16_Team8 = Task(TaskName="Testing RF CAL, RF Test", team=Team8)
            # Task16_Team8.save()
            # Task17_Team8 = Task(TaskName="Receive Jig List", team=Team8)
            # Task17_Team8.save()
            # Task18_Team8 = Task(TaskName="Validate Jig selection and quantity for PSC", team=Team8)
            # Task18_Team8.save()
            # Task19_Team8 = Task(TaskName="Equipment Order-Prepare for jigs to PSC", team=Team8)
            # Task19_Team8.save()
            # Task20_Team8 = Task(TaskName="Schedule a meeting with parts team to review SBOM", team=Team8)
            # Task20_Team8.save()
            #
            # Task1_Team9 = Task (TaskName = "Product Samples (received)", team = Team9)
            # Task1_Team9.save()
            # Task2_Team9 = Task(TaskName="Obtain Model info", team=Team9)
            # Task2_Team9.save()
            # Task3_Team9 = Task(TaskName="Request Test Samples for Tooling and Documentation", team=Team9)
            # Task3_Team9.save()
            # Task4_Team9 = Task(TaskName="HQ Training", team=Team9)
            # Task4_Team9.save()
            # Task5_Team9 = Task(TaskName="Ordering of LDU units", team=Team9)
            # Task5_Team9.save()
            # Task6_Team9 = Task(TaskName="Receive LDU Units", team=Team9)
            # Task6_Team9.save()
            # Task7_Team9 = Task(TaskName="ASC Setup(Carrier) to process & repair (post launch)", team=Team9)
            # Task7_Team9.save()
            # Task8_Team9 = Task(TaskName="Setup E-Learning (ASC/WIS)", team=Team9)
            # Task8_Team9.save()
            # Task9_Team9 = Task(TaskName="ASC/WISC Training", team=Team9)
            # Task9_Team9.save()
            # Task10_Team9 = Task(TaskName="Jig information received (RB Jig List)", team=Team9)
            # Task10_Team9.save()
            # Task11_Team9 = Task(TaskName="WISC Jigs List", team=Team9)
            # Task11_Team9.save()
            # Task12_Team9 = Task(TaskName="Jig Selection", team=Team9)
            # Task12_Team9.save()
            # Task13_Team9 = Task(TaskName="Jig Order placed (RB Mail-in-jigs) - Order Jigs", team=Team9)
            # Task13_Team9.save()
            # Task14_Team9 = Task(TaskName="Jig Order placed (for WISC jigs) - Order Jigs", team=Team9)
            # Task14_Team9.save()
            # Task15_Team9 = Task(TaskName="Supply ASC Jig List to ASCs", team=Team9)
            # Task15_Team9.save()
            # Task16_Team9 = Task(TaskName="Distribute Jigs to Mail-in-Operation", team=Team9)
            # Task16_Team9.save()
            # Task17_Team9 = Task(TaskName="parts Verification Meeting with GPCA for SUR Operation", team=Team9)
            # Task17_Team9.save()
            # Task18_Team9 = Task(TaskName="order Parts for Training", team=Team9)
            # Task18_Team9.save()
            # Task19_Team9 = Task(TaskName="Service Manual", team=Team9)
            # Task19_Team9.save()
            # Task20_Team9 = Task(TaskName="ASC/RB/WIS Work Instructions (move to NPI)", team=Team9)
            # Task20_Team9.save()
            # Task21_Team9 = Task (TaskName = "Etching requirement Document", team = Team9)
            # Task21_Team9.save()
            # Task22_Team9 = Task(TaskName="New Feature Test method (i.e, Force Touch Tool)", team=Team9)
            # Task22_Team9.save()
            # Task23_Team9 = Task(TaskName="IMEI Write (TMAX) Tool Verification", team=Team9)
            # Task23_Team9.save()
            # Task24_Team9 = Task(TaskName="IMEI Write (GSPN) Tool Verification", team=Team9)
            # Task24_Team9.save()
            # Task25_Team9 = Task(TaskName="IMEI Check (TMAX) Tool Verification", team=Team9)
            # Task25_Team9.save()
            # Task26_Team9 = Task(TaskName="IMEI Check (GSPN) Tool Verification", team=Team9)
            # Task26_Team9.save()
            # Task27_Team9 = Task(TaskName="SW Download (TMAX) Tool Verification", team=Team9)
            # Task27_Team9.save()
            # Task28_Team9 = Task(TaskName="FRP Unlock Tool Verification", team=Team9)
            # Task28_Team9.save()
            # Task29_Team9 = Task(TaskName="U400 Verification", team=Team9)
            # Task29_Team9.save()
            # Task30_Team9 = Task(TaskName="RF Test Verification", team=Team9)
            # Task30_Team9.save()
            # Task31_Team9 = Task(TaskName="RF cal/adjust tool verification", team=Team9)
            # Task31_Team9.save()
            # Task32_Team9 = Task(TaskName="Carrier Requirements", team=Team9)
            # Task32_Team9.save()
            # Task33_Team9 = Task(TaskName="WPC Test Verification", team=Team9)
            # Task33_Team9.save()
            # Task34_Team9 = Task(TaskName="Barometer/WRT Test Verification", team=Team9)
            # Task34_Team9.save()
            # Task35_Team9 = Task(TaskName="Galaxy Diagnostics Verification", team=Team9)
            # Task35_Team9.save()
            # Task36_Team9 = Task(TaskName="Fenrir Verification", team=Team9)
            # Task36_Team9.save()
            # Task37_Team9 = Task(TaskName="Etching Verification", team=Team9)
            # Task37_Team9.save()
            # Task38_Team9 = Task(TaskName="Document Upload", team=Team9)
            # Task38_Team9.save()
            # Task39_Team9 = Task(TaskName="Tooling Upload to GSPN (Tooling Distribution to ASC)", team=Team9)
            # Task39_Team9.save()
            # Task40_Team9 = Task(TaskName="SW Upload", team=Team9)
            # Task40_Team9.save()
            # Task41_Team9 = Task (TaskName = "AT&T PreFai Support", team = Team9)
            # Task41_Team9.save()
            #
            # Task1_Team10 = Task (TaskName = "verify parts forcasting for S8 as base", team = Team10)
            # Task1_Team10.save()
            # Task2_Team10 = Task(TaskName="HQ Validation of galaxy S8 forecast", team=Team10)
            # Task2_Team10.save()
            # Task3_Team10 = Task(TaskName="HQ to provide SBOM with part samples to Engineering for validation", team=Team10)
            # Task3_Team10.save()
            #
            # Task1_Team11 = Task (TaskName = "WIS Troubleshooting Training", team = Team11)
            # Task1_Team11.save()
            # Task2_Team11 = Task(TaskName="WIS/BBY Training Creation", team=Team11)
            # Task2_Team11.save()
            # Task3_Team11 = Task(TaskName="WIS/BBY Repair Training Delivery", team=Team11)
            # Task3_Team11.save()
            # Task4_Team11 = Task(TaskName="Jig Delivery for WIS(CSP,BBY)", team=Team11)
            # Task4_Team11.save()
            # Task5_Team11 = Task(TaskName="BBY Tooling setup", team=Team11)
            # Task5_Team11.save()
            # Task6_Team11 = Task(TaskName="WIS Tooling Setup", team=Team11)
            # Task6_Team11.save()
            #
            # Task1_Team12 = Task (TaskName = "Verify Advanced Exchange order", team = Team12)
            # Task1_Team12.save()
            # Task2_Team12 = Task(TaskName="Create PUMI", team=Team12)
            # Task2_Team12.save()
            # Task3_Team12 = Task(TaskName="PUMI Approved", team=Team12)
            # Task3_Team12.save()
            # Task4_Team12 = Task(TaskName="Order Advanced Exchange Inventory", team=Team12)
            # Task4_Team12.save()
            # Task5_Team12 = Task(TaskName="AE Inventory Received", team=Team12)
            # Task5_Team12.save()
            #
            # Task1_Team13 = Task (TaskName = "LDU Order", team = Team13)
            # Task1_Team13.save()
            # Task2_Team13 = Task(TaskName="Receive BBY LDU Units", team=Team13)
            # Task2_Team13.save()
            # Task3_Team13 = Task(TaskName="Receive WIS LDU Units", team=Team13)
            # Task3_Team13.save()
            # Task4_Team13 = Task(TaskName="WIS Training Content/SOPs", team=Team13)
            # Task4_Team13.save()
            # Task5_Team13 = Task(TaskName="BBY Training Content/SOPs", team=Team13)
            # Task5_Team13.save()
            #
            # Task1_Team14 = Task (TaskName = "Doc review: Training Manual", team = Team14)
            # Task1_Team14.save()
            # Task2_Team14 = Task(TaskName="BBY-TEC(SES) Training", team=Team14)
            # Task2_Team14.save()
            # Task3_Team14 = Task(TaskName="Create Tech Training content", team=Team14)
            # Task3_Team14.save()
            # Task4_Team14 = Task(TaskName="Create/update eLearning content", team=Team14)
            # Task4_Team14.save()
            # Task5_Team14 = Task(TaskName="DREAM Technical Training - Internal", team=Team14)
            # Task5_Team14.save()
            # Task6_Team14 = Task(TaskName="DREAM Technical Training - Pratners", team=Team14)
            # Task6_Team14.save()
            # Task7_Team14 = Task(TaskName="Traiing Materials Provided to WIS,BBY and L&R", team=Team14)
            # Task7_Team14.save()
            #
            # Task1_Team15 = Task (TaskName = "Initial Parts Preparation (Request HQ fir SVC reservation)", team = Team15)
            # Task1_Team15.save()
            # Task2_Team15 = Task(TaskName="BOM Creation", team=Team15)
            # Task2_Team15.save()
            # Task3_Team15 = Task(TaskName="Initial Parts Order to Vendors", team=Team15)
            # Task3_Team15.save()
            # Task4_Team15 = Task(TaskName="RB/ASC Jig Part Codes", team=Team15)
            # Task4_Team15.save()
            # Task5_Team15 = Task(TaskName="Jig pricing", team=Team15)
            # Task5_Team15.save()
            # Task6_Team15 = Task(TaskName="Initial Parts Order Receipt", team=Team15)
            # Task6_Team15.save()
            # Task7_Team15 = Task(TaskName="HQ to Provide SBOM with part samples to Engineering for validation", team=Team15)
            # Task7_Team15.save()
            # Task8_Team15 = Task(TaskName="Parts Pricing(ASC,WIS)", team=Team15)
            # Task8_Team15.save()
            # Task9_Team15 = Task(TaskName="Initial Parts Orders to SEA from WIS(At least 2 weeks volume)", team=Team15)
            # Task9_Team15.save()
            # Task10_Team15 = Task(TaskName="Initial Parts Orders to SEA from BBY(At least 2 weeks volume)", team=Team15)
            # Task10_Team15.save()
            # Task11_Team15 = Task(TaskName="Initial Parts Orders to SEA from Mail-in(At least 2 weeks volume)", team=Team15)
            # Task11_Team15.save()
            # Task12_Team15 = Task(TaskName="Initial ASC Parts Orders to SEA", team=Team15)
            # Task12_Team15.save()
            # Task13_Team15 = Task(TaskName="Initial Parts Orders at Mail-in", team=Team15)
            # Task13_Team15.save()
            # Task14_Team15 = Task(TaskName="Initial Parts Orders at Carrier ASC Locations", team=Team15)
            # Task14_Team15.save()
            # Task15_Team15 = Task(TaskName="Initial Parts Orders at WIS Locations", team=Team15)
            # Task15_Team15.save()
            # Task16_Team15 = Task(TaskName="Initial Parts Orders at BBY SES Locations", team=Team15)
            # Task16_Team15.save()
            #
            # Task1_Team16 = Task (TaskName = "Training Material", team = Team16)
            # Task1_Team16.save()
            # Task2_Team16 = Task(TaskName="TMO Training Delivery", team=Team16)
            # Task2_Team16.save()
            # Task3_Team16 = Task(TaskName="Verizon Training Delivery", team=Team16)
            # Task3_Team16.save()
            # Task4_Team16 = Task(TaskName="AT&T Training Delivery", team=Team16)
            # Task4_Team16.save()
            # Task5_Team16 = Task(TaskName="Sprint Training Delivery", team=Team16)
            # Task5_Team16.save()
            # Task6_Team16 = Task(TaskName="Tracfone Training Delivery", team=Team16)
            # Task6_Team16.save()
            # Task7_Team16 = Task(TaskName="USC Training Delivery", team=Team16)
            # Task7_Team16.save()
            # Task8_Team16 = Task(TaskName="TMO Seed Stock Order", team=Team16)
            # Task8_Team16.save()
            # Task9_Team16 = Task(TaskName="TMO Seed Stock Receipt at Carrier", team=Team16)
            # Task9_Team16.save()
            # Task10_Team16 = Task(TaskName="VZW Seed Stock Order", team=Team16)
            # Task10_Team16.save()
            # Task11_Team16 = Task(TaskName="VZW Seed Stock Receipt at Carrier", team=Team16)
            # Task11_Team16.save()
            # Task12_Team16 = Task(TaskName="SPR Seed Stock Order", team=Team16)
            # Task12_Team16.save()
            # Task13_Team16 = Task(TaskName="SPR Seed Stock Receipt at Carrier", team=Team16)
            # Task13_Team16.save()
            # Task14_Team16 = Task(TaskName="AT&T Seed Stock Order", team=Team16)
            # Task14_Team16.save()
            # Task15_Team16 = Task(TaskName="AT&T Seed Stock Receipt at Carrier", team=Team16)
            # Task15_Team16.save()
            # Task16_Team16 = Task(TaskName="USC Seed Stock Order", team=Team16)
            # Task16_Team16.save()
            # Task17_Team16 = Task(TaskName="USC Seed Stock Receipt at Carrier", team=Team16)
            # Task17_Team16.save()
            #
            # Task1_Team17 = Task (TaskName = "First Article Inspection - AT&T - Dream 1", team = Team17)
            # Task1_Team17.save()
            # Task2_Team17 = Task(TaskName="First Article Inspection- AT&T - Dream 2", team=Team17)
            # Task2_Team17.save()
            # Task3_Team17 = Task(TaskName="First Article Inspection - Cricket - Dream 1", team=Team17)
            # Task3_Team17.save()
            # Task4_Team17 = Task(TaskName="First Article Inspection - TMO - Dream 1", team=Team17)
            # Task4_Team17.save()
            # Task5_Team17 = Task(TaskName="First Article Inspection - TMO - Dream 2", team=Team17)
            # Task5_Team17.save()
            # Task6_Team17 = Task(TaskName="First Article Inspection - Metro - Dream 1", team=Team17)
            # Task6_Team17.save()
            # Task7_Team17 = Task(TaskName="First Article Inspection - Sprint - Dream 1", team=Team17)
            # Task7_Team17.save()
            # Task8_Team17 = Task(TaskName="First Article Inspection - Sprint - Dream 2", team=Team17)
            # Task8_Team17.save()
            # Task9_Team17 = Task(TaskName="First Article Inspection - Verizon - Dream 1", team=Team17)
            # Task9_Team17.save()
            # Task10_Team17 = Task(TaskName="First Article Inspection - Verizon - Dream2", team=Team17)
            # Task10_Team17.save()
            # Task11_Team17 = Task(TaskName="First Article Inspection - USC - Dream 1", team=Team17)
            # Task11_Team17.save()
            # Task12_Team17 = Task(TaskName="Ship Approval", team=Team17)
            # Task12_Team17.save()
            #
            # Task1_Team18 = Task (TaskName = "Product Design", team = Team18)
            # Task1_Team18.save()
            # Task2_Team18 = Task(TaskName="Pricing", team=Team18)
            # Task2_Team18.save()
            # Task3_Team18 = Task(TaskName="Contracts/Vendor Agreement", team=Team18)
            # Task3_Team18.save()
            # Task4_Team18 = Task(TaskName="Monthly Pay", team=Team18)
            # Task4_Team18.save()
            # Task5_Team18 = Task(TaskName="Sales Channels", team=Team18)
            # Task5_Team18.save()
            # Task6_Team18 = Task(TaskName="Samsung + Visibility", team=Team18)
            # Task6_Team18.save()
            # Task7_Team18 = Task(TaskName="WCTU Swap", team=Team18)
            # Task7_Team18.save()
            # Task8_Team18 = Task(TaskName="Call Center Support Readiness", team=Team18)
            # Task8_Team18.save()
            # Task9_Team18 = Task(TaskName="Aftermarket SPP Mobile", team=Team18)
            # Task9_Team18.save()
            # Task10_Team18 = Task(TaskName="Assign Service Pack Code (SKU)", team=Team18)
            # Task10_Team18.save()
            # Task11_Team18 = Task(TaskName="Pricing from Assurant", team=Team18)
            # Task11_Team18.save()
            # Task12_Team18 = Task(TaskName="Add model to SPP Landing/ Product Detail Pages", team=Team18)
            # Task12_Team18.save()
            # Task13_Team18 = Task(TaskName="Add model to training matierial for call center agents", team=Team18)
            # Task13_Team18.save()
            # Task14_Team18 = Task(TaskName="Seed stock for Assurant to order", team=Team18)
            # Task14_Team18.save()
            # Task15_Team18 = Task(TaskName="Repair Cost", team=Team18)
            # Task15_Team18.save()
            #
            # Task1_Team19 = Task (TaskName = "EPL Group PL refresher Activity", team = Team19)
            # Task1_Team19.save()
            # Task2_Team19 = Task(TaskName="Walk-in & Repair Center Escalation Guide", team=Team19)
            # Task2_Team19.save()
            # Task3_Team19 = Task(TaskName="REVO STT PL Call Sensing", team=Team19)
            # Task3_Team19.save()
            # Task4_Team19 = Task(TaskName="WeGOLook Pickup & Express Service", team=Team19)
            # Task4_Team19.save()
            # Task5_Team19 = Task(TaskName="DREAM Analysis Training in HQ", team=Team19)
            # Task5_Team19.save()
            # Task6_Team19 = Task(TaskName="8 Point Battery Test Training in HQ", team=Team19)
            # Task6_Team19.save()
            # Task7_Team19 = Task(TaskName="Dallas PL Lab capacity Review", team=Team19)
            # Task7_Team19.save()
            # Task8_Team19 = Task(TaskName="TF team from HQ (Pl Engineers)", team=Team19)
            # Task8_Team19.save()
            # Task9_Team19 = Task(TaskName="Reporting channel alignment on weekly PL/CS report", team=Team19)
            # Task9_Team19.save()
            # Task10_Team19 = Task(TaskName="Comprehensive Script for PR/Legal", team=Team19)
            # Task10_Team19.save()
            # Task11_Team19 = Task(TaskName="Lithium Social Web PL SNS Sensing", team=Team19)
            # Task11_Team19.save()
            # Task12_Team19 = Task(TaskName="GPLS Reporting early Lunch", team=Team19)
            # Task12_Team19.save()
            #
            # Task1_Team20 = Task (TaskName = "New Offer Readiness", team = Team20)
            # Task1_Team20.save()
            # Task2_Team20 = Task(TaskName="System Readiness", team=Team20)
            # Task2_Team20.save()
            # Task3_Team20 = Task(TaskName="Agent Training", team=Team20)
            # Task3_Team20.save()
            return redirect('/admin/mobile/specialproduct/')


class ProductView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = ('mobile.is_strategic')
    template_name = 'mobile/summary.html'
    raise_exception = True
    # login_url = '/login/auth/'
    def get(self, request):
        devices = SpecialProduct.objects.all().order_by("LaunchDate")
        try:
            device_latest = SpecialProduct.objects.order_by('-id')[0]
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
        announcement = 1
        try:
            announcement = Announcements.objects.order_by("-id")[0]
        except:
            print ("Error")
        else:
            print(announcement.post)


        args = {'Device': devices, 'teams':teams, 'announcement':announcement}
        return render (request, self.template_name, args, )

class IntermediateView(LoginRequiredMixin,PermissionRequiredMixin,TemplateView):
    permission_required = ('mobile.is_strategic')
    template_name = 'mobile/intermediate.html'
    raise_exception = True

    def get(self, request, pk):
        devices = SpecialProduct.objects.get(pk=pk)
        teams = devices.team_set.all().order_by('id')
        args = {'devices':devices, 'teams':teams}
        return render(request, self.template_name, args )

class DetailView (LoginRequiredMixin,PermissionRequiredMixin,TemplateView):
    permission_required = ('mobile.is_strategic')
    template_name = 'mobile/detail.html'
    raise_exception = True

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
                    return redirect('/mobile/teams/' + id)
                else:
                    return redirect('/mobile/teams/' + id)
            counter = counter +1
        print("came out of the loop")
        return redirect('/mobile/teams/' + id)
