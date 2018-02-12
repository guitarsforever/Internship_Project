from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from . import extra_utils
from django.contrib.auth.decorators import user_passes_test
from login.forms import (
    RegistrationForm,
Task1_pr_form, Task2_pr_form,
    Task3_pr_form, Task4_pr_form ,Task5_pr_form , Task6_pr_form, Task7_pr_form, Task8_pr_form, Task9_pr_form,
    Task10_pr_form, Task11_pr_form, Task12_pr_form, Task13_pr_form, Task14_pr_form, Task15_pr_form, Task16_pr_form,
    Task17_pr_form, Task18_pr_form, Task19_pr_form, Task20_pr_form, Task1_pr_date_form, Task2_pr_date_form, Task3_pr_date_form,
    Task4_pr_date_form, Task5_pr_date_form, Task6_pr_date_form, Task7_pr_date_form, Task8_pr_date_form, Task9_pr_date_form,
    Task10_pr_date_form, Task11_pr_date_form, Task12_pr_date_form, Task13_pr_date_form, Task14_pr_date_form,
    Task15_pr_date_form, Task16_pr_date_form, Task17_pr_date_form, Task18_pr_date_form, Task19_pr_date_form,
    Task20_pr_date_form,
    Task1_vc_form, Task2_vc_form,
    Task3_vc_form, Task4_vc_form ,Task5_vc_form , Task6_vc_form, Task7_vc_form, Task8_vc_form, Task9_vc_form,
    Task10_vc_form, Task11_vc_form, Task12_vc_form, Task13_vc_form, Task14_vc_form, Task15_vc_form, Task16_vc_form,
    Task17_vc_form, Task18_vc_form, Task19_vc_form, Task20_vc_form, Task1_vc_date_form, Task2_vc_date_form, Task3_vc_date_form,
    Task4_vc_date_form, Task5_vc_date_form, Task6_vc_date_form, Task7_vc_date_form, Task8_vc_date_form, Task9_vc_date_form,
    Task10_vc_date_form, Task11_vc_date_form, Task12_vc_date_form, Task13_vc_date_form, Task14_vc_date_form,
    Task15_vc_date_form, Task16_vc_date_form, Task17_vc_date_form, Task18_vc_date_form, Task19_vc_date_form,
    Task20_vc_date_form,
    Task1_dc_form, Task2_dc_form,
    Task3_dc_form, Task4_dc_form ,Task5_dc_form , Task6_dc_form, Task7_dc_form, Task8_dc_form, Task9_dc_form,
    Task10_dc_form, Task11_dc_form, Task12_dc_form, Task13_dc_form, Task14_dc_form, Task15_dc_form, Task16_dc_form,
    Task17_dc_form, Task18_dc_form, Task19_dc_form, Task20_dc_form, Task1_dc_date_form, Task2_dc_date_form, Task3_dc_date_form,
    Task4_dc_date_form, Task5_dc_date_form, Task6_dc_date_form, Task7_dc_date_form, Task8_dc_date_form, Task9_dc_date_form,
    Task10_dc_date_form, Task11_dc_date_form, Task12_dc_date_form, Task13_dc_date_form, Task14_dc_date_form,
    Task15_dc_date_form, Task16_dc_date_form, Task17_dc_date_form, Task18_dc_date_form, Task19_dc_date_form,
    Task20_dc_date_form,
    Task1_cct_form, Task2_cct_form,
    Task3_cct_form, Task4_cct_form, Task5_cct_form, Task6_cct_form, Task7_cct_form, Task8_cct_form, Task9_cct_form,
    Task10_cct_form, Task11_cct_form, Task12_cct_form, Task13_cct_form, Task14_cct_form, Task15_cct_form, Task16_cct_form,
    Task17_cct_form, Task18_cct_form, Task19_cct_form, Task20_cct_form, Task1_cct_date_form, Task2_cct_date_form,
    Task3_cct_date_form,
    Task4_cct_date_form, Task5_cct_date_form, Task6_cct_date_form, Task7_cct_date_form, Task8_cct_date_form,
    Task9_cct_date_form,
    Task10_cct_date_form, Task11_cct_date_form, Task12_cct_date_form, Task13_cct_date_form, Task14_cct_date_form,
    Task15_cct_date_form, Task16_cct_date_form, Task17_cct_date_form, Task18_cct_date_form, Task19_cct_date_form,
    Task20_cct_date_form,
    Task1_cco_form, Task2_cco_form,
    Task3_cco_form, Task4_cco_form, Task5_cco_form, Task6_cco_form, Task7_cco_form, Task8_cco_form, Task9_cco_form,
    Task10_cco_form, Task11_cco_form, Task12_cco_form, Task13_cco_form, Task14_cco_form, Task15_cco_form,
    Task16_cco_form,
    Task17_cco_form, Task18_cco_form, Task19_cco_form, Task20_cco_form, Task1_cco_date_form, Task2_cco_date_form,
    Task3_cco_date_form,
    Task4_cco_date_form, Task5_cco_date_form, Task6_cco_date_form, Task7_cco_date_form, Task8_cco_date_form,
    Task9_cco_date_form,
    Task10_cco_date_form, Task11_cco_date_form, Task12_cco_date_form, Task13_cco_date_form, Task14_cco_date_form,
    Task15_cco_date_form, Task16_cco_date_form, Task17_cco_date_form, Task18_cco_date_form, Task19_cco_date_form,
    Task20_cco_date_form,
    Task1_ps_form, Task2_ps_form,
    Task3_ps_form, Task4_ps_form, Task5_ps_form, Task6_ps_form, Task7_ps_form, Task8_ps_form, Task9_ps_form,
    Task10_ps_form, Task11_ps_form, Task12_ps_form, Task13_ps_form, Task14_ps_form, Task15_ps_form,
    Task16_ps_form,
    Task17_ps_form, Task18_ps_form, Task19_ps_form, Task20_ps_form, Task1_ps_date_form, Task2_ps_date_form,
    Task3_ps_date_form,
    Task4_ps_date_form, Task5_ps_date_form, Task6_ps_date_form, Task7_ps_date_form, Task8_ps_date_form,
    Task9_ps_date_form,
    Task10_ps_date_form, Task11_ps_date_form, Task12_ps_date_form, Task13_ps_date_form, Task14_ps_date_form,
    Task15_ps_date_form, Task16_ps_date_form, Task17_ps_date_form, Task18_ps_date_form, Task19_ps_date_form,
    Task20_ps_date_form,
    Task1_w_form, Task2_w_form,
    Task3_w_form, Task4_w_form, Task5_w_form, Task6_w_form, Task7_w_form, Task8_w_form, Task9_w_form,
    Task10_w_form, Task11_w_form, Task12_w_form, Task13_w_form, Task14_w_form, Task15_w_form,
    Task16_w_form,
    Task17_w_form, Task18_w_form, Task19_w_form, Task20_w_form, Task1_w_date_form, Task2_w_date_form,
    Task3_w_date_form,
    Task4_w_date_form, Task5_w_date_form, Task6_w_date_form, Task7_w_date_form, Task8_w_date_form,
    Task9_w_date_form,
    Task10_w_date_form, Task11_w_date_form, Task12_w_date_form, Task13_w_date_form, Task14_w_date_form,
    Task15_w_date_form, Task16_w_date_form, Task17_w_date_form, Task18_w_date_form, Task19_w_date_form,
    Task20_w_date_form,
    Task1_fs_form, Task2_fs_form,
    Task3_fs_form, Task4_fs_form, Task5_fs_form, Task6_fs_form, Task7_fs_form, Task8_fs_form, Task9_fs_form,
    Task10_fs_form, Task11_fs_form, Task12_fs_form, Task13_fs_form, Task14_fs_form, Task15_fs_form,
    Task16_fs_form,
    Task17_fs_form, Task18_fs_form, Task19_fs_form, Task20_fs_form, Task1_fs_date_form, Task2_fs_date_form,
    Task3_fs_date_form,
    Task4_fs_date_form, Task5_fs_date_form, Task6_fs_date_form, Task7_fs_date_form, Task8_fs_date_form,
    Task9_fs_date_form,
    Task10_fs_date_form, Task11_fs_date_form, Task12_fs_date_form, Task13_fs_date_form, Task14_fs_date_form,
    Task15_fs_date_form, Task16_fs_date_form, Task17_fs_date_form, Task18_fs_date_form, Task19_fs_date_form,
    Task20_fs_date_form,
    Task1_ts_form, Task2_ts_form,
    Task3_ts_form, Task4_ts_form, Task5_ts_form, Task6_ts_form, Task7_ts_form, Task8_ts_form, Task9_ts_form,
    Task10_ts_form, Task11_ts_form, Task12_ts_form, Task13_ts_form, Task14_ts_form, Task15_ts_form,
    Task16_ts_form,
    Task17_ts_form, Task18_ts_form, Task19_ts_form, Task20_ts_form, Task1_ts_date_form, Task2_ts_date_form,
    Task3_ts_date_form,
    Task4_ts_date_form, Task5_ts_date_form, Task6_ts_date_form, Task7_ts_date_form, Task8_ts_date_form,
    Task9_ts_date_form,
    Task10_ts_date_form, Task11_ts_date_form, Task12_ts_date_form, Task13_ts_date_form, Task14_ts_date_form,
    Task15_ts_date_form, Task16_ts_date_form, Task17_ts_date_form, Task18_ts_date_form, Task19_ts_date_form,
    Task20_ts_date_form,
    Task1_sm_form, Task2_sm_form,
    Task3_sm_form, Task4_sm_form, Task5_sm_form, Task6_sm_form, Task7_sm_form, Task8_sm_form, Task9_sm_form,
    Task10_sm_form, Task11_sm_form, Task12_sm_form, Task13_sm_form, Task14_sm_form, Task15_sm_form,
    Task16_sm_form,
    Task17_sm_form, Task18_sm_form, Task19_sm_form, Task20_sm_form, Task1_sm_date_form, Task2_sm_date_form,
    Task3_sm_date_form,
    Task4_sm_date_form, Task5_sm_date_form, Task6_sm_date_form, Task7_sm_date_form, Task8_sm_date_form,
    Task9_sm_date_form,
    Task10_sm_date_form, Task11_sm_date_form, Task12_sm_date_form, Task13_sm_date_form, Task14_sm_date_form,
    Task15_sm_date_form, Task16_sm_date_form, Task17_sm_date_form, Task18_sm_date_form, Task19_sm_date_form,
    Task20_sm_date_form,
    Task1_st_form, Task2_st_form,
    Task3_st_form, Task4_st_form, Task5_st_form, Task6_st_form, Task7_st_form, Task8_st_form, Task9_st_form,
    Task10_st_form, Task11_st_form, Task12_st_form, Task13_st_form, Task14_st_form, Task15_st_form,
    Task16_st_form,
    Task17_st_form, Task18_st_form, Task19_st_form, Task20_st_form, Task1_st_date_form, Task2_st_date_form,
    Task3_st_date_form,
    Task4_st_date_form, Task5_st_date_form, Task6_st_date_form, Task7_st_date_form, Task8_st_date_form,
    Task9_st_date_form,
    Task10_st_date_form, Task11_st_date_form, Task12_st_date_form, Task13_st_date_form, Task14_st_date_form,
    Task15_st_date_form, Task16_st_date_form, Task17_st_date_form, Task18_st_date_form, Task19_st_date_form,
    Task20_st_date_form,
    Task1_p_form, Task2_p_form,
    Task3_p_form, Task4_p_form, Task5_p_form, Task6_p_form, Task7_p_form, Task8_p_form, Task9_p_form,
    Task10_p_form, Task11_p_form, Task12_p_form, Task13_p_form, Task14_p_form, Task15_p_form,
    Task16_p_form,
    Task17_p_form, Task18_p_form, Task19_p_form, Task20_p_form, Task1_p_date_form, Task2_p_date_form,
    Task3_p_date_form,
    Task4_p_date_form, Task5_p_date_form, Task6_p_date_form, Task7_p_date_form, Task8_p_date_form,
    Task9_p_date_form,
    Task10_p_date_form, Task11_p_date_form, Task12_p_date_form, Task13_p_date_form, Task14_p_date_form,
    Task15_p_date_form, Task16_p_date_form, Task17_p_date_form, Task18_p_date_form, Task19_p_date_form,
    Task20_p_date_form,
)
from django.views.generic import TemplateView, ListView
from login.models import (
    Device,videocontent, digitalcontent, Announcements,reference,test, ProductReadiness,
callcentertraining, callcenteropertaions, productsupport, warehouse, fieldservice, techsupport, servicemarketing,
servicetraining, parts, DashboardControlDevice, ProductReadinessHistory
)
import array
import datetime
from datetime import timedelta
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

def home (request):
    numbers = [1,2,3,4,5]
    name = 'Shreyas Rao'
    args = {'myName': name, 'myNumbers': numbers}
    return render(request, 'login/home.html',args)

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/auth')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'login/reg_form.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('login:view_profile'))
        else:
            return redirect(reverse('login:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'login/change_password.html', args)

class DeviceSummaryPRView(LoginRequiredMixin,TemplateView):
    template_name = 'login/teamsummaryPR.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        device = Device.objects.all().order_by("LaunchDate")
        MainDevices = DashboardControlDevice.objects.all().order_by("id")
        selectedDevice = Device.objects.get(pk=pk)
        PRHistory = selectedDevice.productreadinesshistory_set.all().order_by("Created")
        createdHistory = []
        DelayedHistory = []
        CompletedHistory = []
        DueSoonHistory = []
        OntimeHistory = []
        for History in PRHistory:
            createdHistory.append('Week #' + str(History.Created.isocalendar()[1]) + ', ' + History.Created.strftime('%B') )
            DelayedHistory.append(float(History.Delayed))
            CompletedHistory.append(float(History.Completed))
            DueSoonHistory.append(float(History.DueSoon))
            OntimeHistory.append(float(History.OnTime))
        zipped_data = extra_utils.delayedElements(selectedDevice)
        Delayed = []
        Completed = []
        DueSoon = []
        OnTime = []
        for i, j, k, l in zipped_data:
            Total = i + j + k + l
            if Total != 0:
                PercentI = round(((i / Total) * 100), 2)
                PercentJ = round(((j / Total) * 100), 2)
                PercentK = round(((k / Total) * 100), 2)
                PercentL = round(((l / Total) * 100), 2)
                Completed.append(PercentI)
                Delayed.append(PercentJ)
                DueSoon.append(PercentK)
                OnTime.append(PercentL)

                print (i, j, k, l)
            else:
                Completed.append(0)
                Delayed.append(0)
                DueSoon.append(0)
                OnTime.append(0)
        args = {'Device':device, 'MainDevices':MainDevices,'selectedDevice':selectedDevice, 'Delayed':Delayed, 'Completed':Completed, 'DueSoon':DueSoon,
                'OnTime':OnTime, 'createdHistory':createdHistory, 'DelayedHistory':DelayedHistory, 'CompletedHistory':CompletedHistory,
                'DueSoonHistory':DueSoonHistory, 'OntimeHistory':OntimeHistory}
        return render(request, self.template_name, args )

class DeviceSummaryVCView(LoginRequiredMixin,TemplateView):
    template_name = 'login/teamsummaryVC.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        device = Device.objects.all().order_by("LaunchDate")
        MainDevices = DashboardControlDevice.objects.all().order_by("id")
        selectedDevice = Device.objects.get(pk=pk)
        PRHistory = selectedDevice.videocontenthistory_set.all().order_by("Created")
        createdHistory = []
        DelayedHistory = []
        CompletedHistory = []
        DueSoonHistory = []
        OntimeHistory = []
        for History in PRHistory:
            createdHistory.append('Week #' + str(History.Created.isocalendar()[1]) + ', ' + History.Created.strftime('%B') )
            DelayedHistory.append(float(History.Delayed))
            CompletedHistory.append(float(History.Completed))
            DueSoonHistory.append(float(History.DueSoon))
            OntimeHistory.append(float(History.OnTime))
        zipped_data = extra_utils.delayedElements(selectedDevice)
        Delayed = []
        Completed = []
        DueSoon = []
        OnTime = []
        for i, j, k, l in zipped_data:
            Total = i + j + k + l
            if Total != 0:
                PercentI = round(((i / Total) * 100), 2)
                PercentJ = round(((j / Total) * 100), 2)
                PercentK = round(((k / Total) * 100), 2)
                PercentL = round(((l / Total) * 100), 2)
                Completed.append(PercentI)
                Delayed.append(PercentJ)
                DueSoon.append(PercentK)
                OnTime.append(PercentL)

                print (i, j, k, l)
            else:
                Completed.append(0)
                Delayed.append(0)
                DueSoon.append(0)
                OnTime.append(0)
        args = {'Device':device, 'MainDevices':MainDevices,'selectedDevice':selectedDevice, 'Delayed':Delayed, 'Completed':Completed, 'DueSoon':DueSoon,
                'OnTime':OnTime, 'createdHistory':createdHistory, 'DelayedHistory':DelayedHistory, 'CompletedHistory':CompletedHistory,
                'DueSoonHistory':DueSoonHistory, 'OntimeHistory':OntimeHistory}
        return render(request, self.template_name, args )

class DeviceSummaryDCView(LoginRequiredMixin,TemplateView):
    template_name = 'login/teamsummaryDC.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        device = Device.objects.all().order_by("LaunchDate")
        MainDevices = DashboardControlDevice.objects.all().order_by("id")
        selectedDevice = Device.objects.get(pk=pk)
        PRHistory = selectedDevice.digitalcontenthistory_set.all().order_by("Created")
        createdHistory = []
        DelayedHistory = []
        CompletedHistory = []
        DueSoonHistory = []
        OntimeHistory = []
        for History in PRHistory:
            createdHistory.append('Week #' + str(History.Created.isocalendar()[1]) + ', ' + History.Created.strftime('%B') )
            DelayedHistory.append(float(History.Delayed))
            CompletedHistory.append(float(History.Completed))
            DueSoonHistory.append(float(History.DueSoon))
            OntimeHistory.append(float(History.OnTime))
        zipped_data = extra_utils.delayedElements(selectedDevice)
        Delayed = []
        Completed = []
        DueSoon = []
        OnTime = []
        for i, j, k, l in zipped_data:
            Total = i + j + k + l
            if Total != 0:
                PercentI = round(((i / Total) * 100), 2)
                PercentJ = round(((j / Total) * 100), 2)
                PercentK = round(((k / Total) * 100), 2)
                PercentL = round(((l / Total) * 100), 2)
                Completed.append(PercentI)
                Delayed.append(PercentJ)
                DueSoon.append(PercentK)
                OnTime.append(PercentL)

                print (i, j, k, l)
            else:
                Completed.append(0)
                Delayed.append(0)
                DueSoon.append(0)
                OnTime.append(0)
        args = {'Device':device, 'MainDevices':MainDevices,'selectedDevice':selectedDevice, 'Delayed':Delayed, 'Completed':Completed, 'DueSoon':DueSoon,
                'OnTime':OnTime, 'createdHistory':createdHistory, 'DelayedHistory':DelayedHistory, 'CompletedHistory':CompletedHistory,
                'DueSoonHistory':DueSoonHistory, 'OntimeHistory':OntimeHistory}
        return render(request, self.template_name, args )

class DeviceSummaryCCTView(LoginRequiredMixin,TemplateView):
    template_name = 'login/teamsummaryCCT.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        device = Device.objects.all().order_by("LaunchDate")
        MainDevices = DashboardControlDevice.objects.all().order_by("id")
        selectedDevice = Device.objects.get(pk=pk)
        PRHistory = selectedDevice.callcentertraininghistory_set.all().order_by("Created")
        createdHistory = []
        DelayedHistory = []
        CompletedHistory = []
        DueSoonHistory = []
        OntimeHistory = []
        for History in PRHistory:
            createdHistory.append('Week #' + str(History.Created.isocalendar()[1]) + ', ' + History.Created.strftime('%B') )
            DelayedHistory.append(float(History.Delayed))
            CompletedHistory.append(float(History.Completed))
            DueSoonHistory.append(float(History.DueSoon))
            OntimeHistory.append(float(History.OnTime))
        zipped_data = extra_utils.delayedElements(selectedDevice)
        Delayed = []
        Completed = []
        DueSoon = []
        OnTime = []
        for i, j, k, l in zipped_data:
            Total = i + j + k + l
            if Total != 0:
                PercentI = round(((i / Total) * 100), 2)
                PercentJ = round(((j / Total) * 100), 2)
                PercentK = round(((k / Total) * 100), 2)
                PercentL = round(((l / Total) * 100), 2)
                Completed.append(PercentI)
                Delayed.append(PercentJ)
                DueSoon.append(PercentK)
                OnTime.append(PercentL)

                print (i, j, k, l)
            else:
                Completed.append(0)
                Delayed.append(0)
                DueSoon.append(0)
                OnTime.append(0)
        args = {'Device':device, 'MainDevices':MainDevices,'selectedDevice':selectedDevice, 'Delayed':Delayed, 'Completed':Completed, 'DueSoon':DueSoon,
                'OnTime':OnTime, 'createdHistory':createdHistory, 'DelayedHistory':DelayedHistory, 'CompletedHistory':CompletedHistory,
                'DueSoonHistory':DueSoonHistory, 'OntimeHistory':OntimeHistory}
        return render(request, self.template_name, args )

class DeviceSummaryCCOView(LoginRequiredMixin,TemplateView):
    template_name = 'login/teamsummaryCCO.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        device = Device.objects.all().order_by("LaunchDate")
        MainDevices = DashboardControlDevice.objects.all().order_by("id")
        selectedDevice = Device.objects.get(pk=pk)
        PRHistory = selectedDevice.callcenteroperationhistory_set.all().order_by("Created")
        createdHistory = []
        DelayedHistory = []
        CompletedHistory = []
        DueSoonHistory = []
        OntimeHistory = []
        for History in PRHistory:
            createdHistory.append('Week #' + str(History.Created.isocalendar()[1]) + ', ' + History.Created.strftime('%B') )
            DelayedHistory.append(float(History.Delayed))
            CompletedHistory.append(float(History.Completed))
            DueSoonHistory.append(float(History.DueSoon))
            OntimeHistory.append(float(History.OnTime))
        zipped_data = extra_utils.delayedElements(selectedDevice)
        Delayed = []
        Completed = []
        DueSoon = []
        OnTime = []
        for i, j, k, l in zipped_data:
            Total = i + j + k + l
            if Total != 0:
                PercentI = round(((i / Total) * 100), 2)
                PercentJ = round(((j / Total) * 100), 2)
                PercentK = round(((k / Total) * 100), 2)
                PercentL = round(((l / Total) * 100), 2)
                Completed.append(PercentI)
                Delayed.append(PercentJ)
                DueSoon.append(PercentK)
                OnTime.append(PercentL)

                print (i, j, k, l)
            else:
                Completed.append(0)
                Delayed.append(0)
                DueSoon.append(0)
                OnTime.append(0)
        args = {'Device':device, 'MainDevices':MainDevices,'selectedDevice':selectedDevice, 'Delayed':Delayed, 'Completed':Completed, 'DueSoon':DueSoon,
                'OnTime':OnTime, 'createdHistory':createdHistory, 'DelayedHistory':DelayedHistory, 'CompletedHistory':CompletedHistory,
                'DueSoonHistory':DueSoonHistory, 'OntimeHistory':OntimeHistory}
        return render(request, self.template_name, args )

class DeviceSummaryPSView(LoginRequiredMixin,TemplateView):
    template_name = 'login/teamsummaryPS.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        device = Device.objects.all().order_by("LaunchDate")
        MainDevices = DashboardControlDevice.objects.all().order_by("id")
        selectedDevice = Device.objects.get(pk=pk)
        PRHistory = selectedDevice.productsupporthistory_set.all().order_by("Created")
        createdHistory = []
        DelayedHistory = []
        CompletedHistory = []
        DueSoonHistory = []
        OntimeHistory = []
        for History in PRHistory:
            createdHistory.append('Week #' + str(History.Created.isocalendar()[1]) + ', ' + History.Created.strftime('%B') )
            DelayedHistory.append(float(History.Delayed))
            CompletedHistory.append(float(History.Completed))
            DueSoonHistory.append(float(History.DueSoon))
            OntimeHistory.append(float(History.OnTime))
        zipped_data = extra_utils.delayedElements(selectedDevice)
        Delayed = []
        Completed = []
        DueSoon = []
        OnTime = []
        for i, j, k, l in zipped_data:
            Total = i + j + k + l
            if Total != 0:
                PercentI = round(((i / Total) * 100), 2)
                PercentJ = round(((j / Total) * 100), 2)
                PercentK = round(((k / Total) * 100), 2)
                PercentL = round(((l / Total) * 100), 2)
                Completed.append(PercentI)
                Delayed.append(PercentJ)
                DueSoon.append(PercentK)
                OnTime.append(PercentL)

                print (i, j, k, l)
            else:
                Completed.append(0)
                Delayed.append(0)
                DueSoon.append(0)
                OnTime.append(0)
        args = {'Device':device, 'MainDevices':MainDevices,'selectedDevice':selectedDevice, 'Delayed':Delayed, 'Completed':Completed, 'DueSoon':DueSoon,
                'OnTime':OnTime, 'createdHistory':createdHistory, 'DelayedHistory':DelayedHistory, 'CompletedHistory':CompletedHistory,
                'DueSoonHistory':DueSoonHistory, 'OntimeHistory':OntimeHistory}
        return render(request, self.template_name, args )

class DeviceSummaryWView(LoginRequiredMixin,TemplateView):
    template_name = 'login/teamsummaryW.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        device = Device.objects.all().order_by("LaunchDate")
        MainDevices = DashboardControlDevice.objects.all().order_by("id")
        selectedDevice = Device.objects.get(pk=pk)
        PRHistory = selectedDevice.warehousehistory_set.all().order_by("Created")
        createdHistory = []
        DelayedHistory = []
        CompletedHistory = []
        DueSoonHistory = []
        OntimeHistory = []
        for History in PRHistory:
            createdHistory.append('Week #' + str(History.Created.isocalendar()[1]) + ', ' + History.Created.strftime('%B') )
            DelayedHistory.append(float(History.Delayed))
            CompletedHistory.append(float(History.Completed))
            DueSoonHistory.append(float(History.DueSoon))
            OntimeHistory.append(float(History.OnTime))
        zipped_data = extra_utils.delayedElements(selectedDevice)
        Delayed = []
        Completed = []
        DueSoon = []
        OnTime = []
        for i, j, k, l in zipped_data:
            Total = i + j + k + l
            if Total != 0:
                PercentI = round(((i / Total) * 100), 2)
                PercentJ = round(((j / Total) * 100), 2)
                PercentK = round(((k / Total) * 100), 2)
                PercentL = round(((l / Total) * 100), 2)
                Completed.append(PercentI)
                Delayed.append(PercentJ)
                DueSoon.append(PercentK)
                OnTime.append(PercentL)

                print (i, j, k, l)
            else:
                Completed.append(0)
                Delayed.append(0)
                DueSoon.append(0)
                OnTime.append(0)
        args = {'Device':device, 'MainDevices':MainDevices,'selectedDevice':selectedDevice, 'Delayed':Delayed, 'Completed':Completed, 'DueSoon':DueSoon,
                'OnTime':OnTime, 'createdHistory':createdHistory, 'DelayedHistory':DelayedHistory, 'CompletedHistory':CompletedHistory,
                'DueSoonHistory':DueSoonHistory, 'OntimeHistory':OntimeHistory}
        return render(request, self.template_name, args )

class DeviceSummaryFSView(LoginRequiredMixin,TemplateView):
    template_name = 'login/teamsummaryFS.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        device = Device.objects.all().order_by("LaunchDate")
        MainDevices = DashboardControlDevice.objects.all().order_by("id")
        selectedDevice = Device.objects.get(pk=pk)
        PRHistory = selectedDevice.fieldservicehistory_set.all().order_by("Created")
        createdHistory = []
        DelayedHistory = []
        CompletedHistory = []
        DueSoonHistory = []
        OntimeHistory = []
        for History in PRHistory:
            createdHistory.append('Week #' + str(History.Created.isocalendar()[1]) + ', ' + History.Created.strftime('%B') )
            DelayedHistory.append(float(History.Delayed))
            CompletedHistory.append(float(History.Completed))
            DueSoonHistory.append(float(History.DueSoon))
            OntimeHistory.append(float(History.OnTime))
        zipped_data = extra_utils.delayedElements(selectedDevice)
        Delayed = []
        Completed = []
        DueSoon = []
        OnTime = []
        for i, j, k, l in zipped_data:
            Total = i + j + k + l
            if Total != 0:
                PercentI = round(((i / Total) * 100), 2)
                PercentJ = round(((j / Total) * 100), 2)
                PercentK = round(((k / Total) * 100), 2)
                PercentL = round(((l / Total) * 100), 2)
                Completed.append(PercentI)
                Delayed.append(PercentJ)
                DueSoon.append(PercentK)
                OnTime.append(PercentL)

                print (i, j, k, l)
            else:
                Completed.append(0)
                Delayed.append(0)
                DueSoon.append(0)
                OnTime.append(0)
        args = {'Device':device, 'MainDevices':MainDevices,'selectedDevice':selectedDevice, 'Delayed':Delayed, 'Completed':Completed, 'DueSoon':DueSoon,
                'OnTime':OnTime, 'createdHistory':createdHistory, 'DelayedHistory':DelayedHistory, 'CompletedHistory':CompletedHistory,
                'DueSoonHistory':DueSoonHistory, 'OntimeHistory':OntimeHistory}

        return render(request, self.template_name, args )

class DeviceSummaryTSView(LoginRequiredMixin,TemplateView):
    template_name = 'login/teamsummaryTS.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        device = Device.objects.all().order_by("LaunchDate")
        MainDevices = DashboardControlDevice.objects.all().order_by("id")
        selectedDevice = Device.objects.get(pk=pk)
        PRHistory = selectedDevice.techsupporthistory_set.all().order_by("Created")
        createdHistory = []
        DelayedHistory = []
        CompletedHistory = []
        DueSoonHistory = []
        OntimeHistory = []
        for History in PRHistory:
            createdHistory.append('Week #' + str(History.Created.isocalendar()[1]) + ', ' + History.Created.strftime('%B') )
            DelayedHistory.append(float(History.Delayed))
            CompletedHistory.append(float(History.Completed))
            DueSoonHistory.append(float(History.DueSoon))
            OntimeHistory.append(float(History.OnTime))
        zipped_data = extra_utils.delayedElements(selectedDevice)
        Delayed = []
        Completed = []
        DueSoon = []
        OnTime = []
        for i, j, k, l in zipped_data:
            Total = i + j + k + l
            if Total != 0:
                PercentI = round(((i / Total) * 100), 2)
                PercentJ = round(((j / Total) * 100), 2)
                PercentK = round(((k / Total) * 100), 2)
                PercentL = round(((l / Total) * 100), 2)
                Completed.append(PercentI)
                Delayed.append(PercentJ)
                DueSoon.append(PercentK)
                OnTime.append(PercentL)

                print (i, j, k, l)
            else:
                Completed.append(0)
                Delayed.append(0)
                DueSoon.append(0)
                OnTime.append(0)
        args = {'Device':device, 'MainDevices':MainDevices,'selectedDevice':selectedDevice, 'Delayed':Delayed, 'Completed':Completed, 'DueSoon':DueSoon,
                'OnTime':OnTime, 'createdHistory':createdHistory, 'DelayedHistory':DelayedHistory, 'CompletedHistory':CompletedHistory,
                'DueSoonHistory':DueSoonHistory, 'OntimeHistory':OntimeHistory}
        return render(request, self.template_name, args )

class DeviceSummarySMView(LoginRequiredMixin,TemplateView):
    template_name = 'login/teamsummarySM.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        device = Device.objects.all().order_by("LaunchDate")
        MainDevices = DashboardControlDevice.objects.all().order_by("id")
        selectedDevice = Device.objects.get(pk=pk)
        PRHistory = selectedDevice.servicemarketinghistory_set.all().order_by("Created")
        createdHistory = []
        DelayedHistory = []
        CompletedHistory = []
        DueSoonHistory = []
        OntimeHistory = []
        for History in PRHistory:
            createdHistory.append('Week #' + str(History.Created.isocalendar()[1]) + ', ' + History.Created.strftime('%B') )
            DelayedHistory.append(float(History.Delayed))
            CompletedHistory.append(float(History.Completed))
            DueSoonHistory.append(float(History.DueSoon))
            OntimeHistory.append(float(History.OnTime))
        zipped_data = extra_utils.delayedElements(selectedDevice)
        Delayed = []
        Completed = []
        DueSoon = []
        OnTime = []
        for i, j, k, l in zipped_data:
            Total = i + j + k + l
            if Total != 0:
                PercentI = round(((i / Total) * 100), 2)
                PercentJ = round(((j / Total) * 100), 2)
                PercentK = round(((k / Total) * 100), 2)
                PercentL = round(((l / Total) * 100), 2)
                Completed.append(PercentI)
                Delayed.append(PercentJ)
                DueSoon.append(PercentK)
                OnTime.append(PercentL)

                print (i, j, k, l)
            else:
                Completed.append(0)
                Delayed.append(0)
                DueSoon.append(0)
                OnTime.append(0)
        args = {'Device':device, 'MainDevices':MainDevices,'selectedDevice':selectedDevice, 'Delayed':Delayed, 'Completed':Completed, 'DueSoon':DueSoon,
                'OnTime':OnTime, 'createdHistory':createdHistory, 'DelayedHistory':DelayedHistory, 'CompletedHistory':CompletedHistory,
                'DueSoonHistory':DueSoonHistory, 'OntimeHistory':OntimeHistory}
        return render(request, self.template_name, args )

class DeviceSummarySTView(LoginRequiredMixin,TemplateView):
    template_name = 'login/teamsummaryST.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        device = Device.objects.all().order_by("LaunchDate")
        MainDevices = DashboardControlDevice.objects.all().order_by("id")
        selectedDevice = Device.objects.get(pk=pk)
        PRHistory = selectedDevice.servicetraininghistory_set.all().order_by("Created")
        createdHistory = []
        DelayedHistory = []
        CompletedHistory = []
        DueSoonHistory = []
        OntimeHistory = []
        for History in PRHistory:
            createdHistory.append('Week #' + str(History.Created.isocalendar()[1]) + ', ' + History.Created.strftime('%B') )
            DelayedHistory.append(float(History.Delayed))
            CompletedHistory.append(float(History.Completed))
            DueSoonHistory.append(float(History.DueSoon))
            OntimeHistory.append(float(History.OnTime))
        zipped_data = extra_utils.delayedElements(selectedDevice)
        Delayed = []
        Completed = []
        DueSoon = []
        OnTime = []
        for i, j, k, l in zipped_data:
            Total = i + j + k + l
            if Total != 0:
                PercentI = round(((i / Total) * 100), 2)
                PercentJ = round(((j / Total) * 100), 2)
                PercentK = round(((k / Total) * 100), 2)
                PercentL = round(((l / Total) * 100), 2)
                Completed.append(PercentI)
                Delayed.append(PercentJ)
                DueSoon.append(PercentK)
                OnTime.append(PercentL)

                print (i, j, k, l)
            else:
                Completed.append(0)
                Delayed.append(0)
                DueSoon.append(0)
                OnTime.append(0)
        args = {'Device':device, 'MainDevices':MainDevices,'selectedDevice':selectedDevice, 'Delayed':Delayed, 'Completed':Completed, 'DueSoon':DueSoon,
                'OnTime':OnTime, 'createdHistory':createdHistory, 'DelayedHistory':DelayedHistory, 'CompletedHistory':CompletedHistory,
                'DueSoonHistory':DueSoonHistory, 'OntimeHistory':OntimeHistory}
        return render(request, self.template_name, args )

class DeviceSummaryPView(LoginRequiredMixin,TemplateView):
    template_name = 'login/teamsummaryP.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        device = Device.objects.all().order_by("LaunchDate")
        MainDevices = DashboardControlDevice.objects.all().order_by("id")
        selectedDevice = Device.objects.get(pk=pk)
        PRHistory = selectedDevice.partshistory_set.all().order_by("Created")
        createdHistory = []
        DelayedHistory = []
        CompletedHistory = []
        DueSoonHistory = []
        OntimeHistory = []
        for History in PRHistory:
            createdHistory.append('Week #' + str(History.Created.isocalendar()[1]) + ', ' + History.Created.strftime('%B') )
            DelayedHistory.append(float(History.Delayed))
            CompletedHistory.append(float(History.Completed))
            DueSoonHistory.append(float(History.DueSoon))
            OntimeHistory.append(float(History.OnTime))
        zipped_data = extra_utils.delayedElements(selectedDevice)
        Delayed = []
        Completed = []
        DueSoon = []
        OnTime = []
        for i, j, k, l in zipped_data:
            Total = i + j + k + l
            if Total != 0:
                PercentI = round(((i / Total) * 100), 2)
                PercentJ = round(((j / Total) * 100), 2)
                PercentK = round(((k / Total) * 100), 2)
                PercentL = round(((l / Total) * 100), 2)
                Completed.append(PercentI)
                Delayed.append(PercentJ)
                DueSoon.append(PercentK)
                OnTime.append(PercentL)

                print (i, j, k, l)
            else:
                Completed.append(0)
                Delayed.append(0)
                DueSoon.append(0)
                OnTime.append(0)
        args = {'Device':device, 'MainDevices':MainDevices,'selectedDevice':selectedDevice, 'Delayed':Delayed, 'Completed':Completed, 'DueSoon':DueSoon,
                'OnTime':OnTime, 'createdHistory':createdHistory, 'DelayedHistory':DelayedHistory, 'CompletedHistory':CompletedHistory,
                'DueSoonHistory':DueSoonHistory, 'OntimeHistory':OntimeHistory}
        return render(request, self.template_name, args )

class HomepageHAView(LoginRequiredMixin,TemplateView):
    template_name = 'login/homepageHA.html'
    login_url = '/login/auth/'
    def get(self, request):
        device = Device.objects.filter(Device_Category='HA')
        for D in device:
            print(D.Name)
        args = {'Devices':device,}
        return render(request, self.template_name, args )

class HomepageHEView(LoginRequiredMixin,TemplateView):
    template_name = 'login/homepageHE.html'
    login_url = '/login/auth/'
    def get(self, request):
        device = Device.objects.filter(Device_Category='HE')
        for D in device:
            print(D.Name)
        args = {'Devices':device,}
        return render(request, self.template_name, args )

class HomepageView(LoginRequiredMixin,TemplateView):
    template_name = 'login/homepage.html'
    login_url = '/login/auth/'
    def get(self, request):
        extra_utils.update_Warning()
        device = Device.objects.all().order_by("LaunchDate")
        MainDevices = DashboardControlDevice.objects.all().order_by("id")
        # array = []
        # completed = []
        # count = 0
        # today = datetime.date.today()
        # CurrentWeek = today.isocalendar()[1]

        # for D in MainDevices:
        #     count +=1
        #     array.append(D.Device.Name)
        #     completed.append(D.Device.completed)
        #     if count == 1:
        #         set = D.Device.devicehistory_set.all().order_by("Created")
        #         setcompleted1 = []
        #         Total = 0
        #         for Set in set:
        #             Total += 1
        #             setcompleted1.append( Set.Completed)
        #         setcompleted1 = setcompleted1[-4:]
        #     if count == 2:
        #         set = D.Device.devicehistory_set.all().order_by("Created")
        #         setcompleted2 = []
        #         for Set in set:
        #             setcompleted2.append( Set.Completed)
        #         setcompleted2 = setcompleted2[-4:]
        #     if count == 3:
        #         set = D.Device.devicehistory_set.all().order_by("Created")
        #         setcompleted3 = []
        #         for Set in set:
        #             setcompleted3.append( Set.Completed)
        #         setcompleted3 = setcompleted3[-4:]
        #     if count == 4:
        #         set = D.Device.devicehistory_set.all().order_by("Created")
        #         setcompleted4 = []
        #         for Set in set:
        #             setcompleted4.append( Set.Completed)
        #         setcompleted4 = setcompleted4[-4:]
        #     if count == 5:
        #         set = D.Device.devicehistory_set.all().order_by("Created")
        #         setcompleted5 = []
        #         for Set in set:
        #             setcompleted5.append( Set.Completed)
        #         setcompleted5 = setcompleted5[-4:]

        # zippeddata = zip(array,completed)


        args = {'Device':device, 'MainDevices':MainDevices}
        return render(request, self.template_name, args )


class DeviceSummaryView(LoginRequiredMixin,TemplateView):
    template_name = 'login/devicesummary.html'
    login_url = '/login/auth/'
    def get(self, request,pk):
        device = Device.objects.all().order_by("LaunchDate")
        MainDevices = DashboardControlDevice.objects.all().order_by("id")
        selectedDevice = Device.objects.get(pk=pk)
        zipped_data= extra_utils.delayedElements(selectedDevice)
        Delayed = []
        Completed = []
        DueSoon = []
        OnTime = []
        for i,j,k,l in zipped_data:
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
        # array = []
        # counter = 0
        # count = 0
        # today = datetime.date.today()
        # CurrentWeek = today.isocalendar()[1]
        # PreviousWeek1 = CurrentWeek -1
        # PreviousWeek2 = CurrentWeek -2
        # PreviousWeek3 = CurrentWeek - 3
        # PreviousWeek4 = CurrentWeek - 4
        # for D in MainDevices:
        #     count +=1
        #     array.append(D.Device.Name)
        #     if count == 1:
        #         set = D.Device.devicehistory_set.all().order_by("Created")
        #         setcompleted1 = []
        #         for Set in set:
        #             setcompleted1.append( Set.Completed)
        #         setcompleted1 = setcompleted1[-4:]
        #     if count == 2:
        #         set = D.Device.devicehistory_set.all().order_by("Created")
        #         setcompleted2 = []
        #         for Set in set:
        #             setcompleted2.append( Set.Completed)
        #         setcompleted2 = setcompleted2[-4:]
        #     if count == 3:
        #         set = D.Device.devicehistory_set.all().order_by("Created")
        #         setcompleted3 = []
        #         for Set in set:
        #             setcompleted3.append( Set.Completed)
        #         setcompleted3 = setcompleted3[-4:]
        #     if count == 4:
        #         set = D.Device.devicehistory_set.all().order_by("Created")
        #         setcompleted4 = []
        #         for Set in set:
        #             setcompleted4.append( Set.Completed)
        #         setcompleted4 = setcompleted4[-4:]
        #     if count == 5:
        #         set = D.Device.devicehistory_set.all().order_by("Created")
        #         setcompleted5 = []
        #         for Set in set:
        #             setcompleted5.append( Set.Completed)
        #         setcompleted5 = setcompleted5[-4:]

        # for D in device:
        #     counter += 1
        # SeletedDevice = Device.objects.get(pk=pk)
        # set = SeletedDevice.devicehistory_set.all().order_by("Created")
        # setselectedcompleted = []
        # week = []
        # Total = 0
        # for Set in set:
        #     Total += 1
        #     setselectedcompleted.append(Set.Completed)
        # for num in range (CurrentWeek - Total + 1, CurrentWeek+1):
        #     week.append("Week " + str(num))

        # TeamReadiness = [SeletedDevice.ProductReadiness.completed,SeletedDevice.VideoContent.completed,SeletedDevice.DigitalContent.completed,
        #                 SeletedDevice.CallCenterTraining.completed,SeletedDevice.CallCenterOpertaions.completed,SeletedDevice.ProductSupport.completed,
        #                 SeletedDevice.Warehouse.completed,SeletedDevice.FieldService.completed,SeletedDevice.TechSupport.completed,
        #                 SeletedDevice.ServiceMarketing.completed,SeletedDevice.ServiceTraining.completed,SeletedDevice.Parts.completed, ]

        args = {'Device':device, 'MainDevices':MainDevices,'selectedDevice':selectedDevice, 'Delayed':Delayed, 'Completed':Completed, 'DueSoon':DueSoon,
                'OnTime':OnTime}
        return render(request, self.template_name, args )

class DeviceSummaryHAView(LoginRequiredMixin,TemplateView):
    template_name = 'login/devicesummaryHA.html'
    login_url = '/login/auth/'
    def get(self, request,pk):
        device = Device.objects.filter(Device_Category='HA')
        selectedDevice =  Device.objects.get(pk=pk)
        zipped_data= extra_utils.delayedElements(selectedDevice)
        Delayed = []
        Completed = []
        DueSoon = []
        OnTime = []
        for i,j,k,l in zipped_data:
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
        args = {'Device':device,'selectedDevice':selectedDevice, 'Delayed':Delayed, 'Completed':Completed, 'DueSoon':DueSoon,
                'OnTime':OnTime}
        return render(request, self.template_name, args )

class DeviceSummaryHEView(LoginRequiredMixin,TemplateView):
    template_name = 'login/devicesummaryHE.html'
    login_url = '/login/auth/'
    def get(self, request,pk):
        device = Device.objects.filter(Device_Category='HE')
        selectedDevice =  Device.objects.get(pk=pk)
        zipped_data= extra_utils.delayedElements(selectedDevice)
        Delayed = []
        Completed = []
        DueSoon = []
        OnTime = []
        for i,j,k,l in zipped_data:
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
        args = {'Device':device,'selectedDevice':selectedDevice, 'Delayed':Delayed, 'Completed':Completed, 'DueSoon':DueSoon,
                'OnTime':OnTime}
        return render(request, self.template_name, args )

class DefaultSettingView(LoginRequiredMixin,TemplateView):
    template_name = 'login/defaultsetting.html'
    template_name1 = 'login/notasuperuser.html'
    login_url = '/login/auth/'
    def get(self,request):
        if request.user.is_superuser:
            ref = reference.objects.order_by('id')[0]
            args = {'ref' : ref}
            return render(request, self.template_name, args)
        else:
            return render (request, self.template_name1)
    def post(self,request):
        if 'Task1Submit' in request.POST:
            ref = reference.objects.order_by('id')[0]
            x = ref.Launch_Date
            ProductReadines = ProductReadiness(Task1_Start_Date=x-timedelta(100), Task1_End_Date=x-timedelta(90),
                                               Task2_Start_Date=x - timedelta(100), Task2_End_Date=x - timedelta(85),
                                               Task3_Start_Date=x - timedelta(90), Task3_End_Date=x - timedelta(80),
                                               Task4_Start_Date=x - timedelta(80), Task4_End_Date=x - timedelta(70),
                                               Task5_Start_Date=x - timedelta(75), Task5_End_Date=x - timedelta(60),
                                               Task6_Start_Date=x - timedelta(75), Task6_End_Date=x - timedelta(45),
                                               Task7_Start_Date=x - timedelta(60), Task7_End_Date=x - timedelta(45),
                                               Task8_Start_Date=x - timedelta(30), Task8_End_Date=x - timedelta(14),
                                               Task9_Start_Date=x - timedelta(14), Task9_End_Date=x - timedelta(0),)
            ProductReadines.save()
            DigitalContent = digitalcontent(Task1_Start_Date=x-timedelta(75), Task1_End_Date=x-timedelta(14),
                                               Task2_Start_Date=x - timedelta(60), Task2_End_Date=x - timedelta(45),
                                               Task3_Start_Date=x - timedelta(60), Task3_End_Date=x - timedelta(14),
                                               Task4_Start_Date=x - timedelta(60), Task4_End_Date=x - timedelta(14),
                                               Task5_Start_Date=x - timedelta(60), Task5_End_Date=x + timedelta(30),
                                               Task6_Start_Date=x - timedelta(60), Task6_End_Date=x - timedelta(14),)
            DigitalContent.save()
            VideoContent = videocontent(Task1_Start_Date=x-timedelta(45), Task1_End_Date=x-timedelta(14),
                                               Task2_Start_Date=x - timedelta(0), Task2_End_Date=x + timedelta(14),
                                               Task3_Start_Date=x + timedelta(14), Task3_End_Date=x + timedelta(60),
)
            VideoContent.save()
            CallCenterTraining = callcentertraining(Task1_Start_Date=x-timedelta(60), Task1_End_Date=x-timedelta(30),
                                               Task2_Start_Date=x - timedelta(45), Task2_End_Date=x - timedelta(30),
                                               Task3_Start_Date=x - timedelta(30), Task3_End_Date=x - timedelta(20),
                                               Task4_Start_Date=x - timedelta(30), Task4_End_Date=x - timedelta(0),)
            CallCenterTraining.save()
            CallCenterOperations = callcenteropertaions(Task1_Start_Date=x-timedelta(75), Task1_End_Date=x-timedelta(60),
                                               Task2_Start_Date=x - timedelta(75), Task2_End_Date=x - timedelta(60),
                                               Task3_Start_Date=x - timedelta(40), Task3_End_Date=x - timedelta(30),
                                               Task4_Start_Date=x - timedelta(30), Task4_End_Date=x - timedelta(20),)
            CallCenterOperations.save()
            ProductSupport = productsupport(Task1_Start_Date=x-timedelta(100), Task1_End_Date=x-timedelta(85),
                                               Task2_Start_Date=x - timedelta(90), Task2_End_Date=x - timedelta(85),
                                               Task3_Start_Date=x - timedelta(90), Task3_End_Date=x - timedelta(80),
                                               Task4_Start_Date=x - timedelta(90), Task4_End_Date=x - timedelta(70),
                                               Task7_Start_Date=x - timedelta(0), Task7_End_Date=x + timedelta(30),
                                               Task8_Start_Date=x - timedelta(0), Task8_End_Date=x + timedelta(30),
                                               Task9_Start_Date=x - timedelta(0), Task9_End_Date=x + timedelta(30),)
            ProductSupport.save()
            Warehouse = warehouse(id=None)
            Warehouse.save()
            FieldService = fieldservice(id=None)
            FieldService.save()
            TechSupport = techsupport(id=None)
            TechSupport.save()
            ServiceMarketing = servicemarketing(Task1_Start_Date=x-timedelta(90), Task1_End_Date=x-timedelta(80),
                                               Task2_Start_Date=x - timedelta(80), Task2_End_Date=x - timedelta(60),
                                               Task3_Start_Date=x - timedelta(60), Task3_End_Date=x - timedelta(30),
                                               Task4_Start_Date=x - timedelta(60), Task4_End_Date=x - timedelta(30),)
            ServiceMarketing.save()
            ServiceTraining = servicetraining(Task1_Start_Date=x-timedelta(60), Task1_End_Date=x-timedelta(30),
                                              Task4_Start_Date=x + timedelta(15), Task4_End_Date=x + timedelta(30),)
            ServiceTraining.save()
            Parts = parts(Task1_Start_Date=x-timedelta(90), Task1_End_Date=x-timedelta(30),
                                               Task2_Start_Date=x - timedelta(60), Task2_End_Date=x - timedelta(30),
                                               Task3_Start_Date=x - timedelta(14), Task3_End_Date=x - timedelta(4),
                                               Task4_Start_Date=x - timedelta(14), Task4_End_Date=x - timedelta(4),
                                               Task5_Start_Date=x - timedelta(14), Task5_End_Date=x - timedelta(4),
                                               Task6_Start_Date=x - timedelta(14), Task6_End_Date=x - timedelta(4),
                                               Task7_Start_Date=x - timedelta(14), Task7_End_Date=x - timedelta(4),)
            Parts.save()
            a = Device(Name = "default", LaunchDate = ref.Launch_Date, ProductReadiness = ProductReadines,
                       VideoContent = VideoContent, DigitalContent = DigitalContent, CallCenterOpertaions = CallCenterOperations,
                       CallCenterTraining =CallCenterTraining, ProductSupport = ProductSupport,
                       Warehouse = Warehouse, FieldService = FieldService, TechSupport = TechSupport,
                       ServiceMarketing = ServiceMarketing, ServiceTraining =ServiceTraining,
                       Parts = Parts,
                       )
            a.save()
#             messages.success(request, 'Your default device configuration is successfully created - Go to admin page to complete the initialization!')
            return redirect('/admin/login/device/')

class ExcelDetailView(LoginRequiredMixin,ListView):
    template_name = 'login/detailexcel.html'
    login_url = '/login/auth/'
    def get(self, request, pk):
        devices = Device.objects.get(pk=pk)
        Active_PR=extra_utils.activeTasksPR(devices)
        Active_DC=extra_utils.activeTasksDC(devices)
        Active_VC=extra_utils.activeTasksVC(devices)
        Active_CCO=extra_utils.activeTasksCCO(devices)
        Active_CCT=extra_utils.activeTasksCCT(devices)
        Active_PS=extra_utils.activeTasksPS(devices)
        Active_W=extra_utils.activeTasksW(devices)
        Active_FS=extra_utils.activeTasksFS(devices)
        Active_TS=extra_utils.activeTasksTS(devices)
        Active_SM=extra_utils.activeTasksSM(devices)
        Active_ST=extra_utils.activeTasksST(devices)
        Active_P = extra_utils.activeTasksP(devices)
        posts1_PR = devices.ProductReadiness.task1statusproductreadiness_set.all().order_by('-created')
        posts2_PR = devices.ProductReadiness.task2statusproductreadiness_set.all().order_by('-created')
        posts3_PR = devices.ProductReadiness.task3statusproductreadiness_set.all().order_by('-created')
        posts4_PR = devices.ProductReadiness.task4statusproductreadiness_set.all().order_by('-created')
        posts5_PR = devices.ProductReadiness.task5statusproductreadiness_set.all().order_by('-created')
        posts6_PR = devices.ProductReadiness.task6statusproductreadiness_set.all().order_by('-created')
        posts7_PR = devices.ProductReadiness.task7statusproductreadiness_set.all().order_by('-created')
        posts8_PR = devices.ProductReadiness.task8statusproductreadiness_set.all().order_by('-created')
        posts9_PR = devices.ProductReadiness.task9statusproductreadiness_set.all().order_by('-created')
        posts10_PR = devices.ProductReadiness.task10statusproductreadiness_set.all().order_by('-created')
        posts11_PR = devices.ProductReadiness.task11statusproductreadiness_set.all().order_by('-created')
        posts12_PR = devices.ProductReadiness.task12statusproductreadiness_set.all().order_by('-created')
        posts13_PR = devices.ProductReadiness.task13statusproductreadiness_set.all().order_by('-created')
        posts14_PR = devices.ProductReadiness.task14statusproductreadiness_set.all().order_by('-created')
        posts15_PR = devices.ProductReadiness.task15statusproductreadiness_set.all().order_by('-created')
        posts16_PR = devices.ProductReadiness.task16statusproductreadiness_set.all().order_by('-created')
        posts17_PR = devices.ProductReadiness.task17statusproductreadiness_set.all().order_by('-created')
        posts18_PR = devices.ProductReadiness.task18statusproductreadiness_set.all().order_by('-created')
        posts19_PR = devices.ProductReadiness.task19statusproductreadiness_set.all().order_by('-created')
        posts20_PR = devices.ProductReadiness.task20statusproductreadiness_set.all().order_by('-created')
        posts1_DC = devices.DigitalContent.task1statusdigitalcontent_set.all().order_by('-created')
        posts2_DC = devices.DigitalContent.task2statusdigitalcontent_set.all().order_by('-created')
        posts3_DC = devices.DigitalContent.task3statusdigitalcontent_set.all().order_by('-created')
        posts4_DC = devices.DigitalContent.task4statusdigitalcontent_set.all().order_by('-created')
        posts5_DC = devices.DigitalContent.task5statusdigitalcontent_set.all().order_by('-created')
        posts6_DC = devices.DigitalContent.task6statusdigitalcontent_set.all().order_by('-created')
        posts7_DC = devices.DigitalContent.task7statusdigitalcontent_set.all().order_by('-created')
        posts8_DC = devices.DigitalContent.task8statusdigitalcontent_set.all().order_by('-created')
        posts9_DC = devices.DigitalContent.task9statusdigitalcontent_set.all().order_by('-created')
        posts10_DC = devices.DigitalContent.task10statusdigitalcontent_set.all().order_by('-created')
        posts11_DC = devices.DigitalContent.task11statusdigitalcontent_set.all().order_by('-created')
        posts12_DC = devices.DigitalContent.task12statusdigitalcontent_set.all().order_by('-created')
        posts13_DC = devices.DigitalContent.task13statusdigitalcontent_set.all().order_by('-created')
        posts14_DC = devices.DigitalContent.task14statusdigitalcontent_set.all().order_by('-created')
        posts15_DC = devices.DigitalContent.task15statusdigitalcontent_set.all().order_by('-created')
        posts16_DC = devices.DigitalContent.task16statusdigitalcontent_set.all().order_by('-created')
        posts17_DC = devices.DigitalContent.task17statusdigitalcontent_set.all().order_by('-created')
        posts18_DC = devices.DigitalContent.task18statusdigitalcontent_set.all().order_by('-created')
        posts19_DC = devices.DigitalContent.task19statusdigitalcontent_set.all().order_by('-created')
        posts20_DC = devices.DigitalContent.task20statusdigitalcontent_set.all().order_by('-created')
        posts1_VC = devices.VideoContent.task1statusvideocontent_set.all().order_by('-created')
        posts2_VC = devices.VideoContent.task2statusvideocontent_set.all().order_by('-created')
        posts3_VC = devices.VideoContent.task3statusvideocontent_set.all().order_by('-created')
        posts4_VC = devices.VideoContent.task4statusvideocontent_set.all().order_by('-created')
        posts5_VC = devices.VideoContent.task5statusvideocontent_set.all().order_by('-created')
        posts6_VC = devices.VideoContent.task6statusvideocontent_set.all().order_by('-created')
        posts7_VC = devices.VideoContent.task7statusvideocontent_set.all().order_by('-created')
        posts8_VC = devices.VideoContent.task8statusvideocontent_set.all().order_by('-created')
        posts9_VC = devices.VideoContent.task9statusvideocontent_set.all().order_by('-created')
        posts10_VC = devices.VideoContent.task10statusvideocontent_set.all().order_by('-created')
        posts11_VC = devices.VideoContent.task11statusvideocontent_set.all().order_by('-created')
        posts12_VC = devices.VideoContent.task12statusvideocontent_set.all().order_by('-created')
        posts13_VC = devices.VideoContent.task13statusvideocontent_set.all().order_by('-created')
        posts14_VC = devices.VideoContent.task14statusvideocontent_set.all().order_by('-created')
        posts15_VC = devices.VideoContent.task15statusvideocontent_set.all().order_by('-created')
        posts16_VC = devices.VideoContent.task16statusvideocontent_set.all().order_by('-created')
        posts17_VC = devices.VideoContent.task17statusvideocontent_set.all().order_by('-created')
        posts18_VC = devices.VideoContent.task18statusvideocontent_set.all().order_by('-created')
        posts19_VC = devices.VideoContent.task19statusvideocontent_set.all().order_by('-created')
        posts20_VC = devices.VideoContent.task20statusvideocontent_set.all().order_by('-created')
        posts1_CCT = devices.CallCenterTraining.task1statuscallcentertraining_set.all().order_by('-created')
        posts2_CCT = devices.CallCenterTraining.task2statuscallcentertraining_set.all().order_by('-created')
        posts3_CCT = devices.CallCenterTraining.task3statuscallcentertraining_set.all().order_by('-created')
        posts4_CCT = devices.CallCenterTraining.task4statuscallcentertraining_set.all().order_by('-created')
        posts5_CCT = devices.CallCenterTraining.task5statuscallcentertraining_set.all().order_by('-created')
        posts6_CCT = devices.CallCenterTraining.task6statuscallcentertraining_set.all().order_by('-created')
        posts7_CCT = devices.CallCenterTraining.task7statuscallcentertraining_set.all().order_by('-created')
        posts8_CCT = devices.CallCenterTraining.task8statuscallcentertraining_set.all().order_by('-created')
        posts9_CCT = devices.CallCenterTraining.task9statuscallcentertraining_set.all().order_by('-created')
        posts10_CCT = devices.CallCenterTraining.task10statuscallcentertraining_set.all().order_by('-created')
        posts11_CCT = devices.CallCenterTraining.task11statuscallcentertraining_set.all().order_by('-created')
        posts12_CCT = devices.CallCenterTraining.task12statuscallcentertraining_set.all().order_by('-created')
        posts13_CCT = devices.CallCenterTraining.task13statuscallcentertraining_set.all().order_by('-created')
        posts14_CCT = devices.CallCenterTraining.task14statuscallcentertraining_set.all().order_by('-created')
        posts15_CCT = devices.CallCenterTraining.task15statuscallcentertraining_set.all().order_by('-created')
        posts16_CCT = devices.CallCenterTraining.task16statuscallcentertraining_set.all().order_by('-created')
        posts17_CCT = devices.CallCenterTraining.task17statuscallcentertraining_set.all().order_by('-created')
        posts18_CCT = devices.CallCenterTraining.task18statuscallcentertraining_set.all().order_by('-created')
        posts19_CCT = devices.CallCenterTraining.task19statuscallcentertraining_set.all().order_by('-created')
        posts20_CCT = devices.CallCenterTraining.task20statuscallcentertraining_set.all().order_by('-created')
        posts1_CCO = devices.CallCenterOpertaions.task1statuscallcenteropertaions_set.all().order_by('-created')
        posts2_CCO = devices.CallCenterOpertaions.task2statuscallcenteropertaions_set.all().order_by('-created')
        posts3_CCO = devices.CallCenterOpertaions.task3statuscallcenteropertaions_set.all().order_by('-created')
        posts4_CCO = devices.CallCenterOpertaions.task4statuscallcenteropertaions_set.all().order_by('-created')
        posts5_CCO = devices.CallCenterOpertaions.task5statuscallcenteropertaions_set.all().order_by('-created')
        posts6_CCO = devices.CallCenterOpertaions.task6statuscallcenteropertaions_set.all().order_by('-created')
        posts7_CCO = devices.CallCenterOpertaions.task7statuscallcenteropertaions_set.all().order_by('-created')
        posts8_CCO = devices.CallCenterOpertaions.task8statuscallcenteropertaions_set.all().order_by('-created')
        posts9_CCO= devices.CallCenterOpertaions.task9statuscallcenteropertaions_set.all().order_by('-created')
        posts10_CCO = devices.CallCenterOpertaions.task10statuscallcenteropertaions_set.all().order_by('-created')
        posts11_CCO = devices.CallCenterOpertaions.task11statuscallcenteropertaions_set.all().order_by('-created')
        posts12_CCO = devices.CallCenterOpertaions.task12statuscallcenteropertaions_set.all().order_by('-created')
        posts13_CCO = devices.CallCenterOpertaions.task13statuscallcenteropertaions_set.all().order_by('-created')
        posts14_CCO = devices.CallCenterOpertaions.task14statuscallcenteropertaions_set.all().order_by('-created')
        posts15_CCO = devices.CallCenterOpertaions.task15statuscallcenteropertaions_set.all().order_by('-created')
        posts16_CCO = devices.CallCenterOpertaions.task16statuscallcenteropertaions_set.all().order_by('-created')
        posts17_CCO = devices.CallCenterOpertaions.task17statuscallcenteropertaions_set.all().order_by('-created')
        posts18_CCO = devices.CallCenterOpertaions.task18statuscallcenteropertaions_set.all().order_by('-created')
        posts19_CCO = devices.CallCenterOpertaions.task19statuscallcenteropertaions_set.all().order_by('-created')
        posts20_CCO = devices.CallCenterOpertaions.task20statuscallcenteropertaions_set.all().order_by('-created')
        posts1_PS = devices.ProductSupport.task1statusproductsupport_set.all().order_by('-created')
        posts2_PS = devices.ProductSupport.task2statusproductsupport_set.all().order_by('-created')
        posts3_PS = devices.ProductSupport.task3statusproductsupport_set.all().order_by('-created')
        posts4_PS = devices.ProductSupport.task4statusproductsupport_set.all().order_by('-created')
        posts5_PS = devices.ProductSupport.task5statusproductsupport_set.all().order_by('-created')
        posts6_PS = devices.ProductSupport.task6statusproductsupport_set.all().order_by('-created')
        posts7_PS = devices.ProductSupport.task7statusproductsupport_set.all().order_by('-created')
        posts8_PS = devices.ProductSupport.task8statusproductsupport_set.all().order_by('-created')
        posts9_PS = devices.ProductSupport.task9statusproductsupport_set.all().order_by('-created')
        posts10_PS = devices.ProductSupport.task10statusproductsupport_set.all().order_by('-created')
        posts11_PS = devices.ProductSupport.task11statusproductsupport_set.all().order_by('-created')
        posts12_PS = devices.ProductSupport.task12statusproductsupport_set.all().order_by('-created')
        posts13_PS = devices.ProductSupport.task13statusproductsupport_set.all().order_by('-created')
        posts14_PS = devices.ProductSupport.task14statusproductsupport_set.all().order_by('-created')
        posts15_PS = devices.ProductSupport.task15statusproductsupport_set.all().order_by('-created')
        posts16_PS = devices.ProductSupport.task16statusproductsupport_set.all().order_by('-created')
        posts17_PS = devices.ProductSupport.task17statusproductsupport_set.all().order_by('-created')
        posts18_PS = devices.ProductSupport.task18statusproductsupport_set.all().order_by('-created')
        posts19_PS = devices.ProductSupport.task19statusproductsupport_set.all().order_by('-created')
        posts20_PS = devices.ProductSupport.task20statusproductsupport_set.all().order_by('-created')
        posts1_W = devices.Warehouse.task1statuswarehouse_set.all().order_by('-created')
        posts2_W = devices.Warehouse.task2statuswarehouse_set.all().order_by('-created')
        posts3_W = devices.Warehouse.task3statuswarehouse_set.all().order_by('-created')
        posts4_W = devices.Warehouse.task4statuswarehouse_set.all().order_by('-created')
        posts5_W = devices.Warehouse.task5statuswarehouse_set.all().order_by('-created')
        posts6_W = devices.Warehouse.task6statuswarehouse_set.all().order_by('-created')
        posts7_W = devices.Warehouse.task7statuswarehouse_set.all().order_by('-created')
        posts8_W = devices.Warehouse.task8statuswarehouse_set.all().order_by('-created')
        posts9_W = devices.Warehouse.task9statuswarehouse_set.all().order_by('-created')
        posts10_W = devices.Warehouse.task10statuswarehouse_set.all().order_by('-created')
        posts11_W = devices.Warehouse.task11statuswarehouse_set.all().order_by('-created')
        posts12_W = devices.Warehouse.task12statuswarehouse_set.all().order_by('-created')
        posts13_W = devices.Warehouse.task13statuswarehouse_set.all().order_by('-created')
        posts14_W = devices.Warehouse.task14statuswarehouse_set.all().order_by('-created')
        posts15_W = devices.Warehouse.task15statuswarehouse_set.all().order_by('-created')
        posts16_W = devices.Warehouse.task16statuswarehouse_set.all().order_by('-created')
        posts17_W = devices.Warehouse.task17statuswarehouse_set.all().order_by('-created')
        posts18_W = devices.Warehouse.task18statuswarehouse_set.all().order_by('-created')
        posts19_W = devices.Warehouse.task19statuswarehouse_set.all().order_by('-created')
        posts20_W = devices.Warehouse.task20statuswarehouse_set.all().order_by('-created')
        posts1_FS = devices.FieldService.task1statusfieldservice_set.all().order_by('-created')
        posts2_FS = devices.FieldService.task2statusfieldservice_set.all().order_by('-created')
        posts3_FS = devices.FieldService.task3statusfieldservice_set.all().order_by('-created')
        posts4_FS = devices.FieldService.task4statusfieldservice_set.all().order_by('-created')
        posts5_FS = devices.FieldService.task5statusfieldservice_set.all().order_by('-created')
        posts6_FS = devices.FieldService.task6statusfieldservice_set.all().order_by('-created')
        posts7_FS = devices.FieldService.task7statusfieldservice_set.all().order_by('-created')
        posts8_FS = devices.FieldService.task8statusfieldservice_set.all().order_by('-created')
        posts9_FS = devices.FieldService.task9statusfieldservice_set.all().order_by('-created')
        posts10_FS = devices.FieldService.task10statusfieldservice_set.all().order_by('-created')
        posts11_FS = devices.FieldService.task11statusfieldservice_set.all().order_by('-created')
        posts12_FS = devices.FieldService.task12statusfieldservice_set.all().order_by('-created')
        posts13_FS = devices.FieldService.task13statusfieldservice_set.all().order_by('-created')
        posts14_FS = devices.FieldService.task14statusfieldservice_set.all().order_by('-created')
        posts15_FS = devices.FieldService.task15statusfieldservice_set.all().order_by('-created')
        posts16_FS = devices.FieldService.task16statusfieldservice_set.all().order_by('-created')
        posts17_FS = devices.FieldService.task17statusfieldservice_set.all().order_by('-created')
        posts18_FS = devices.FieldService.task18statusfieldservice_set.all().order_by('-created')
        posts19_FS = devices.FieldService.task19statusfieldservice_set.all().order_by('-created')
        posts20_FS = devices.FieldService.task20statusfieldservice_set.all().order_by('-created')
        posts1_TS = devices.TechSupport.task1statustechsupport_set.all().order_by('-created')
        posts2_TS = devices.TechSupport.task2statustechsupport_set.all().order_by('-created')
        posts3_TS = devices.TechSupport.task3statustechsupport_set.all().order_by('-created')
        posts4_TS = devices.TechSupport.task4statustechsupport_set.all().order_by('-created')
        posts5_TS = devices.TechSupport.task5statustechsupport_set.all().order_by('-created')
        posts6_TS = devices.TechSupport.task6statustechsupport_set.all().order_by('-created')
        posts7_TS = devices.TechSupport.task7statustechsupport_set.all().order_by('-created')
        posts8_TS = devices.TechSupport.task8statustechsupport_set.all().order_by('-created')
        posts9_TS = devices.TechSupport.task9statustechsupport_set.all().order_by('-created')
        posts10_TS = devices.TechSupport.task10statustechsupport_set.all().order_by('-created')
        posts11_TS = devices.TechSupport.task11statustechsupport_set.all().order_by('-created')
        posts12_TS = devices.TechSupport.task12statustechsupport_set.all().order_by('-created')
        posts13_TS = devices.TechSupport.task13statustechsupport_set.all().order_by('-created')
        posts14_TS = devices.TechSupport.task14statustechsupport_set.all().order_by('-created')
        posts15_TS = devices.TechSupport.task15statustechsupport_set.all().order_by('-created')
        posts16_TS = devices.TechSupport.task16statustechsupport_set.all().order_by('-created')
        posts17_TS = devices.TechSupport.task17statustechsupport_set.all().order_by('-created')
        posts18_TS = devices.TechSupport.task18statustechsupport_set.all().order_by('-created')
        posts19_TS = devices.TechSupport.task19statustechsupport_set.all().order_by('-created')
        posts20_TS = devices.TechSupport.task20statustechsupport_set.all().order_by('-created')
        posts1_SM = devices.ServiceMarketing.task1statusservicemarketing_set.all().order_by('-created')
        posts2_SM = devices.ServiceMarketing.task2statusservicemarketing_set.all().order_by('-created')
        posts3_SM = devices.ServiceMarketing.task3statusservicemarketing_set.all().order_by('-created')
        posts4_SM = devices.ServiceMarketing.task4statusservicemarketing_set.all().order_by('-created')
        posts5_SM = devices.ServiceMarketing.task5statusservicemarketing_set.all().order_by('-created')
        posts6_SM = devices.ServiceMarketing.task6statusservicemarketing_set.all().order_by('-created')
        posts7_SM = devices.ServiceMarketing.task7statusservicemarketing_set.all().order_by('-created')
        posts8_SM = devices.ServiceMarketing.task8statusservicemarketing_set.all().order_by('-created')
        posts9_SM = devices.ServiceMarketing.task9statusservicemarketing_set.all().order_by('-created')
        posts10_SM = devices.ServiceMarketing.task10statusservicemarketing_set.all().order_by('-created')
        posts11_SM = devices.ServiceMarketing.task11statusservicemarketing_set.all().order_by('-created')
        posts12_SM = devices.ServiceMarketing.task12statusservicemarketing_set.all().order_by('-created')
        posts13_SM = devices.ServiceMarketing.task13statusservicemarketing_set.all().order_by('-created')
        posts14_SM = devices.ServiceMarketing.task14statusservicemarketing_set.all().order_by('-created')
        posts15_SM = devices.ServiceMarketing.task15statusservicemarketing_set.all().order_by('-created')
        posts16_SM = devices.ServiceMarketing.task16statusservicemarketing_set.all().order_by('-created')
        posts17_SM = devices.ServiceMarketing.task17statusservicemarketing_set.all().order_by('-created')
        posts18_SM = devices.ServiceMarketing.task18statusservicemarketing_set.all().order_by('-created')
        posts19_SM = devices.ServiceMarketing.task19statusservicemarketing_set.all().order_by('-created')
        posts20_SM = devices.ServiceMarketing.task20statusservicemarketing_set.all().order_by('-created')
        posts1_ST = devices.ServiceTraining.task1statusservicetraining_set.all().order_by('-created')
        posts2_ST = devices.ServiceTraining.task2statusservicetraining_set.all().order_by('-created')
        posts3_ST = devices.ServiceTraining.task3statusservicetraining_set.all().order_by('-created')
        posts4_ST = devices.ServiceTraining.task4statusservicetraining_set.all().order_by('-created')
        posts5_ST = devices.ServiceTraining.task5statusservicetraining_set.all().order_by('-created')
        posts6_ST = devices.ServiceTraining.task6statusservicetraining_set.all().order_by('-created')
        posts7_ST = devices.ServiceTraining.task7statusservicetraining_set.all().order_by('-created')
        posts8_ST = devices.ServiceTraining.task8statusservicetraining_set.all().order_by('-created')
        posts9_ST = devices.ServiceTraining.task9statusservicetraining_set.all().order_by('-created')
        posts10_ST = devices.ServiceTraining.task10statusservicetraining_set.all().order_by('-created')
        posts11_ST = devices.ServiceTraining.task11statusservicetraining_set.all().order_by('-created')
        posts12_ST = devices.ServiceTraining.task12statusservicetraining_set.all().order_by('-created')
        posts13_ST = devices.ServiceTraining.task13statusservicetraining_set.all().order_by('-created')
        posts14_ST = devices.ServiceTraining.task14statusservicetraining_set.all().order_by('-created')
        posts15_ST = devices.ServiceTraining.task15statusservicetraining_set.all().order_by('-created')
        posts16_ST = devices.ServiceTraining.task16statusservicetraining_set.all().order_by('-created')
        posts17_ST = devices.ServiceTraining.task17statusservicetraining_set.all().order_by('-created')
        posts18_ST = devices.ServiceTraining.task18statusservicetraining_set.all().order_by('-created')
        posts19_ST = devices.ServiceTraining.task19statusservicetraining_set.all().order_by('-created')
        posts20_ST = devices.ServiceTraining.task20statusservicetraining_set.all().order_by('-created')
        posts1_P = devices.Parts.task1statusparts_set.all().order_by('-created')
        posts2_P = devices.Parts.task2statusparts_set.all().order_by('-created')
        posts3_P = devices.Parts.task3statusparts_set.all().order_by('-created')
        posts4_P = devices.Parts.task4statusparts_set.all().order_by('-created')
        posts5_P = devices.Parts.task5statusparts_set.all().order_by('-created')
        posts6_P = devices.Parts.task6statusparts_set.all().order_by('-created')
        posts7_P = devices.Parts.task7statusparts_set.all().order_by('-created')
        posts8_P = devices.Parts.task8statusparts_set.all().order_by('-created')
        posts9_P = devices.Parts.task9statusparts_set.all().order_by('-created')
        posts10_P = devices.Parts.task10statusparts_set.all().order_by('-created')
        posts11_P = devices.Parts.task11statusparts_set.all().order_by('-created')
        posts12_P = devices.Parts.task12statusparts_set.all().order_by('-created')
        posts13_P = devices.Parts.task13statusparts_set.all().order_by('-created')
        posts14_P = devices.Parts.task14statusparts_set.all().order_by('-created')
        posts15_P = devices.Parts.task15statusparts_set.all().order_by('-created')
        posts16_P = devices.Parts.task16statusparts_set.all().order_by('-created')
        posts17_P = devices.Parts.task17statusparts_set.all().order_by('-created')
        posts18_P = devices.Parts.task18statusparts_set.all().order_by('-created')
        posts19_P = devices.Parts.task19statusparts_set.all().order_by('-created')
        posts20_P = devices.Parts.task20statusparts_set.all().order_by('-created')
        args = {'Device': devices, 'Active_PR':Active_PR, 'Active_DC':Active_DC, 'Active_VC':Active_VC, 'Active_CCO':Active_CCO,
                'Active_CCT': Active_CCT,'Active_PS':Active_PS ,'Active_W':Active_W ,'Active_FS':Active_FS,
                'Active_TS': Active_TS, 'Active_SM':Active_SM, 'Active_FS':Active_FS, 'Active_ST':Active_ST,'Active_P':Active_P,
                'posts1_PR': posts1_PR, 'posts2_PR': posts2_PR, 'posts3_PR': posts3_PR, 'posts4_PR': posts4_PR,
                'posts5_PR': posts5_PR, 'posts6_PR': posts6_PR,
                'posts7_PR': posts7_PR, 'posts8_PR': posts8_PR, 'posts9_PR': posts9_PR, 'posts10_PR': posts10_PR, 'posts11_PR': posts11_PR,
                'posts12_PR': posts12_PR, 'posts13_PR': posts13_PR,
                'posts14_PR': posts14_PR, 'posts15_PR': posts15_PR, 'posts16_PR': posts16_PR, 'posts17_PR': posts17_PR, 'posts18_PR': posts18_PR,
                'posts19_PR': posts19_PR,
                'posts20_PR': posts20_PR,
                'posts1_DC': posts1_DC, 'posts2_DC': posts2_DC, 'posts3_DC': posts3_DC, 'posts4_DC': posts4_DC,
                'posts5_DC': posts5_DC, 'posts6_DC': posts6_DC,
                'posts7_DC': posts7_DC, 'posts8_DC': posts8_DC, 'posts9_DC': posts9_DC, 'posts10_DC': posts10_DC,
                'posts11_DC': posts11_DC,
                'posts12_DC': posts12_DC, 'posts13_DC': posts13_DC,
                'posts14_DC': posts14_DC, 'posts15_DC': posts15_DC, 'posts16_DC': posts16_DC, 'posts17_DC': posts17_DC,
                'posts18_DC': posts18_DC,
                'posts19_DC': posts19_DC,
                'posts20_DC': posts20_DC,
                'posts1_VC': posts1_VC, 'posts2_VC': posts2_VC, 'posts3_VC': posts3_VC, 'posts4_VC': posts4_VC,
                'posts5_VC': posts5_VC, 'posts6_VC': posts6_VC,
                'posts7_VC': posts7_VC, 'posts8_VC': posts8_VC, 'posts9_VC': posts9_VC, 'posts10_VC': posts10_VC,
                'posts11_VC': posts11_VC,
                'posts12_VC': posts12_VC, 'posts13_VC': posts13_VC,
                'posts14_VC': posts14_VC, 'posts15_VC': posts15_VC, 'posts16_VC': posts16_VC, 'posts17_VC': posts17_VC,
                'posts18_VC': posts18_VC,
                'posts19_VC': posts19_VC,
                'posts20_VC': posts20_VC,
                'posts1_CCO': posts1_CCO, 'posts2_CCO': posts2_CCO, 'posts3_CCO': posts3_CCO, 'posts4_CCO': posts4_CCO,
                'posts5_CCO': posts5_CCO, 'posts6_CCO': posts6_CCO,
                'posts7_CCO': posts7_CCO, 'posts8_CCO': posts8_CCO, 'posts9_CCO': posts9_CCO, 'posts10_CCO': posts10_CCO,
                'posts11_CCO': posts11_CCO,
                'posts12_CCO': posts12_CCO, 'posts13_CCO': posts13_CCO,
                'posts14_CCO': posts14_CCO, 'posts15_CCO': posts15_CCO, 'posts16_CCO': posts16_CCO, 'posts17_CCO': posts17_CCO,
                'posts18_CCO': posts18_CCO,
                'posts19_CCO': posts19_CCO,
                'posts20_CCO': posts20_CCO,
                'posts1_CCT': posts1_CCT, 'posts2_CCT': posts2_CCT, 'posts3_CCT': posts3_CCT, 'posts4_CCT': posts4_CCT,
                'posts5_CCT': posts5_CCT, 'posts6_CCT': posts6_CCT,
                'posts7_CCT': posts7_CCT, 'posts8_CCT': posts8_CCT, 'posts9_CCT': posts9_CCT, 'posts10_CCT': posts10_CCT,
                'posts11_CCT': posts11_CCT,
                'posts12_CCT': posts12_CCT, 'posts13_CCT': posts13_CCT,
                'posts14_CCT': posts14_CCT, 'posts15_CCT': posts15_CCT, 'posts16_CCT': posts16_CCT, 'posts17_CCT': posts17_CCT,
                'posts18_CCT': posts18_CCT,
                'posts19_CCT': posts19_CCT,
                'posts20_CCT': posts20_CCT,
                'posts1_PS': posts1_PS, 'posts2_PS': posts2_PS, 'posts3_PS': posts3_PS, 'posts4_PS': posts4_PS,
                'posts5_PS': posts5_PS, 'posts6_PS': posts6_PS,
                'posts7_PS': posts7_PS, 'posts8_PS': posts8_PS, 'posts9_PS': posts9_PS, 'posts10_PS': posts10_PS,
                'posts11_PS': posts11_PS,
                'posts12_PS': posts12_PS, 'posts13_PS': posts13_PS,
                'posts14_PS': posts14_PS, 'posts15_PS': posts15_PS, 'posts16_PS': posts16_PS, 'posts17_PS': posts17_PS,
                'posts18_PS': posts18_PS,
                'posts19_PS': posts19_PS,
                'posts20_PS': posts20_PS,
                'posts1_FS': posts1_FS, 'posts2_FS': posts2_FS, 'posts3_FS': posts3_FS, 'posts4_FS': posts4_FS,
                'posts5_FS': posts5_FS, 'posts6_FS': posts6_FS,
                'posts7_FS': posts7_FS, 'posts8_FS': posts8_FS, 'posts9_FS': posts9_FS, 'posts10_FS': posts10_FS,
                'posts11_FS': posts11_FS,
                'posts12_FS': posts12_FS, 'posts13_FS': posts13_FS,
                'posts14_FS': posts14_FS, 'posts15_FS': posts15_FS, 'posts16_FS': posts16_FS, 'posts17_FS': posts17_FS,
                'posts18_FS': posts18_FS,
                'posts19_FS': posts19_FS,
                'posts20_FS': posts20_FS,
                'posts1_W': posts1_W, 'posts2_W': posts2_W, 'posts3_W': posts3_W, 'posts4_W': posts4_W,
                'posts5_W': posts5_W, 'posts6_W': posts6_W,
                'posts7_W': posts7_W, 'posts8_W': posts8_W, 'posts9_W': posts9_W, 'posts10_W': posts10_W,
                'posts11_W': posts11_W,
                'posts12_W': posts12_W, 'posts13_W': posts13_W,
                'posts14_W': posts14_W, 'posts15_W': posts15_W, 'posts16_W': posts16_W, 'posts17_W': posts17_W,
                'posts18_W': posts18_W,
                'posts19_W': posts19_W,
                'posts20_W': posts20_W,
                'posts1_TS': posts1_TS, 'posts2_TS': posts2_TS, 'posts3_TS': posts3_TS, 'posts4_TS': posts4_TS,
                'posts5_TS': posts5_TS, 'posts6_TS': posts6_TS,
                'posts7_TS': posts7_TS, 'posts8_TS': posts8_TS, 'posts9_TS': posts9_TS, 'posts10_TS': posts10_TS,
                'posts11_TS': posts11_TS,
                'posts12_TS': posts12_TS, 'posts13_TS': posts13_TS,
                'posts14_TS': posts14_TS, 'posts15_TS': posts15_TS, 'posts16_TS': posts16_TS, 'posts17_TS': posts17_TS,
                'posts18_TS': posts18_TS,
                'posts19_TS': posts19_TS,
                'posts20_TS': posts20_TS,
                'posts1_SM': posts1_SM, 'posts2_SM': posts2_SM, 'posts3_SM': posts3_SM, 'posts4_SM': posts4_SM,
                'posts5_SM': posts5_SM, 'posts6_SM': posts6_SM,
                'posts7_SM': posts7_SM, 'posts8_SM': posts8_SM, 'posts9_SM': posts9_SM, 'posts10_SM': posts10_SM,
                'posts11_SM': posts11_SM,
                'posts12_SM': posts12_SM, 'posts13_SM': posts13_SM,
                'posts14_SM': posts14_SM, 'posts15_SM': posts15_SM, 'posts16_SM': posts16_SM, 'posts17_SM': posts17_SM,
                'posts18_SM': posts18_SM,
                'posts19_SM': posts19_SM,
                'posts20_SM': posts20_SM,
                'posts1_ST': posts1_ST, 'posts2_ST': posts2_ST, 'posts3_ST': posts3_ST, 'posts4_ST': posts4_ST,
                'posts5_ST': posts5_ST, 'posts6_ST': posts6_ST,
                'posts7_ST': posts7_ST, 'posts8_ST': posts8_ST, 'posts9_ST': posts9_ST, 'posts10_ST': posts10_ST,
                'posts11_ST': posts11_ST,
                'posts12_ST': posts12_ST, 'posts13_ST': posts13_ST,
                'posts14_ST': posts14_ST, 'posts15_ST': posts15_ST, 'posts16_ST': posts16_ST, 'posts17_ST': posts17_ST,
                'posts18_ST': posts18_ST,
                'posts19_ST': posts19_ST,
                'posts20_ST': posts20_ST,
                'posts1_P': posts1_P, 'posts2_P': posts2_P, 'posts3_P': posts3_P, 'posts4_P': posts4_P,
                'posts5_P': posts5_P, 'posts6_P': posts6_P,
                'posts7_P': posts7_P, 'posts8_P': posts8_P, 'posts9_P': posts9_P, 'posts10_P': posts10_P,
                'posts11_P': posts11_P,
                'posts12_P': posts12_P, 'posts13_P': posts13_P,
                'posts14_P': posts14_P, 'posts15_P': posts15_P, 'posts16_P': posts16_P, 'posts17_P': posts17_P,
                'posts18_P': posts18_P,
                'posts19_P': posts19_P,
                'posts20_P': posts20_P,
                }
        return render (request, self.template_name, args, )

class ExcelView(LoginRequiredMixin,ListView):
    template_name = 'login/excel.html'
    login_url = '/login/auth/'
    def get(self, request):
        # extra_utils.update_Warning()
        device = Device.objects.all().order_by("LaunchDate")
        args = {'Device': device}
        return render (request, self.template_name, args, )

class ProductView(LoginRequiredMixin,ListView):
    template_name = 'login/summary.html'
    login_url = '/login/auth/'
    def get(self, request):
        print("shreyas is here")
        print (request.user.has_perm('general.is_strategic'))
        extra_utils.update_Warning()
        device = Device.objects.all().order_by("LaunchDate")
        announcement = 1
        try:
            announcement = Announcements.objects.get(pk=1)
        except:
            print ("Error")
        else:
            print(announcement.post)
        args = {'Device': device, 'announcement':announcement,}
        return render (request, self.template_name, args, )

class IntermediateView(LoginRequiredMixin,TemplateView):
    template_name = 'login/test.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        devices = Device.objects.get(pk=pk)
        percent = int ((devices.ProductReadiness.completed + devices.DigitalContent.completed + devices.VideoContent.completed
                   + devices.CallCenterTraining.completed + devices.CallCenterOpertaions.completed + devices.ProductSupport.completed
                    + devices.Warehouse.completed + devices.FieldService.completed + devices.TechSupport.completed +
                    devices.ServiceMarketing.completed + devices.ServiceTraining.completed + devices.Parts.completed)/12)
        devices.completed = percent
        devices.save()
        args = {'devices':devices, 'percent':percent}
        return render(request, self.template_name, args )

class ProductReadinessView(LoginRequiredMixin,TemplateView):
    template_name = 'login/device1.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        form1 = Task1_pr_form()
        form2 = Task2_pr_form()
        form3 = Task3_pr_form()
        form4 = Task4_pr_form()
        form5 = Task5_pr_form()
        form6 = Task6_pr_form()
        form7 = Task7_pr_form()
        form8 = Task8_pr_form()
        form9 = Task9_pr_form()
        form10 = Task10_pr_form()
        form11 = Task11_pr_form()
        form12 = Task12_pr_form()
        form13 = Task13_pr_form()
        form14 = Task14_pr_form()
        form15 = Task15_pr_form()
        form16 = Task16_pr_form()
        form17 = Task17_pr_form()
        form18 = Task18_pr_form()
        form19 = Task19_pr_form()
        form20 = Task20_pr_form()
        devices = Device.objects.get(pk=pk)
        Task1_vc_dateform = Task1_pr_date_form(instance=devices.ProductReadiness)
        Task2_vc_dateform = Task2_pr_date_form(instance=devices.ProductReadiness)
        Task3_vc_dateform = Task3_pr_date_form(instance=devices.ProductReadiness)
        Task4_vc_dateform = Task4_pr_date_form(instance=devices.ProductReadiness)
        Task5_vc_dateform = Task5_pr_date_form(instance=devices.ProductReadiness)
        Task6_vc_dateform = Task6_pr_date_form(instance=devices.ProductReadiness)
        Task7_vc_dateform = Task7_pr_date_form(instance=devices.ProductReadiness)
        Task8_vc_dateform = Task8_pr_date_form(instance=devices.ProductReadiness)
        Task9_vc_dateform = Task9_pr_date_form(instance=devices.ProductReadiness)
        Task10_vc_dateform = Task10_pr_date_form(instance=devices.ProductReadiness)
        Task11_vc_dateform = Task11_pr_date_form(instance=devices.ProductReadiness)
        Task12_vc_dateform = Task12_pr_date_form(instance=devices.ProductReadiness)
        Task13_vc_dateform = Task13_pr_date_form(instance=devices.ProductReadiness)
        Task14_vc_dateform = Task14_pr_date_form(instance=devices.ProductReadiness)
        Task15_vc_dateform = Task15_pr_date_form(instance=devices.ProductReadiness)
        Task16_vc_dateform = Task16_pr_date_form(instance=devices.ProductReadiness)
        Task17_vc_dateform = Task17_pr_date_form(instance=devices.ProductReadiness)
        Task18_vc_dateform = Task18_pr_date_form(instance=devices.ProductReadiness)
        Task19_vc_dateform = Task19_pr_date_form(instance=devices.ProductReadiness)
        Task20_vc_dateform = Task20_pr_date_form(instance=devices.ProductReadiness)

        # Calculating % completed
        y = 0
        if devices.ProductReadiness.Task1_Name:
            y = y + 1
        if devices.ProductReadiness.Task2_Name:
            y = y + 1
        if devices.ProductReadiness.Task3_Name:
            y = y + 1
        if devices.ProductReadiness.Task4_Name:
            y = y + 1
        if devices.ProductReadiness.Task5_Name:
            y = y + 1
        if devices.ProductReadiness.Task6_Name:
            y = y + 1
        if devices.ProductReadiness.Task7_Name:
            y = y + 1
        if devices.ProductReadiness.Task8_Name:
            y = y + 1
        if devices.ProductReadiness.Task9_Name:
            y = y + 1
        if devices.ProductReadiness.Task10_Name:
            y = y + 1
        if devices.ProductReadiness.Task11_Name:
            y = y + 1
        if devices.ProductReadiness.Task12_Name:
            y = y + 1
        if devices.ProductReadiness.Task13_Name:
            y = y + 1
        if devices.ProductReadiness.Task14_Name:
            y = y + 1
        if devices.ProductReadiness.Task15_Name:
            y = y + 1
        if devices.ProductReadiness.Task16_Name:
            y = y + 1
        if devices.ProductReadiness.Task17_Name:
            y = y + 1
        if devices.ProductReadiness.Task18_Name:
            y = y + 1
        if devices.ProductReadiness.Task19_Name:
            y = y + 1
        if devices.ProductReadiness.Task20_Name:
            y = y + 1

        x = 0
        if devices.ProductReadiness.Task1_complete_date:
            x = x + 1
            devices.ProductReadiness.Task1_alert = False
            devices.ProductReadiness.Task1_warning = False
            devices.ProductReadiness.Status = 'On_Time'
        if devices.ProductReadiness.Task2_complete_date:
            x = x + 1
            devices.ProductReadiness.Task2_alert = False
            devices.ProductReadiness.Task2_warning = False
            devices.ProductReadiness.Status = 'On_Time'
        if devices.ProductReadiness.Task3_complete_date:
            x = x + 1
            devices.ProductReadiness.Task3_alert = False
            devices.ProductReadiness.Task3_warning = False
            devices.ProductReadiness.Status = 'On_Time'
        if devices.ProductReadiness.Task4_complete_date:
            x = x + 1
            devices.ProductReadiness.Task4_alert = False
            devices.ProductReadiness.Task4_warning = False
            devices.ProductReadiness.Status = 'On_Time'
        if devices.ProductReadiness.Task5_complete_date:
            x = x + 1
            devices.ProductReadiness.Task5_alert = False
            devices.ProductReadiness.Task5_warning = False
            devices.ProductReadiness.Status = 'On_Time'
        if devices.ProductReadiness.Task6_complete_date:
            x = x + 1
            devices.ProductReadiness.Task6_alert = False
            devices.ProductReadiness.Task6_warning = False
            devices.ProductReadiness.Status = 'On_Time'
        if devices.ProductReadiness.Task7_complete_date:
            x = x + 1
            devices.ProductReadiness.Task7_alert = False
            devices.ProductReadiness.Task7_warning = False
            devices.ProductReadiness.Status = 'On_Time'
        if devices.ProductReadiness.Task8_complete_date:
            x = x + 1
            devices.ProductReadiness.Task8_alert = False
            devices.ProductReadiness.Task8_warning = False
            devices.ProductReadiness.Status = 'On_Time'
        if devices.ProductReadiness.Task9_complete_date:
            x = x + 1
            devices.ProductReadiness.Task9_alert = False
            devices.ProductReadiness.Task9_warning = False
            devices.ProductReadiness.Status = 'On_Time'
        if devices.ProductReadiness.Task10_complete_date:
            x = x + 1
            devices.ProductReadiness.Task10_alert = False
            devices.ProductReadiness.Task10_warning = False
            devices.ProductReadiness.Status = 'On_Time'
        if devices.ProductReadiness.Task11_complete_date:
            x = x + 1
            devices.ProductReadiness.Task11_alert = False
            devices.ProductReadiness.Task11_warning = False
            devices.ProductReadiness.Status = 'On_Time'
        if devices.ProductReadiness.Task12_complete_date:
            x = x + 1
            devices.ProductReadiness.Task12_alert = False
            devices.ProductReadiness.Task12_warning = False
            devices.ProductReadiness.Status = 'On_Time'
        if devices.ProductReadiness.Task13_complete_date:
            x = x + 1
            devices.ProductReadiness.Task13_alert = False
            devices.ProductReadiness.Task13_warning = False
            devices.ProductReadiness.Status = 'On_Time'
        if devices.ProductReadiness.Task14_complete_date:
            x = x + 1
            devices.ProductReadiness.Task14_alert = False
            devices.ProductReadiness.Task14_warning = False
            devices.ProductReadiness.Status = 'On_Time'
        if devices.ProductReadiness.Task15_complete_date:
            x = x + 1
            devices.ProductReadiness.Task15_alert = False
            devices.ProductReadiness.Task15_warning = False
            devices.ProductReadiness.Status = 'On_Time'
        if devices.ProductReadiness.Task16_complete_date:
            x = x + 1
            devices.ProductReadiness.Task16_alert = False
            devices.ProductReadiness.Task16_warning = False
            devices.ProductReadiness.Status = 'On_Time'
        if devices.ProductReadiness.Task17_complete_date:
            x = x + 1
            devices.ProductReadiness.Task17_alert = False
            devices.ProductReadiness.Task17_warning = False
            devices.ProductReadiness.Status = 'On_Time'
        if devices.ProductReadiness.Task18_complete_date:
            x = x + 1
            devices.ProductReadiness.Task18_alert = False
            devices.ProductReadiness.Task18_warning = False
            devices.ProductReadiness.Status = 'On_Time'
        if devices.ProductReadiness.Task19_complete_date:
            x = x + 1
            devices.ProductReadiness.Task19_alert = False
            devices.ProductReadiness.Task19_warning = False
            devices.ProductReadiness.Status = 'On_Time'
        if devices.ProductReadiness.Task20_complete_date:
            x = x + 1
            devices.ProductReadiness.Task20_alert = False
            devices.ProductReadiness.Task20_warning = False
            devices.ProductReadiness.Status = 'On_Time'
        percent = x / y * 100
        print (percent)

        # alerting logic
        today = datetime.date.today()
        if devices.ProductReadiness.Task1_End_Date:
            Task1_delta = devices.ProductReadiness.Task1_End_Date - today
        else:
            Task1_delta = None
        if devices.ProductReadiness.Task2_End_Date:
            Task2_delta = devices.ProductReadiness.Task2_End_Date - today
        else:
            Task2_delta = None
        if devices.ProductReadiness.Task3_End_Date:
            Task3_delta = devices.ProductReadiness.Task3_End_Date - today
        else:
            Task3_delta = None
        if devices.ProductReadiness.Task4_End_Date:
            Task4_delta = devices.ProductReadiness.Task4_End_Date - today
        else:
            Task4_delta = None
        if devices.ProductReadiness.Task5_End_Date:
            Task5_delta = devices.ProductReadiness.Task5_End_Date - today
        else:
            Task5_delta = None
        if devices.ProductReadiness.Task6_End_Date:
            Task6_delta = devices.ProductReadiness.Task6_End_Date - today
        else:
            Task6_delta = None
        if devices.ProductReadiness.Task7_End_Date:
            Task7_delta = devices.ProductReadiness.Task7_End_Date - today
        else:
            Task7_delta = None
        if devices.ProductReadiness.Task8_End_Date:
            Task8_delta = devices.ProductReadiness.Task8_End_Date - today
        else:
            Task8_delta = None
        if devices.ProductReadiness.Task9_End_Date:
            Task9_delta = devices.ProductReadiness.Task9_End_Date - today
        else:
            Task9_delta = None
        if devices.ProductReadiness.Task10_End_Date:
            Task10_delta = devices.ProductReadiness.Task10_End_Date - today
        else:
            Task10_delta = None
        if devices.ProductReadiness.Task11_End_Date:
            Task11_delta = devices.ProductReadiness.Task11_End_Date - today
        else:
            Task11_delta = None
        if devices.ProductReadiness.Task12_End_Date:
            Task12_delta = devices.ProductReadiness.Task12_End_Date - today
        else:
            Task12_delta = None
        if devices.ProductReadiness.Task13_End_Date:
            Task13_delta = devices.ProductReadiness.Task13_End_Date - today
        else:
            Task13_delta = None
        if devices.ProductReadiness.Task14_End_Date:
            Task14_delta = devices.ProductReadiness.Task14_End_Date - today
        else:
            Task14_delta = None
        if devices.ProductReadiness.Task15_End_Date:
            Task15_delta = devices.ProductReadiness.Task15_End_Date - today
        else:
            Task15_delta = None
        if devices.ProductReadiness.Task16_End_Date:
            Task16_delta = devices.ProductReadiness.Task16_End_Date - today
        else:
            Task16_delta = None
        if devices.ProductReadiness.Task17_End_Date:
            Task17_delta = devices.ProductReadiness.Task17_End_Date - today
        else:
            Task17_delta = None
        if devices.ProductReadiness.Task18_End_Date:
            Task18_delta = devices.ProductReadiness.Task18_End_Date - today
        else:
            Task18_delta = None
        if devices.ProductReadiness.Task19_End_Date:
            Task19_delta = devices.ProductReadiness.Task19_End_Date - today
        else:
            Task19_delta = None
        if devices.ProductReadiness.Task20_End_Date:
            Task20_delta = devices.ProductReadiness.Task20_End_Date - today
        else:
            Task20_delta = None

        if Task1_delta and Task1_delta < timedelta(
                devices.ProductReadiness.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not devices.ProductReadiness.Task1_complete_date:
            devices.ProductReadiness.Task1_warning = True
            devices.ProductReadiness.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(
                devices.ProductReadiness.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not devices.ProductReadiness.Task2_complete_date:
            devices.ProductReadiness.Task2_warning = True
            devices.ProductReadiness.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(
                devices.ProductReadiness.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not devices.ProductReadiness.Task3_complete_date:
            devices.ProductReadiness.Task3_warning = True
            devices.ProductReadiness.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(
                devices.ProductReadiness.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not devices.ProductReadiness.Task4_complete_date:
            devices.ProductReadiness.Task4_warning = True
            devices.ProductReadiness.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(
                devices.ProductReadiness.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not devices.ProductReadiness.Task5_complete_date:
            devices.ProductReadiness.Task5_warning = True
            devices.ProductReadiness.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(
                devices.ProductReadiness.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not devices.ProductReadiness.Task6_complete_date:
            devices.ProductReadiness.Task6_warning = True
            devices.ProductReadiness.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(
                devices.ProductReadiness.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not devices.ProductReadiness.Task7_complete_date:
            devices.ProductReadiness.Task7_warning = True
            devices.ProductReadiness.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(
                devices.ProductReadiness.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not devices.ProductReadiness.Task8_complete_date:
            devices.ProductReadiness.Task8_warning = True
            devices.ProductReadiness.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(
                devices.ProductReadiness.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not devices.ProductReadiness.Task9_complete_date:
            devices.ProductReadiness.Task9_warning = True
            devices.ProductReadiness.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(
                devices.ProductReadiness.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not devices.ProductReadiness.Task10_complete_date:
            devices.ProductReadiness.Task10_warning = True
            devices.ProductReadiness.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(
                devices.ProductReadiness.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not devices.ProductReadiness.Task11_complete_date:
            devices.ProductReadiness.Task11_warning = True
            devices.ProductReadiness.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(
                devices.ProductReadiness.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not devices.ProductReadiness.Task12_complete_date:
            devices.ProductReadiness.Task12_warning = True
            devices.ProductReadiness.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(
                devices.ProductReadiness.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not devices.ProductReadiness.Task13_complete_date:
            devices.ProductReadiness.Task13_warning = True
            devices.ProductReadiness.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(
                devices.ProductReadiness.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not devices.ProductReadiness.Task14_complete_date:
            devices.ProductReadiness.Task14_warning = True
            devices.ProductReadiness.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(
                devices.ProductReadiness.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not devices.ProductReadiness.Task15_complete_date:
            devices.ProductReadiness.Task15_warning = True
            devices.ProductReadiness.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(
                devices.ProductReadiness.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not devices.ProductReadiness.Task16_complete_date:
            devices.ProductReadiness.Task16_warning = True
            devices.ProductReadiness.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(
                devices.ProductReadiness.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not devices.ProductReadiness.Task17_complete_date:
            devices.ProductReadiness.Task17_warning = True
            devices.ProductReadiness.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(
                devices.ProductReadiness.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not devices.ProductReadiness.Task18_complete_date:
            devices.ProductReadiness.Task18_warning = True
            devices.ProductReadiness.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(
                devices.ProductReadiness.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not devices.ProductReadiness.Task19_complete_date:
            devices.ProductReadiness.Task19_warning = True
            devices.ProductReadiness.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(
                devices.ProductReadiness.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not devices.ProductReadiness.Task20_complete_date:
            devices.ProductReadiness.Task20_warning = True
            devices.ProductReadiness.Status = 'At Risk'

        if devices.ProductReadiness.Task1_End_Date and Task1_delta < timedelta(
                0) and not devices.ProductReadiness.Task1_complete_date:
            devices.ProductReadiness.Task1_alert = True
            devices.ProductReadiness.Status = 'Delayed'
        if devices.ProductReadiness.Task2_End_Date and Task2_delta < timedelta(
                0) and not devices.ProductReadiness.Task2_complete_date:
            devices.ProductReadiness.Task2_alert = True
            devices.ProductReadiness.Status = 'Delayed'
        if devices.ProductReadiness.Task3_End_Date and Task3_delta < timedelta(
                0) and not devices.ProductReadiness.Task3_complete_date:
            devices.ProductReadiness.Task3_alert = True
            devices.ProductReadiness.Status = 'Delayed'
        if devices.ProductReadiness.Task4_End_Date and Task4_delta < timedelta(
                0) and not devices.ProductReadiness.Task4_complete_date:
            devices.ProductReadiness.Task4_alert = True
            devices.ProductReadiness.Status = 'Delayed'
        if devices.ProductReadiness.Task5_End_Date and Task5_delta < timedelta(
                0) and not devices.ProductReadiness.Task5_complete_date:
            devices.ProductReadiness.Task5_alert = True
            devices.ProductReadiness.Status = 'Delayed'
        if devices.ProductReadiness.Task6_End_Date and Task6_delta < timedelta(
                0) and not devices.ProductReadiness.Task6_complete_date:
            devices.ProductReadiness.Task6_alert = True
            devices.ProductReadiness.Status = 'Delayed'
        if devices.ProductReadiness.Task7_End_Date and Task7_delta < timedelta(
                0) and not devices.ProductReadiness.Task7_complete_date:
            devices.ProductReadiness.Task7_alert = True
            devices.ProductReadiness.Status = 'Delayed'
        if devices.ProductReadiness.Task8_End_Date and Task8_delta < timedelta(
                0) and not devices.ProductReadiness.Task8_complete_date:
            devices.ProductReadiness.Task8_alert = True
            devices.ProductReadiness.Status = 'Delayed'
        if devices.ProductReadiness.Task9_End_Date and Task9_delta < timedelta(
                0) and not devices.ProductReadiness.Task9_complete_date:
            devices.ProductReadiness.Task9_alert = True
            devices.ProductReadiness.Status = 'Delayed'
        if devices.ProductReadiness.Task10_End_Date and Task10_delta < timedelta(
                0) and not devices.ProductReadiness.Task10_complete_date:
            devices.ProductReadiness.Task10_alert = True
            devices.ProductReadiness.Status = 'Delayed'
        if devices.ProductReadiness.Task11_End_Date and Task11_delta < timedelta(
                0) and not devices.ProductReadiness.Task11_complete_date:
            devices.ProductReadiness.Task11_alert = True
            devices.ProductReadiness.Status = 'Delayed'
        if devices.ProductReadiness.Task12_End_Date and Task12_delta < timedelta(
                0) and not devices.ProductReadiness.Task12_complete_date:
            devices.ProductReadiness.Task12_alert = True
            devices.ProductReadiness.Status = 'Delayed'
        if devices.ProductReadiness.Task13_End_Date and Task13_delta < timedelta(
                0) and not devices.ProductReadiness.Task13_complete_date:
            devices.ProductReadiness.Task13_alert = True
            devices.ProductReadiness.Status = 'Delayed'
        if devices.ProductReadiness.Task14_End_Date and Task14_delta < timedelta(
                0) and not devices.ProductReadiness.Task14_complete_date:
            devices.ProductReadiness.Task14_alert = True
            devices.ProductReadiness.Status = 'Delayed'
        if devices.ProductReadiness.Task15_End_Date and Task15_delta < timedelta(
                0) and not devices.ProductReadiness.Task15_complete_date:
            devices.ProductReadiness.Task15_alert = True
            devices.ProductReadiness.Status = 'Delayed'
        if devices.ProductReadiness.Task16_End_Date and Task16_delta < timedelta(
                0) and not devices.ProductReadiness.Task16_complete_date:
            devices.ProductReadiness.Task16_alert = True
            devices.ProductReadiness.Status = 'Delayed'
        if devices.ProductReadiness.Task17_End_Date and Task17_delta < timedelta(
                0) and not devices.ProductReadiness.Task17_complete_date:
            devices.ProductReadiness.Task17_alert = True
            devices.ProductReadiness.Status = 'Delayed'
        if devices.ProductReadiness.Task18_End_Date and Task18_delta < timedelta(
                0) and not devices.ProductReadiness.Task18_complete_date:
            devices.ProductReadiness.Task18_alert = True
            devices.ProductReadiness.Status = 'Delayed'
        if devices.ProductReadiness.Task19_End_Date and Task19_delta < timedelta(
                0) and not devices.ProductReadiness.Task19_complete_date:
            devices.ProductReadiness.Task19_alert = True
            devices.ProductReadiness.Status = 'Delayed'
        if devices.ProductReadiness.Task20_End_Date and Task20_delta < timedelta(
                0) and not devices.ProductReadiness.Task20_complete_date:
            devices.ProductReadiness.Task20_alert = True
            devices.ProductReadiness.Status = 'Delayed'



        devices.ProductReadiness.completed = int(percent)
        devices.ProductReadiness.save()
        posts1 = devices.ProductReadiness.task1statusproductreadiness_set.all().order_by('-created')
        posts2 = devices.ProductReadiness.task2statusproductreadiness_set.all().order_by('-created')
        posts3 = devices.ProductReadiness.task3statusproductreadiness_set.all().order_by('-created')
        posts4 = devices.ProductReadiness.task4statusproductreadiness_set.all().order_by('-created')
        posts5 = devices.ProductReadiness.task5statusproductreadiness_set.all().order_by('-created')
        posts6 = devices.ProductReadiness.task6statusproductreadiness_set.all().order_by('-created')
        posts7 = devices.ProductReadiness.task7statusproductreadiness_set.all().order_by('-created')
        posts8 = devices.ProductReadiness.task8statusproductreadiness_set.all().order_by('-created')
        posts9 = devices.ProductReadiness.task9statusproductreadiness_set.all().order_by('-created')
        posts10 = devices.ProductReadiness.task10statusproductreadiness_set.all().order_by('-created')
        posts11 = devices.ProductReadiness.task11statusproductreadiness_set.all().order_by('-created')
        posts12 = devices.ProductReadiness.task12statusproductreadiness_set.all().order_by('-created')
        posts13 = devices.ProductReadiness.task13statusproductreadiness_set.all().order_by('-created')
        posts14 = devices.ProductReadiness.task14statusproductreadiness_set.all().order_by('-created')
        posts15 = devices.ProductReadiness.task15statusproductreadiness_set.all().order_by('-created')
        posts16 = devices.ProductReadiness.task16statusproductreadiness_set.all().order_by('-created')
        posts17 = devices.ProductReadiness.task17statusproductreadiness_set.all().order_by('-created')
        posts18 = devices.ProductReadiness.task18statusproductreadiness_set.all().order_by('-created')
        posts19 = devices.ProductReadiness.task19statusproductreadiness_set.all().order_by('-created')
        posts20 = devices.ProductReadiness.task20statusproductreadiness_set.all().order_by('-created')

        args = {'devices': devices, 'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5,
                'form6': form6,
                'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12,
                'form13': form13,
                'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17, 'form18': form18,
                'form19': form19,
                'form20': form20, 'posts1': posts1, 'posts2': posts2, 'posts3': posts3, 'posts4': posts4,
                'posts5': posts5, 'posts6': posts6,
                'posts7': posts7, 'posts8': posts8, 'posts9': posts9, 'posts10': posts10, 'posts11': posts11,
                'posts12': posts12, 'posts13': posts13,
                'posts14': posts14, 'posts15': posts15, 'posts16': posts16, 'posts17': posts17, 'posts18': posts18,
                'posts19': posts19,
                'posts20': posts20, 'Task1_vc_dateform': Task1_vc_dateform, 'Task2_vc_dateform': Task2_vc_dateform,
                'Task3_vc_dateform': Task3_vc_dateform, 'Task4_vc_dateform': Task4_vc_dateform,
                'Task5_vc_dateform': Task5_vc_dateform, 'Task6_vc_dateform': Task6_vc_dateform,
                'Task7_vc_dateform': Task7_vc_dateform, 'Task8_vc_dateform': Task8_vc_dateform,
                'Task9_vc_dateform': Task9_vc_dateform, 'Task10_vc_dateform': Task10_vc_dateform,
                'Task11_vc_dateform': Task11_vc_dateform, 'Task12_vc_dateform': Task12_vc_dateform,
                'Task13_vc_dateform': Task13_vc_dateform, 'Task14_vc_dateform': Task14_vc_dateform,
                'Task15_vc_dateform': Task15_vc_dateform, 'Task16_vc_dateform': Task16_vc_dateform,
                'Task17_vc_dateform': Task17_vc_dateform, 'Task18_vc_dateform': Task18_vc_dateform,
                'Task19_vc_dateform': Task19_vc_dateform, 'Task20_vc_dateform': Task20_vc_dateform,
                'Task1_delta': Task1_delta, 'Task7_delta': Task7_delta, 'Task12_delta': Task12_delta,
                'Task17_delta': Task17_delta,
                'Task2_delta': Task2_delta, 'Task8_delta': Task8_delta, 'Task13_delta': Task13_delta,
                'Task3_delta': Task3_delta, 'Task9_delta': Task9_delta, 'Task14_delta': Task14_delta,
                'Task18_delta': Task18_delta,
                'Task4_delta': Task4_delta, 'Task10_delta': Task10_delta, 'Task15_delta': Task15_delta,
                'Task19_delta': Task19_delta,
                'Task5_delta': Task5_delta, 'Task11_delta': Task11_delta, 'Task16_delta': Task16_delta,
                'Task20_delta': Task20_delta,
                'Task6_delta': Task6_delta,
                }
        return render(request, self.template_name, args)

    def post(self, request, pk):

        form1 = Task1_pr_form(request.POST)
        form2 = Task2_pr_form(request.POST)
        form3 = Task3_pr_form(request.POST)
        form4 = Task4_pr_form(request.POST)
        form5 = Task5_pr_form(request.POST)
        form6 = Task6_pr_form(request.POST)
        form7 = Task7_pr_form(request.POST)
        form8 = Task8_pr_form(request.POST)
        form9 = Task9_pr_form(request.POST)
        form10 = Task10_pr_form(request.POST)
        form11 = Task11_pr_form(request.POST)
        form12 = Task12_pr_form(request.POST)
        form13 = Task13_pr_form(request.POST)
        form14 = Task14_pr_form(request.POST)
        form15 = Task15_pr_form(request.POST)
        form16 = Task16_pr_form(request.POST)
        form17 = Task17_pr_form(request.POST)
        form18 = Task18_pr_form(request.POST)
        form19 = Task19_pr_form(request.POST)
        form20 = Task20_pr_form(request.POST)
        devices = Device.objects.get(pk=pk)

        Task1_vc_dateform = Task1_pr_date_form(request.POST, instance=devices.ProductReadiness)
        Task2_vc_dateform = Task2_pr_date_form(request.POST, instance=devices.ProductReadiness)
        Task3_vc_dateform = Task3_pr_date_form(request.POST, instance=devices.ProductReadiness)
        Task4_vc_dateform = Task4_pr_date_form(request.POST, instance=devices.ProductReadiness)
        Task5_vc_dateform = Task5_pr_date_form(request.POST, instance=devices.ProductReadiness)
        Task6_vc_dateform = Task6_pr_date_form(request.POST, instance=devices.ProductReadiness)
        Task7_vc_dateform = Task7_pr_date_form(request.POST, instance=devices.ProductReadiness)
        Task8_vc_dateform = Task8_pr_date_form(request.POST, instance=devices.ProductReadiness)
        Task9_vc_dateform = Task9_pr_date_form(request.POST, instance=devices.ProductReadiness)
        Task10_vc_dateform = Task10_pr_date_form(request.POST, instance=devices.ProductReadiness)
        Task11_vc_dateform = Task11_pr_date_form(request.POST, instance=devices.ProductReadiness)
        Task12_vc_dateform = Task12_pr_date_form(request.POST, instance=devices.ProductReadiness)
        Task13_vc_dateform = Task13_pr_date_form(request.POST, instance=devices.ProductReadiness)
        Task14_vc_dateform = Task14_pr_date_form(request.POST, instance=devices.ProductReadiness)
        Task15_vc_dateform = Task15_pr_date_form(request.POST, instance=devices.ProductReadiness)
        Task16_vc_dateform = Task16_pr_date_form(request.POST, instance=devices.ProductReadiness)
        Task17_vc_dateform = Task17_pr_date_form(request.POST, instance=devices.ProductReadiness)
        Task18_vc_dateform = Task18_pr_date_form(request.POST, instance=devices.ProductReadiness)
        Task19_vc_dateform = Task19_pr_date_form(request.POST, instance=devices.ProductReadiness)
        Task20_vc_dateform = Task20_pr_date_form(request.POST, instance=devices.ProductReadiness)

        if 'Task1Submit' in request.POST:
            if form1.is_valid() and Task1_vc_dateform.is_valid():
                post = form1.save(commit=False)
                post.user = request.user
                post.Parts = devices.ProductReadiness
                Task1_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/productreadiness')
            else:
                return redirect('/login/summary/' + pk + '/productreadiness')
        elif 'Task2Submit' in request.POST:
            if form2.is_valid() and Task2_vc_dateform.is_valid():
                post = form2.save(commit=False)
                post.user = request.user
                post.Parts = devices.ProductReadiness
                Task2_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/productreadiness')
            else:
                return redirect('/login/summary/' + pk + '/productreadiness')
        elif 'Task3Submit' in request.POST:
            if form3.is_valid() and Task3_vc_dateform.is_valid():
                post = form3.save(commit=False)
                post.user = request.user
                post.Parts = devices.ProductReadiness
                Task3_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/productreadiness')
            else:
                return redirect('/login/summary/' + pk + '/productreadiness')
        elif 'Task4Submit' in request.POST:
            if form4.is_valid() and Task4_vc_dateform.is_valid():
                post = form4.save(commit=False)
                post.user = request.user
                post.Parts = devices.ProductReadiness
                Task4_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/productreadiness')
            else:
                return redirect('/login/summary/' + pk + '/productreadiness')
        elif 'Task5Submit' in request.POST:
            if form5.is_valid() and Task5_vc_dateform.is_valid():
                post = form5.save(commit=False)
                post.user = request.user
                post.Parts = devices.ProductReadiness
                Task5_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/productreadiness')
            else:
                return redirect('/login/summary/' + pk + '/productreadiness')
        elif 'Task6Submit' in request.POST:
            if form6.is_valid() and Task6_vc_dateform.is_valid():
                post = form6.save(commit=False)
                post.user = request.user
                post.Parts = devices.ProductReadiness
                Task6_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/productreadiness')
            else:
                return redirect('/login/summary/' + pk + '/productreadiness')
        elif 'Task7Submit' in request.POST:
            if form7.is_valid() and Task7_vc_dateform.is_valid():
                post = form7.save(commit=False)
                post.user = request.user
                post.Parts = devices.ProductReadiness
                Task7_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/productreadiness')
            else:
                return redirect('/login/summary/' + pk + '/productreadiness')
        elif 'Task8Submit' in request.POST:
            if form8.is_valid() and Task8_vc_dateform.is_valid():
                post = form8.save(commit=False)
                post.user = request.user
                post.Parts = devices.ProductReadiness
                Task8_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/productreadiness')
            else:
                return redirect('/login/summary/' + pk + '/productreadiness')
        elif 'Task9Submit' in request.POST:
            if form9.is_valid() and Task9_vc_dateform.is_valid():
                post = form9.save(commit=False)
                post.user = request.user
                post.Parts = devices.ProductReadiness
                Task9_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/productreadiness')
            else:
                return redirect('/login/summary/' + pk + '/productreadiness')
        elif 'Task10Submit' in request.POST:
            if form10.is_valid() and Task10_vc_dateform.is_valid():
                post = form10.save(commit=False)
                post.user = request.user
                post.Parts = devices.ProductReadiness
                Task10_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/productreadiness')
            else:
                return redirect('/login/summary/' + pk + '/productreadiness')
        elif 'Task11Submit' in request.POST:
            if form11.is_valid() and Task11_vc_dateform.is_valid():
                post = form11.save(commit=False)
                post.user = request.user
                post.Parts = devices.ProductReadiness
                Task11_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/productreadiness')
            else:
                return redirect('/login/summary/' + pk + '/productreadiness')
        elif 'Task12Submit' in request.POST:
            if form12.is_valid() and Task12_vc_dateform.is_valid():
                post = form12.save(commit=False)
                post.user = request.user
                post.Parts = devices.ProductReadiness
                Task12_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/productreadiness')
            else:
                return redirect('/login/summary/' + pk + '/productreadiness')
        elif 'Task13Submit' in request.POST:
            if form13.is_valid() and Task13_vc_dateform.is_valid():
                post = form13.save(commit=False)
                post.user = request.user
                post.Parts = devices.ProductReadiness
                Task13_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/productreadiness')
            else:
                return redirect('/login/summary/' + pk + '/productreadiness')
        elif 'Task14Submit' in request.POST:
            if form14.is_valid() and Task14_vc_dateform.is_valid():
                post = form14.save(commit=False)
                post.user = request.user
                post.Parts = devices.ProductReadiness
                Task14_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/productreadiness')
            else:
                return redirect('/login/summary/' + pk + '/productreadiness')
        elif 'Task15Submit' in request.POST:
            if form15.is_valid() and Task15_vc_dateform.is_valid():
                post = form15.save(commit=False)
                post.user = request.user
                post.Parts = devices.ProductReadiness
                Task15_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/productreadiness')
            else:
                return redirect('/login/summary/' + pk + '/productreadiness')
        elif 'Task16Submit' in request.POST:
            if form16.is_valid() and Task16_vc_dateform.is_valid():
                post = form16.save(commit=False)
                post.user = request.user
                post.Parts = devices.ProductReadiness
                Task16_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/productreadiness')
            else:
                return redirect('/login/summary/' + pk + '/productreadiness')
        elif 'Task17Submit' in request.POST:
            if form17.is_valid() and Task17_vc_dateform.is_valid():
                post = form17.save(commit=False)
                post.user = request.user
                post.Parts = devices.ProductReadiness
                Task17_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/productreadiness')
            else:
                return redirect('/login/summary/' + pk + '/productreadiness')
        elif 'Task18Submit' in request.POST:
            if form18.is_valid() and Task18_vc_dateform.is_valid():
                post = form18.save(commit=False)
                post.user = request.user
                post.Parts = devices.ProductReadiness
                Task18_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/productreadiness')
            else:
                return redirect('/login/summary/' + pk + '/productreadiness')
        elif 'Task19Submit' in request.POST:
            if form19.is_valid() and Task19_vc_dateform.is_valid():
                post = form19.save(commit=False)
                post.user = request.user
                post.Parts = devices.ProductReadiness
                Task19_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/productreadiness')
            else:
                return redirect('/login/summary/' + pk + '/productreadiness')
        elif 'Task20Submit' in request.POST:
            if form20.is_valid() and Task20_vc_dateform.is_valid():
                post = form20.save(commit=False)
                post.user = request.user
                post.Parts = devices.ProductReadiness
                Task20_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/productreadiness')
            else:
                return redirect('/login/summary/' + pk + '/productreadiness')
                

                ########################################################################################################################


class VideoContentView(LoginRequiredMixin,TemplateView):
    template_name = 'login/device2.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        form1 = Task1_vc_form()
        form2 = Task2_vc_form()
        form3 = Task3_vc_form()
        form4 = Task4_vc_form()
        form5 = Task5_vc_form()
        form6 = Task6_vc_form()
        form7 = Task7_vc_form()
        form8 = Task8_vc_form()
        form9 = Task9_vc_form()
        form10 = Task10_vc_form()
        form11 = Task11_vc_form()
        form12 = Task12_vc_form()
        form13 = Task13_vc_form()
        form14 = Task14_vc_form()
        form15 = Task15_vc_form()
        form16 = Task16_vc_form()
        form17 = Task17_vc_form()
        form18 = Task18_vc_form()
        form19 = Task19_vc_form()
        form20 = Task20_vc_form()
        devices = Device.objects.get(pk=pk)
        Task1_vc_dateform = Task1_vc_date_form(instance=devices.VideoContent)
        Task2_vc_dateform = Task2_vc_date_form(instance=devices.VideoContent)
        Task3_vc_dateform = Task3_vc_date_form(instance=devices.VideoContent)
        Task4_vc_dateform = Task4_vc_date_form(instance=devices.VideoContent)
        Task5_vc_dateform = Task5_vc_date_form(instance=devices.VideoContent)
        Task6_vc_dateform = Task6_vc_date_form(instance=devices.VideoContent)
        Task7_vc_dateform = Task7_vc_date_form(instance=devices.VideoContent)
        Task8_vc_dateform = Task8_vc_date_form(instance=devices.VideoContent)
        Task9_vc_dateform = Task9_vc_date_form(instance=devices.VideoContent)
        Task10_vc_dateform = Task10_vc_date_form(instance=devices.VideoContent)
        Task11_vc_dateform = Task11_vc_date_form(instance=devices.VideoContent)
        Task12_vc_dateform = Task12_vc_date_form(instance=devices.VideoContent)
        Task13_vc_dateform = Task13_vc_date_form(instance=devices.VideoContent)
        Task14_vc_dateform = Task14_vc_date_form(instance=devices.VideoContent)
        Task15_vc_dateform = Task15_vc_date_form(instance=devices.VideoContent)
        Task16_vc_dateform = Task16_vc_date_form(instance=devices.VideoContent)
        Task17_vc_dateform = Task17_vc_date_form(instance=devices.VideoContent)
        Task18_vc_dateform = Task18_vc_date_form(instance=devices.VideoContent)
        Task19_vc_dateform = Task19_vc_date_form(instance=devices.VideoContent)
        Task20_vc_dateform = Task20_vc_date_form(instance=devices.VideoContent)

        #Calculating % completed
        y=0
        if devices.VideoContent.Task1_Name:
            y=y+1
        if devices.VideoContent.Task2_Name:
            y=y+1
        if devices.VideoContent.Task3_Name:
            y=y+1
        if devices.VideoContent.Task4_Name:
            y=y+1
        if devices.VideoContent.Task5_Name:
            y=y+1
        if devices.VideoContent.Task6_Name:
            y=y+1
        if devices.VideoContent.Task7_Name:
            y=y+1
        if devices.VideoContent.Task8_Name:
            y=y+1
        if devices.VideoContent.Task9_Name:
            y=y+1
        if devices.VideoContent.Task10_Name:
            y=y+1
        if devices.VideoContent.Task11_Name:
            y=y+1
        if devices.VideoContent.Task12_Name:
            y=y+1
        if devices.VideoContent.Task13_Name:
            y=y+1
        if devices.VideoContent.Task14_Name:
            y=y+1
        if devices.VideoContent.Task15_Name:
            y=y+1
        if devices.VideoContent.Task16_Name:
            y=y+1
        if devices.VideoContent.Task17_Name:
            y=y+1
        if devices.VideoContent.Task18_Name:
            y=y+1
        if devices.VideoContent.Task19_Name:
            y=y+1
        if devices.VideoContent.Task20_Name:
            y=y+1

        x = 0
        if devices.VideoContent.Task1_complete_date:
            x =x+1
            devices.VideoContent.Task1_alert = False
            devices.VideoContent.Task1_warning=False
            devices.VideoContent.Status='On_Time'
        if devices.VideoContent.Task2_complete_date:
            x = x + 1
            devices.VideoContent.Task2_alert = False
            devices.VideoContent.Task2_warning=False
            devices.VideoContent.Status = 'On_Time'
        if devices.VideoContent.Task3_complete_date:
            x = x + 1
            devices.VideoContent.Task3_alert = False
            devices.VideoContent.Task3_warning=False
            devices.VideoContent.Status = 'On_Time'
        if devices.VideoContent.Task4_complete_date:
            x = x + 1
            devices.VideoContent.Task4_alert = False
            devices.VideoContent.Task4_warning=False
            devices.VideoContent.Status = 'On_Time'
        if devices.VideoContent.Task5_complete_date:
            x = x + 1
            devices.VideoContent.Task5_alert = False
            devices.VideoContent.Task5_warning=False
            devices.VideoContent.Status = 'On_Time'
        if devices.VideoContent.Task6_complete_date:
            x = x + 1
            devices.VideoContent.Task6_alert = False
            devices.VideoContent.Task6_warning=False
            devices.VideoContent.Status = 'On_Time'
        if devices.VideoContent.Task7_complete_date:
            x =x+1
            devices.VideoContent.Task7_alert = False
            devices.VideoContent.Task7_warning=False
            devices.VideoContent.Status = 'On_Time'
        if devices.VideoContent.Task8_complete_date:
            x =x+1
            devices.VideoContent.Task8_alert = False
            devices.VideoContent.Task8_warning=False
            devices.VideoContent.Status = 'On_Time'
        if devices.VideoContent.Task9_complete_date:
            x =x+1
            devices.VideoContent.Task9_alert = False
            devices.VideoContent.Task9_warning=False
            devices.VideoContent.Status = 'On_Time'
        if devices.VideoContent.Task10_complete_date:
            x =x+1
            devices.VideoContent.Task10_alert = False
            devices.VideoContent.Task10_warning=False
            devices.VideoContent.Status = 'On_Time'
        if devices.VideoContent.Task11_complete_date:
            x =x+1
            devices.VideoContent.Task11_alert = False
            devices.VideoContent.Task11_warning=False
            devices.VideoContent.Status = 'On_Time'
        if devices.VideoContent.Task12_complete_date:
            x = x + 1
            devices.VideoContent.Task12_alert = False
            devices.VideoContent.Task12_warning=False
            devices.VideoContent.Status = 'On_Time'
        if devices.VideoContent.Task13_complete_date:
            x = x + 1
            devices.VideoContent.Task13_alert = False
            devices.VideoContent.Task13_warning=False
            devices.VideoContent.Status = 'On_Time'
        if devices.VideoContent.Task14_complete_date:
            x = x + 1
            devices.VideoContent.Task14_alert = False
            devices.VideoContent.Task14_warning=False
            devices.VideoContent.Status = 'On_Time'
        if devices.VideoContent.Task15_complete_date:
            x = x + 1
            devices.VideoContent.Task15_alert = False
            devices.VideoContent.Task15_warning=False
            devices.VideoContent.Status = 'On_Time'
        if devices.VideoContent.Task16_complete_date:
            x = x + 1
            devices.VideoContent.Task16_alert = False
            devices.VideoContent.Task16_warning=False
            devices.VideoContent.Status = 'On_Time'
        if devices.VideoContent.Task17_complete_date:
            x =x+1
            devices.VideoContent.Task17_alert = False
            devices.VideoContent.Task17_warning=False
            devices.VideoContent.Status = 'On_Time'
        if devices.VideoContent.Task18_complete_date:
            x =x+1
            devices.VideoContent.Task18_alert = False
            devices.VideoContent.Task18_warning=False
            devices.VideoContent.Status = 'On_Time'
        if devices.VideoContent.Task19_complete_date:
            x =x+1
            devices.VideoContent.Task19_alert = False
            devices.VideoContent.Task19_warning=False
            devices.VideoContent.Status = 'On_Time'
        if devices.VideoContent.Task20_complete_date:
            x =x+1
            devices.VideoContent.Task20_alert = False
            devices.VideoContent.Task20_warning=False
            devices.VideoContent.Status = 'On_Time'
        percent = x/y * 100
        print (percent)

        #alerting logic
        today = datetime.date.today()
        if devices.VideoContent.Task1_End_Date:
            Task1_delta =  devices.VideoContent.Task1_End_Date - today
        else:
            Task1_delta = None
        if devices.VideoContent.Task2_End_Date:
            Task2_delta = devices.VideoContent.Task2_End_Date - today
        else:
            Task2_delta = None
        if devices.VideoContent.Task3_End_Date:
            Task3_delta = devices.VideoContent.Task3_End_Date - today
        else:
            Task3_delta = None
        if devices.VideoContent.Task4_End_Date:
            Task4_delta = devices.VideoContent.Task4_End_Date - today
        else:
            Task4_delta = None
        if devices.VideoContent.Task5_End_Date:
            Task5_delta = devices.VideoContent.Task5_End_Date - today
        else:
            Task5_delta = None
        if devices.VideoContent.Task6_End_Date:
            Task6_delta = devices.VideoContent.Task6_End_Date - today
        else:
            Task6_delta = None
        if devices.VideoContent.Task7_End_Date:
            Task7_delta = devices.VideoContent.Task7_End_Date - today
        else:
            Task7_delta = None
        if devices.VideoContent.Task8_End_Date:
            Task8_delta = devices.VideoContent.Task8_End_Date - today
        else:
            Task8_delta = None
        if devices.VideoContent.Task9_End_Date:
            Task9_delta = devices.VideoContent.Task9_End_Date - today
        else:
            Task9_delta = None
        if devices.VideoContent.Task10_End_Date:
            Task10_delta =  devices.VideoContent.Task10_End_Date - today
        else:
            Task10_delta = None
        if devices.VideoContent.Task11_End_Date:
            Task11_delta =  devices.VideoContent.Task11_End_Date - today
        else:
            Task11_delta = None
        if devices.VideoContent.Task12_End_Date:
            Task12_delta = devices.VideoContent.Task12_End_Date - today
        else:
            Task12_delta = None
        if devices.VideoContent.Task13_End_Date:
            Task13_delta = devices.VideoContent.Task13_End_Date - today
        else:
            Task13_delta = None
        if devices.VideoContent.Task14_End_Date:
            Task14_delta = devices.VideoContent.Task14_End_Date - today
        else:
            Task14_delta = None
        if devices.VideoContent.Task15_End_Date:
            Task15_delta = devices.VideoContent.Task15_End_Date - today
        else:
            Task15_delta = None
        if devices.VideoContent.Task16_End_Date:
            Task16_delta = devices.VideoContent.Task16_End_Date - today
        else:
            Task16_delta = None
        if devices.VideoContent.Task17_End_Date:
            Task17_delta = devices.VideoContent.Task17_End_Date - today
        else:
            Task17_delta = None
        if devices.VideoContent.Task18_End_Date:
            Task18_delta = devices.VideoContent.Task18_End_Date - today
        else:
            Task18_delta = None
        if devices.VideoContent.Task19_End_Date:
            Task19_delta = devices.VideoContent.Task19_End_Date - today
        else:
            Task19_delta = None
        if devices.VideoContent.Task20_End_Date:
            Task20_delta = devices.VideoContent.Task20_End_Date - today
        else:
            Task20_delta = None

        if Task1_delta and Task1_delta < timedelta(devices.VideoContent.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not devices.VideoContent.Task1_complete_date:
            devices.VideoContent.Task1_warning = True
            devices.VideoContent.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(devices.VideoContent.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not devices.VideoContent.Task2_complete_date:
            devices.VideoContent.Task2_warning = True
            devices.VideoContent.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(devices.VideoContent.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not devices.VideoContent.Task3_complete_date:
            devices.VideoContent.Task3_warning = True
            devices.VideoContent.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(devices.VideoContent.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not devices.VideoContent.Task4_complete_date:
            devices.VideoContent.Task4_warning = True
            devices.VideoContent.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(devices.VideoContent.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not devices.VideoContent.Task5_complete_date:
            devices.VideoContent.Task5_warning = True
            devices.VideoContent.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(devices.VideoContent.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not devices.VideoContent.Task6_complete_date:
            devices.VideoContent.Task6_warning = True
            devices.VideoContent.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(devices.VideoContent.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not devices.VideoContent.Task7_complete_date:
            devices.VideoContent.Task7_warning = True
            devices.VideoContent.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(devices.VideoContent.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not devices.VideoContent.Task8_complete_date:
            devices.VideoContent.Task8_warning = True
            devices.VideoContent.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(devices.VideoContent.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not devices.VideoContent.Task9_complete_date:
            devices.VideoContent.Task9_warning = True
            devices.VideoContent.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(devices.VideoContent.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not devices.VideoContent.Task10_complete_date:
            devices.VideoContent.Task10_warning = True
            devices.VideoContent.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(devices.VideoContent.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not devices.VideoContent.Task11_complete_date:
            devices.VideoContent.Task11_warning = True
            devices.VideoContent.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(devices.VideoContent.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not devices.VideoContent.Task12_complete_date:
            devices.VideoContent.Task12_warning = True
            devices.VideoContent.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(devices.VideoContent.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not devices.VideoContent.Task13_complete_date:
            devices.VideoContent.Task13_warning = True
            devices.VideoContent.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(devices.VideoContent.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not devices.VideoContent.Task14_complete_date:
            devices.VideoContent.Task14_warning = True
            devices.VideoContent.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(devices.VideoContent.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not devices.VideoContent.Task15_complete_date:
            devices.VideoContent.Task15_warning = True
            devices.VideoContent.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(devices.VideoContent.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not devices.VideoContent.Task16_complete_date:
            devices.VideoContent.Task16_warning = True
            devices.VideoContent.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(devices.VideoContent.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not devices.VideoContent.Task17_complete_date:
            devices.VideoContent.Task17_warning = True
            devices.VideoContent.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(devices.VideoContent.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not devices.VideoContent.Task18_complete_date:
            devices.VideoContent.Task18_warning = True
            devices.VideoContent.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(devices.VideoContent.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not devices.VideoContent.Task19_complete_date:
            devices.VideoContent.Task19_warning = True
            devices.VideoContent.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(devices.VideoContent.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not devices.VideoContent.Task20_complete_date:
            devices.VideoContent.Task20_warning = True
            devices.VideoContent.Status = 'At Risk'

        if devices.VideoContent.Task1_End_Date and Task1_delta < timedelta(0) and not devices.VideoContent.Task1_complete_date:
            devices.VideoContent.Task1_alert = True
            devices.VideoContent.Status = 'Delayed'
        if devices.VideoContent.Task2_End_Date and Task2_delta < timedelta(0) and not devices.VideoContent.Task2_complete_date:
            devices.VideoContent.Task2_alert = True
            devices.VideoContent.Status = 'Delayed'
        if devices.VideoContent.Task3_End_Date and Task3_delta < timedelta(0) and not devices.VideoContent.Task3_complete_date:
            devices.VideoContent.Task3_alert = True
            devices.VideoContent.Status = 'Delayed'
        if devices.VideoContent.Task4_End_Date and Task4_delta < timedelta(0) and not devices.VideoContent.Task4_complete_date:
            devices.VideoContent.Task4_alert = True
            devices.VideoContent.Status = 'Delayed'
        if devices.VideoContent.Task5_End_Date and Task5_delta < timedelta(0) and not devices.VideoContent.Task5_complete_date:
            devices.VideoContent.Task5_alert = True
            devices.VideoContent.Status = 'Delayed'
        if devices.VideoContent.Task6_End_Date and Task6_delta < timedelta(0) and not devices.VideoContent.Task6_complete_date:
            devices.VideoContent.Task6_alert = True
            devices.VideoContent.Status = 'Delayed'
        if devices.VideoContent.Task7_End_Date and Task7_delta < timedelta(0) and not devices.VideoContent.Task7_complete_date:
            devices.VideoContent.Task7_alert = True
            devices.VideoContent.Status = 'Delayed'
        if devices.VideoContent.Task8_End_Date and Task8_delta < timedelta(0)and not devices.VideoContent.Task8_complete_date:
            devices.VideoContent.Task8_alert = True
            devices.VideoContent.Status = 'Delayed'
        if devices.VideoContent.Task9_End_Date and Task9_delta < timedelta(0)and not devices.VideoContent.Task9_complete_date:
            devices.VideoContent.Task9_alert = True
            devices.VideoContent.Status = 'Delayed'
        if devices.VideoContent.Task10_End_Date and Task10_delta < timedelta(0) and not devices.VideoContent.Task10_complete_date:
            devices.VideoContent.Task10_alert = True
            devices.VideoContent.Status = 'Delayed'
        if devices.VideoContent.Task11_End_Date and Task11_delta < timedelta(0) and not devices.VideoContent.Task11_complete_date:
            devices.VideoContent.Task11_alert = True
            devices.VideoContent.Status = 'Delayed'
        if devices.VideoContent.Task12_End_Date and Task12_delta < timedelta(0) and not devices.VideoContent.Task12_complete_date:
            devices.VideoContent.Task12_alert = True
            devices.VideoContent.Status = 'Delayed'
        if devices.VideoContent.Task13_End_Date and Task13_delta < timedelta(0) and not devices.VideoContent.Task13_complete_date:
            devices.VideoContent.Task13_alert = True
            devices.VideoContent.Status = 'Delayed'
        if devices.VideoContent.Task14_End_Date and Task14_delta < timedelta(0) and not devices.VideoContent.Task14_complete_date:
            devices.VideoContent.Task14_alert = True
            devices.VideoContent.Status = 'Delayed'
        if devices.VideoContent.Task15_End_Date and Task15_delta < timedelta(0) and not devices.VideoContent.Task15_complete_date:
            devices.VideoContent.Task15_alert = True
            devices.VideoContent.Status = 'Delayed'
        if devices.VideoContent.Task16_End_Date and Task16_delta < timedelta(0) and not devices.VideoContent.Task16_complete_date:
            devices.VideoContent.Task16_alert = True
            devices.VideoContent.Status = 'Delayed'
        if devices.VideoContent.Task17_End_Date and Task17_delta < timedelta(0)and not devices.VideoContent.Task17_complete_date:
            devices.VideoContent.Task17_alert = True
            devices.VideoContent.Status = 'Delayed'
        if devices.VideoContent.Task18_End_Date and Task18_delta < timedelta(0)and not devices.VideoContent.Task18_complete_date:
            devices.VideoContent.Task18_alert = True
            devices.VideoContent.Status = 'Delayed'
        if devices.VideoContent.Task19_End_Date and Task19_delta < timedelta(0)and not devices.VideoContent.Task19_complete_date:
            devices.VideoContent.Task19_alert = True
            devices.VideoContent.Status = 'Delayed'
        if devices.VideoContent.Task20_End_Date and Task20_delta < timedelta(0)and not devices.VideoContent.Task20_complete_date:
            devices.VideoContent.Task20_alert = True
            devices.VideoContent.Status = 'Delayed'

        devices.VideoContent.completed = int(percent)
        devices.VideoContent.save()
        posts1 = devices.VideoContent.task1statusvideocontent_set.all().order_by('-created')
        posts2 = devices.VideoContent.task2statusvideocontent_set.all().order_by('-created')
        posts3 = devices.VideoContent.task3statusvideocontent_set.all().order_by('-created')
        posts4 = devices.VideoContent.task4statusvideocontent_set.all().order_by('-created')
        posts5 = devices.VideoContent.task5statusvideocontent_set.all().order_by('-created')
        posts6 = devices.VideoContent.task6statusvideocontent_set.all().order_by('-created')
        posts7 = devices.VideoContent.task7statusvideocontent_set.all().order_by('-created')
        posts8 = devices.VideoContent.task8statusvideocontent_set.all().order_by('-created')
        posts9 = devices.VideoContent.task9statusvideocontent_set.all().order_by('-created')
        posts10 = devices.VideoContent.task10statusvideocontent_set.all().order_by('-created')
        posts11 = devices.VideoContent.task11statusvideocontent_set.all().order_by('-created')
        posts12 = devices.VideoContent.task12statusvideocontent_set.all().order_by('-created')
        posts13 = devices.VideoContent.task13statusvideocontent_set.all().order_by('-created')
        posts14 = devices.VideoContent.task14statusvideocontent_set.all().order_by('-created')
        posts15 = devices.VideoContent.task15statusvideocontent_set.all().order_by('-created')
        posts16 = devices.VideoContent.task16statusvideocontent_set.all().order_by('-created')
        posts17 = devices.VideoContent.task17statusvideocontent_set.all().order_by('-created')
        posts18 = devices.VideoContent.task18statusvideocontent_set.all().order_by('-created')
        posts19 = devices.VideoContent.task19statusvideocontent_set.all().order_by('-created')
        posts20 = devices.VideoContent.task20statusvideocontent_set.all().order_by('-created')

        args = {'devices':devices, 'form1':form1, 'form2':form2, 'form3':form3, 'form4':form4, 'form5':form5, 'form6':form6,
                'form7': form7, 'form8':form8, 'form9':form9, 'form10':form10, 'form11':form11, 'form12':form12, 'form13':form13,
                'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17, 'form18': form18, 'form19': form19,
                'form20': form20, 'posts1':posts1, 'posts2':posts2, 'posts3':posts3, 'posts4':posts4, 'posts5':posts5, 'posts6':posts6,
                'posts7': posts7, 'posts8':posts8, 'posts9':posts9, 'posts10':posts10, 'posts11':posts11, 'posts12':posts12, 'posts13':posts13,
                'posts14': posts14, 'posts15': posts15, 'posts16': posts16, 'posts17': posts17, 'posts18': posts18, 'posts19': posts19,
                'posts20': posts20, 'Task1_vc_dateform':Task1_vc_dateform, 'Task2_vc_dateform':Task2_vc_dateform,
                'Task3_vc_dateform':Task3_vc_dateform, 'Task4_vc_dateform':Task4_vc_dateform,
                'Task5_vc_dateform': Task5_vc_dateform, 'Task6_vc_dateform': Task6_vc_dateform,
                'Task7_vc_dateform': Task7_vc_dateform, 'Task8_vc_dateform': Task8_vc_dateform,
                'Task9_vc_dateform': Task9_vc_dateform, 'Task10_vc_dateform': Task10_vc_dateform,
                'Task11_vc_dateform': Task11_vc_dateform, 'Task12_vc_dateform': Task12_vc_dateform,
                'Task13_vc_dateform': Task13_vc_dateform, 'Task14_vc_dateform': Task14_vc_dateform,
                'Task15_vc_dateform': Task15_vc_dateform, 'Task16_vc_dateform': Task16_vc_dateform,
                'Task17_vc_dateform': Task17_vc_dateform, 'Task18_vc_dateform': Task18_vc_dateform,
                'Task19_vc_dateform': Task19_vc_dateform, 'Task20_vc_dateform': Task20_vc_dateform,
                'Task1_delta':Task1_delta, 'Task7_delta':Task7_delta, 'Task12_delta':Task12_delta, 'Task17_delta':Task17_delta,
                'Task2_delta': Task2_delta, 'Task8_delta': Task8_delta, 'Task13_delta': Task13_delta,
                'Task3_delta': Task3_delta, 'Task9_delta':Task9_delta, 'Task14_delta':Task14_delta, 'Task18_delta':Task18_delta,
                'Task4_delta':Task4_delta, 'Task10_delta':Task10_delta, 'Task15_delta':Task15_delta, 'Task19_delta':Task19_delta,
                'Task5_delta':Task5_delta, 'Task11_delta':Task11_delta, 'Task16_delta':Task16_delta, 'Task20_delta':Task20_delta,
                'Task6_delta':Task6_delta,
                }
        return render(request,self.template_name,args)

    def post(self, request, pk):

        form1 = Task1_vc_form(request.POST)
        form2 = Task2_vc_form(request.POST)
        form3 = Task3_vc_form(request.POST)
        form4 = Task4_vc_form(request.POST)
        form5 = Task5_vc_form(request.POST)
        form6 = Task6_vc_form(request.POST)
        form7 = Task7_vc_form(request.POST)
        form8 = Task8_vc_form(request.POST)
        form9 = Task9_vc_form(request.POST)
        form10 = Task10_vc_form(request.POST)
        form11 = Task11_vc_form(request.POST)
        form12 = Task12_vc_form(request.POST)
        form13 = Task13_vc_form(request.POST)
        form14 = Task14_vc_form(request.POST)
        form15 = Task15_vc_form(request.POST)
        form16 = Task16_vc_form(request.POST)
        form17 = Task17_vc_form(request.POST)
        form18 = Task18_vc_form(request.POST)
        form19 = Task19_vc_form(request.POST)
        form20 = Task20_vc_form(request.POST)
        devices = Device.objects.get(pk=pk)

        Task1_vc_dateform = Task1_vc_date_form(request.POST,instance=devices.VideoContent)
        Task2_vc_dateform = Task2_vc_date_form(request.POST,instance=devices.VideoContent)
        Task3_vc_dateform = Task3_vc_date_form(request.POST,instance=devices.VideoContent)
        Task4_vc_dateform = Task4_vc_date_form(request.POST,instance=devices.VideoContent)
        Task5_vc_dateform = Task5_vc_date_form(request.POST,instance=devices.VideoContent)
        Task6_vc_dateform = Task6_vc_date_form(request.POST,instance=devices.VideoContent)
        Task7_vc_dateform = Task7_vc_date_form(request.POST,instance=devices.VideoContent)
        Task8_vc_dateform = Task8_vc_date_form(request.POST,instance=devices.VideoContent)
        Task9_vc_dateform = Task9_vc_date_form(request.POST,instance=devices.VideoContent)
        Task10_vc_dateform = Task10_vc_date_form(request.POST,instance=devices.VideoContent)
        Task11_vc_dateform = Task11_vc_date_form(request.POST,instance=devices.VideoContent)
        Task12_vc_dateform = Task12_vc_date_form(request.POST,instance=devices.VideoContent)
        Task13_vc_dateform = Task13_vc_date_form(request.POST,instance=devices.VideoContent)
        Task14_vc_dateform = Task14_vc_date_form(request.POST,instance=devices.VideoContent)
        Task15_vc_dateform = Task15_vc_date_form(request.POST,instance=devices.VideoContent)
        Task16_vc_dateform = Task16_vc_date_form(request.POST,instance=devices.VideoContent)
        Task17_vc_dateform = Task17_vc_date_form(request.POST,instance=devices.VideoContent)
        Task18_vc_dateform = Task18_vc_date_form(request.POST,instance=devices.VideoContent)
        Task19_vc_dateform = Task19_vc_date_form(request.POST,instance=devices.VideoContent)
        Task20_vc_dateform = Task20_vc_date_form(request.POST,instance=devices.VideoContent)

        if 'Task1Submit' in request.POST:
            if form1.is_valid() and Task1_vc_dateform.is_valid():
                post = form1.save(commit=False)
                post.user = request.user
                post.VideoContent = devices.VideoContent
                Task1_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk + '/videocontent')
            else:
                return redirect('/login/summary/' + pk + '/videocontent')
        elif 'Task2Submit' in request.POST:
            if form2.is_valid() and Task2_vc_dateform.is_valid():
                post = form2.save(commit=False)
                post.user = request.user
                post.VideoContent = devices.VideoContent
                Task2_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/videocontent')
            else:
                return redirect('/login/summary/' + pk + '/videocontent')
        elif 'Task3Submit' in request.POST:
            if form3.is_valid() and Task3_vc_dateform.is_valid():
                post = form3.save(commit=False)
                post.user = request.user
                post.VideoContent = devices.VideoContent
                Task3_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/videocontent')
            else:
                return redirect('/login/summary/' + pk + '/videocontent')
        elif 'Task4Submit' in request.POST:
            if form4.is_valid() and Task4_vc_dateform.is_valid():
                post = form4.save(commit=False)
                post.user = request.user
                post.VideoContent = devices.VideoContent
                Task4_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/videocontent')
            else:
                return redirect('/login/summary/' + pk + '/videocontent')
        elif 'Task5Submit' in request.POST:
            if form5.is_valid() and Task5_vc_dateform.is_valid():
                post = form5.save(commit=False)
                post.user = request.user
                post.VideoContent = devices.VideoContent
                Task5_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/videocontent')
            else:
                return redirect('/login/summary/' + pk + '/videocontent')
        elif 'Task6Submit' in request.POST:
            if form6.is_valid() and Task6_vc_dateform.is_valid():
                post = form6.save(commit=False)
                post.user = request.user
                post.VideoContent = devices.VideoContent
                Task6_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/videocontent')
            else:
                return redirect('/login/summary/' + pk + '/videocontent')
        elif 'Task7Submit' in request.POST:
            if form7.is_valid() and Task7_vc_dateform.is_valid():
                post = form7.save(commit=False)
                post.user = request.user
                post.VideoContent = devices.VideoContent
                Task7_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/videocontent')
            else:
                return redirect('/login/summary/' + pk + '/videocontent')
        elif 'Task8Submit' in request.POST:
            if form8.is_valid() and Task8_vc_dateform.is_valid():
                post = form8.save(commit=False)
                post.user = request.user
                post.VideoContent = devices.VideoContent
                Task8_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/videocontent')
            else:
                return redirect('/login/summary/' + pk + '/videocontent')
        elif 'Task9Submit' in request.POST:
            if form9.is_valid() and Task9_vc_dateform.is_valid():
                post = form9.save(commit=False)
                post.user = request.user
                post.VideoContent = devices.VideoContent
                Task9_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/videocontent')
            else:
                return redirect('/login/summary/' + pk + '/videocontent')
        elif 'Task10Submit' in request.POST:
            if form10.is_valid() and Task10_vc_dateform.is_valid():
                post = form10.save(commit=False)
                post.user = request.user
                post.VideoContent = devices.VideoContent
                Task10_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/videocontent')
            else:
                return redirect('/login/summary/' + pk + '/videocontent')
        elif 'Task11Submit' in request.POST:
            if form11.is_valid() and Task11_vc_dateform.is_valid():
                post = form11.save(commit=False)
                post.user = request.user
                post.VideoContent = devices.VideoContent
                Task11_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/videocontent')
            else:
                return redirect('/login/summary/' + pk + '/videocontent')
        elif 'Task12Submit' in request.POST:
            if form12.is_valid() and Task12_vc_dateform.is_valid():
                post = form12.save(commit=False)
                post.user = request.user
                post.VideoContent = devices.VideoContent
                Task12_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/videocontent')
            else:
                return redirect('/login/summary/' + pk + '/videocontent')
        elif 'Task13Submit' in request.POST:
            if form13.is_valid() and Task13_vc_dateform.is_valid():
                post = form13.save(commit=False)
                post.user = request.user
                post.VideoContent = devices.VideoContent
                Task13_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/videocontent')
            else:
                return redirect('/login/summary/' + pk + '/videocontent')
        elif 'Task14Submit' in request.POST:
            if form14.is_valid() and Task14_vc_dateform.is_valid():
                post = form14.save(commit=False)
                post.user = request.user
                post.VideoContent = devices.VideoContent
                Task14_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/videocontent')
            else:
                return redirect('/login/summary/' + pk + '/videocontent')
        elif 'Task15Submit' in request.POST:
            if form15.is_valid() and Task15_vc_dateform.is_valid():
                post = form15.save(commit=False)
                post.user = request.user
                post.VideoContent = devices.VideoContent
                Task15_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/videocontent')
            else:
                return redirect('/login/summary/' + pk + '/videocontent')
        elif 'Task16Submit' in request.POST:
            if form16.is_valid() and Task16_vc_dateform.is_valid():
                post = form16.save(commit=False)
                post.user = request.user
                post.VideoContent = devices.VideoContent
                Task16_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/videocontent')
            else:
                return redirect('/login/summary/' + pk + '/videocontent')
        elif 'Task17Submit' in request.POST:
            if form17.is_valid() and Task17_vc_dateform.is_valid():
                post = form17.save(commit=False)
                post.user = request.user
                post.VideoContent = devices.VideoContent
                Task17_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/videocontent')
            else:
                return redirect('/login/summary/' + pk + '/videocontent')
        elif 'Task18Submit' in request.POST:
            if form18.is_valid() and Task18_vc_dateform.is_valid():
                post = form18.save(commit=False)
                post.user = request.user
                post.VideoContent = devices.VideoContent
                Task18_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/videocontent')
            else:
                return redirect('/login/summary/' + pk + '/videocontent')
        elif 'Task19Submit' in request.POST:
            if form19.is_valid() and Task19_vc_dateform.is_valid():
                post = form19.save(commit=False)
                post.user = request.user
                post.VideoContent = devices.VideoContent
                Task19_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/videocontent')
            else:
                return redirect('/login/summary/' + pk + '/videocontent')
        elif 'Task20Submit' in request.POST:
            if form20.is_valid() and Task20_vc_dateform.is_valid():
                post = form20.save(commit=False)
                post.user = request.user
                post.VideoContent = devices.VideoContent
                Task20_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/videocontent')
            else:
                return redirect('/login/summary/' + pk + '/videocontent')

########################################################################################################################

class CallCenterTrainingView(LoginRequiredMixin,TemplateView):
    template_name = 'login/device4.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        form1 = Task1_cct_form()
        form2 = Task2_cct_form()
        form3 = Task3_cct_form()
        form4 = Task4_cct_form()
        form5 = Task5_cct_form()
        form6 = Task6_cct_form()
        form7 = Task7_cct_form()
        form8 = Task8_cct_form()
        form9 = Task9_cct_form()
        form10 = Task10_cct_form()
        form11 = Task11_cct_form()
        form12 = Task12_cct_form()
        form13 = Task13_cct_form()
        form14 = Task14_cct_form()
        form15 = Task15_cct_form()
        form16 = Task16_cct_form()
        form17 = Task17_cct_form()
        form18 = Task18_cct_form()
        form19 = Task19_cct_form()
        form20 = Task20_cct_form()
        devices = Device.objects.get(pk=pk)
        Task1_vc_dateform = Task1_cct_date_form(instance=devices.CallCenterTraining)
        Task2_vc_dateform = Task2_cct_date_form(instance=devices.CallCenterTraining)
        Task3_vc_dateform = Task3_cct_date_form(instance=devices.CallCenterTraining)
        Task4_vc_dateform = Task4_cct_date_form(instance=devices.CallCenterTraining)
        Task5_vc_dateform = Task5_cct_date_form(instance=devices.CallCenterTraining)
        Task6_vc_dateform = Task6_cct_date_form(instance=devices.CallCenterTraining)
        Task7_vc_dateform = Task7_cct_date_form(instance=devices.CallCenterTraining)
        Task8_vc_dateform = Task8_cct_date_form(instance=devices.CallCenterTraining)
        Task9_vc_dateform = Task9_cct_date_form(instance=devices.CallCenterTraining)
        Task10_vc_dateform = Task10_cct_date_form(instance=devices.CallCenterTraining)
        Task11_vc_dateform = Task11_cct_date_form(instance=devices.CallCenterTraining)
        Task12_vc_dateform = Task12_cct_date_form(instance=devices.CallCenterTraining)
        Task13_vc_dateform = Task13_cct_date_form(instance=devices.CallCenterTraining)
        Task14_vc_dateform = Task14_cct_date_form(instance=devices.CallCenterTraining)
        Task15_vc_dateform = Task15_cct_date_form(instance=devices.CallCenterTraining)
        Task16_vc_dateform = Task16_cct_date_form(instance=devices.CallCenterTraining)
        Task17_vc_dateform = Task17_cct_date_form(instance=devices.CallCenterTraining)
        Task18_vc_dateform = Task18_cct_date_form(instance=devices.CallCenterTraining)
        Task19_vc_dateform = Task19_cct_date_form(instance=devices.CallCenterTraining)
        Task20_vc_dateform = Task20_cct_date_form(instance=devices.CallCenterTraining)

        #Calculating % completed
        y=0
        if devices.CallCenterTraining.Task1_Name:
            y=y+1
        if devices.CallCenterTraining.Task2_Name:
            y=y+1
        if devices.CallCenterTraining.Task3_Name:
            y=y+1
        if devices.CallCenterTraining.Task4_Name:
            y=y+1
        if devices.CallCenterTraining.Task5_Name:
            y=y+1
        if devices.CallCenterTraining.Task6_Name:
            y=y+1
        if devices.CallCenterTraining.Task7_Name:
            y=y+1
        if devices.CallCenterTraining.Task8_Name:
            y=y+1
        if devices.CallCenterTraining.Task9_Name:
            y=y+1
        if devices.CallCenterTraining.Task10_Name:
            y=y+1
        if devices.CallCenterTraining.Task11_Name:
            y=y+1
        if devices.CallCenterTraining.Task12_Name:
            y=y+1
        if devices.CallCenterTraining.Task13_Name:
            y=y+1
        if devices.CallCenterTraining.Task14_Name:
            y=y+1
        if devices.CallCenterTraining.Task15_Name:
            y=y+1
        if devices.CallCenterTraining.Task16_Name:
            y=y+1
        if devices.CallCenterTraining.Task17_Name:
            y=y+1
        if devices.CallCenterTraining.Task18_Name:
            y=y+1
        if devices.CallCenterTraining.Task19_Name:
            y=y+1
        if devices.CallCenterTraining.Task20_Name:
            y=y+1

        x = 0
        if devices.CallCenterTraining.Task1_complete_date:
            x =x+1
            devices.CallCenterTraining.Task1_alert = False
            devices.CallCenterTraining.Task1_warning=False
            devices.CallCenterTraining.Status='On_Time'
        if devices.CallCenterTraining.Task2_complete_date:
            x = x + 1
            devices.CallCenterTraining.Task2_alert = False
            devices.CallCenterTraining.Task2_warning=False
            devices.CallCenterTraining.Status = 'On_Time'
        if devices.CallCenterTraining.Task3_complete_date:
            x = x + 1
            devices.CallCenterTraining.Task3_alert = False
            devices.CallCenterTraining.Task3_warning=False
            devices.CallCenterTraining.Status = 'On_Time'
        if devices.CallCenterTraining.Task4_complete_date:
            x = x + 1
            devices.CallCenterTraining.Task4_alert = False
            devices.CallCenterTraining.Task4_warning=False
            devices.CallCenterTraining.Status = 'On_Time'
        if devices.CallCenterTraining.Task5_complete_date:
            x = x + 1
            devices.CallCenterTraining.Task5_alert = False
            devices.CallCenterTraining.Task5_warning=False
            devices.CallCenterTraining.Status = 'On_Time'
        if devices.CallCenterTraining.Task6_complete_date:
            x = x + 1
            devices.CallCenterTraining.Task6_alert = False
            devices.CallCenterTraining.Task6_warning=False
            devices.CallCenterTraining.Status = 'On_Time'
        if devices.CallCenterTraining.Task7_complete_date:
            x =x+1
            devices.CallCenterTraining.Task7_alert = False
            devices.CallCenterTraining.Task7_warning=False
            devices.CallCenterTraining.Status = 'On_Time'
        if devices.CallCenterTraining.Task8_complete_date:
            x =x+1
            devices.CallCenterTraining.Task8_alert = False
            devices.CallCenterTraining.Task8_warning=False
            devices.CallCenterTraining.Status = 'On_Time'
        if devices.CallCenterTraining.Task9_complete_date:
            x =x+1
            devices.CallCenterTraining.Task9_alert = False
            devices.CallCenterTraining.Task9_warning=False
            devices.CallCenterTraining.Status = 'On_Time'
        if devices.CallCenterTraining.Task10_complete_date:
            x =x+1
            devices.CallCenterTraining.Task10_alert = False
            devices.CallCenterTraining.Task10_warning=False
            devices.CallCenterTraining.Status = 'On_Time'
        if devices.CallCenterTraining.Task11_complete_date:
            x =x+1
            devices.CallCenterTraining.Task11_alert = False
            devices.CallCenterTraining.Task11_warning=False
            devices.CallCenterTraining.Status = 'On_Time'
        if devices.CallCenterTraining.Task12_complete_date:
            x = x + 1
            devices.CallCenterTraining.Task12_alert = False
            devices.CallCenterTraining.Task12_warning=False
            devices.CallCenterTraining.Status = 'On_Time'
        if devices.CallCenterTraining.Task13_complete_date:
            x = x + 1
            devices.CallCenterTraining.Task13_alert = False
            devices.CallCenterTraining.Task13_warning=False
            devices.CallCenterTraining.Status = 'On_Time'
        if devices.CallCenterTraining.Task14_complete_date:
            x = x + 1
            devices.CallCenterTraining.Task14_alert = False
            devices.CallCenterTraining.Task14_warning=False
            devices.CallCenterTraining.Status = 'On_Time'
        if devices.CallCenterTraining.Task15_complete_date:
            x = x + 1
            devices.CallCenterTraining.Task15_alert = False
            devices.CallCenterTraining.Task15_warning=False
            devices.CallCenterTraining.Status = 'On_Time'
        if devices.CallCenterTraining.Task16_complete_date:
            x = x + 1
            devices.CallCenterTraining.Task16_alert = False
            devices.CallCenterTraining.Task16_warning=False
            devices.CallCenterTraining.Status = 'On_Time'
        if devices.CallCenterTraining.Task17_complete_date:
            x =x+1
            devices.CallCenterTraining.Task17_alert = False
            devices.CallCenterTraining.Task17_warning=False
            devices.CallCenterTraining.Status = 'On_Time'
        if devices.CallCenterTraining.Task18_complete_date:
            x =x+1
            devices.CallCenterTraining.Task18_alert = False
            devices.CallCenterTraining.Task18_warning=False
            devices.CallCenterTraining.Status = 'On_Time'
        if devices.CallCenterTraining.Task19_complete_date:
            x =x+1
            devices.CallCenterTraining.Task19_alert = False
            devices.CallCenterTraining.Task19_warning=False
            devices.CallCenterTraining.Status = 'On_Time'
        if devices.CallCenterTraining.Task20_complete_date:
            x =x+1
            devices.CallCenterTraining.Task20_alert = False
            devices.CallCenterTraining.Task20_warning=False
            devices.CallCenterTraining.Status = 'On_Time'
        percent = x/y * 100
        print (percent)

        #alerting logic
        today = datetime.date.today()
        if devices.CallCenterTraining.Task1_End_Date:
            Task1_delta =  devices.CallCenterTraining.Task1_End_Date - today
        else:
            Task1_delta = None
        if devices.CallCenterTraining.Task2_End_Date:
            Task2_delta = devices.CallCenterTraining.Task2_End_Date - today
        else:
            Task2_delta = None
        if devices.CallCenterTraining.Task3_End_Date:
            Task3_delta = devices.CallCenterTraining.Task3_End_Date - today
        else:
            Task3_delta = None
        if devices.CallCenterTraining.Task4_End_Date:
            Task4_delta = devices.CallCenterTraining.Task4_End_Date - today
        else:
            Task4_delta = None
        if devices.CallCenterTraining.Task5_End_Date:
            Task5_delta = devices.CallCenterTraining.Task5_End_Date - today
        else:
            Task5_delta = None
        if devices.CallCenterTraining.Task6_End_Date:
            Task6_delta = devices.CallCenterTraining.Task6_End_Date - today
        else:
            Task6_delta = None
        if devices.CallCenterTraining.Task7_End_Date:
            Task7_delta = devices.CallCenterTraining.Task7_End_Date - today
        else:
            Task7_delta = None
        if devices.CallCenterTraining.Task8_End_Date:
            Task8_delta = devices.CallCenterTraining.Task8_End_Date - today
        else:
            Task8_delta = None
        if devices.CallCenterTraining.Task9_End_Date:
            Task9_delta = devices.CallCenterTraining.Task9_End_Date - today
        else:
            Task9_delta = None
        if devices.CallCenterTraining.Task10_End_Date:
            Task10_delta =  devices.CallCenterTraining.Task10_End_Date - today
        else:
            Task10_delta = None
        if devices.CallCenterTraining.Task11_End_Date:
            Task11_delta =  devices.CallCenterTraining.Task11_End_Date - today
        else:
            Task11_delta = None
        if devices.CallCenterTraining.Task12_End_Date:
            Task12_delta = devices.CallCenterTraining.Task12_End_Date - today
        else:
            Task12_delta = None
        if devices.CallCenterTraining.Task13_End_Date:
            Task13_delta = devices.CallCenterTraining.Task13_End_Date - today
        else:
            Task13_delta = None
        if devices.CallCenterTraining.Task14_End_Date:
            Task14_delta = devices.CallCenterTraining.Task14_End_Date - today
        else:
            Task14_delta = None
        if devices.CallCenterTraining.Task15_End_Date:
            Task15_delta = devices.CallCenterTraining.Task15_End_Date - today
        else:
            Task15_delta = None
        if devices.CallCenterTraining.Task16_End_Date:
            Task16_delta = devices.CallCenterTraining.Task16_End_Date - today
        else:
            Task16_delta = None
        if devices.CallCenterTraining.Task17_End_Date:
            Task17_delta = devices.CallCenterTraining.Task17_End_Date - today
        else:
            Task17_delta = None
        if devices.CallCenterTraining.Task18_End_Date:
            Task18_delta = devices.CallCenterTraining.Task18_End_Date - today
        else:
            Task18_delta = None
        if devices.CallCenterTraining.Task19_End_Date:
            Task19_delta = devices.CallCenterTraining.Task19_End_Date - today
        else:
            Task19_delta = None
        if devices.CallCenterTraining.Task20_End_Date:
            Task20_delta = devices.CallCenterTraining.Task20_End_Date - today
        else:
            Task20_delta = None


        if Task1_delta and Task1_delta < timedelta(devices.CallCenterTraining.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not devices.CallCenterTraining.Task1_complete_date:
            devices.CallCenterTraining.Task1_warning = True
            devices.CallCenterTraining.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(devices.CallCenterTraining.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not devices.CallCenterTraining.Task2_complete_date:
            devices.CallCenterTraining.Task2_warning = True
            devices.CallCenterTraining.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(devices.CallCenterTraining.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not devices.CallCenterTraining.Task3_complete_date:
            devices.CallCenterTraining.Task3_warning = True
            devices.CallCenterTraining.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(devices.CallCenterTraining.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not devices.CallCenterTraining.Task4_complete_date:
            devices.CallCenterTraining.Task4_warning = True
            devices.CallCenterTraining.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(devices.CallCenterTraining.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not devices.CallCenterTraining.Task5_complete_date:
            devices.CallCenterTraining.Task5_warning = True
            devices.CallCenterTraining.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(devices.CallCenterTraining.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not devices.CallCenterTraining.Task6_complete_date:
            devices.CallCenterTraining.Task6_warning = True
            devices.CallCenterTraining.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(devices.CallCenterTraining.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not devices.CallCenterTraining.Task7_complete_date:
            devices.CallCenterTraining.Task7_warning = True
            devices.CallCenterTraining.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(devices.CallCenterTraining.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not devices.CallCenterTraining.Task8_complete_date:
            devices.CallCenterTraining.Task8_warning = True
            devices.CallCenterTraining.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(devices.CallCenterTraining.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not devices.CallCenterTraining.Task9_complete_date:
            devices.CallCenterTraining.Task9_warning = True
            devices.CallCenterTraining.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(devices.CallCenterTraining.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not devices.CallCenterTraining.Task10_complete_date:
            devices.CallCenterTraining.Task10_warning = True
            devices.CallCenterTraining.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(devices.CallCenterTraining.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not devices.CallCenterTraining.Task11_complete_date:
            devices.CallCenterTraining.Task11_warning = True
            devices.CallCenterTraining.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(devices.CallCenterTraining.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not devices.CallCenterTraining.Task12_complete_date:
            devices.CallCenterTraining.Task12_warning = True
            devices.CallCenterTraining.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(devices.CallCenterTraining.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not devices.CallCenterTraining.Task13_complete_date:
            devices.CallCenterTraining.Task13_warning = True
            devices.CallCenterTraining.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(devices.CallCenterTraining.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not devices.CallCenterTraining.Task14_complete_date:
            devices.CallCenterTraining.Task14_warning = True
            devices.CallCenterTraining.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(devices.CallCenterTraining.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not devices.CallCenterTraining.Task15_complete_date:
            devices.CallCenterTraining.Task15_warning = True
            devices.CallCenterTraining.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(devices.CallCenterTraining.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not devices.CallCenterTraining.Task16_complete_date:
            devices.CallCenterTraining.Task16_warning = True
            devices.CallCenterTraining.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(devices.CallCenterTraining.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not devices.CallCenterTraining.Task17_complete_date:
            devices.CallCenterTraining.Task17_warning = True
            devices.CallCenterTraining.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(devices.CallCenterTraining.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not devices.CallCenterTraining.Task18_complete_date:
            devices.CallCenterTraining.Task18_warning = True
            devices.CallCenterTraining.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(devices.CallCenterTraining.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not devices.CallCenterTraining.Task19_complete_date:
            devices.CallCenterTraining.Task19_warning = True
            devices.CallCenterTraining.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(devices.CallCenterTraining.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not devices.CallCenterTraining.Task20_complete_date:
            devices.CallCenterTraining.Task20_warning = True
            devices.CallCenterTraining.Status = 'At Risk'

        if devices.CallCenterTraining.Task1_End_Date and Task1_delta < timedelta(0) and not devices.CallCenterTraining.Task1_complete_date:
            devices.CallCenterTraining.Task1_alert = True
            devices.CallCenterTraining.Status = 'Delayed'
        if devices.CallCenterTraining.Task2_End_Date and Task2_delta < timedelta(0) and not devices.CallCenterTraining.Task2_complete_date:
            devices.CallCenterTraining.Task2_alert = True
            devices.CallCenterTraining.Status = 'Delayed'
        if devices.CallCenterTraining.Task3_End_Date and Task3_delta < timedelta(0) and not devices.CallCenterTraining.Task3_complete_date:
            devices.CallCenterTraining.Task3_alert = True
            devices.CallCenterTraining.Status = 'Delayed'
        if devices.CallCenterTraining.Task4_End_Date and Task4_delta < timedelta(0) and not devices.CallCenterTraining.Task4_complete_date:
            devices.CallCenterTraining.Task4_alert = True
            devices.CallCenterTraining.Status = 'Delayed'
        if devices.CallCenterTraining.Task5_End_Date and Task5_delta < timedelta(0) and not devices.CallCenterTraining.Task5_complete_date:
            devices.CallCenterTraining.Task5_alert = True
            devices.CallCenterTraining.Status = 'Delayed'
        if devices.CallCenterTraining.Task6_End_Date and Task6_delta < timedelta(0) and not devices.CallCenterTraining.Task6_complete_date:
            devices.CallCenterTraining.Task6_alert = True
            devices.CallCenterTraining.Status = 'Delayed'
        if devices.CallCenterTraining.Task7_End_Date and Task7_delta < timedelta(0) and not devices.CallCenterTraining.Task7_complete_date:
            devices.CallCenterTraining.Task7_alert = True
            devices.CallCenterTraining.Status = 'Delayed'
        if devices.CallCenterTraining.Task8_End_Date and Task8_delta < timedelta(0)and not devices.CallCenterTraining.Task8_complete_date:
            devices.CallCenterTraining.Task8_alert = True
            devices.CallCenterTraining.Status = 'Delayed'
        if devices.CallCenterTraining.Task9_End_Date and Task9_delta < timedelta(0)and not devices.CallCenterTraining.Task9_complete_date:
            devices.CallCenterTraining.Task9_alert = True
            devices.CallCenterTraining.Status = 'Delayed'
        if devices.CallCenterTraining.Task10_End_Date and Task10_delta < timedelta(0) and not devices.CallCenterTraining.Task10_complete_date:
            devices.CallCenterTraining.Task10_alert = True
            devices.CallCenterTraining.Status = 'Delayed'
        if devices.CallCenterTraining.Task11_End_Date and Task11_delta < timedelta(0) and not devices.CallCenterTraining.Task11_complete_date:
            devices.CallCenterTraining.Task11_alert = True
            devices.CallCenterTraining.Status = 'Delayed'
        if devices.CallCenterTraining.Task12_End_Date and Task12_delta < timedelta(0) and not devices.CallCenterTraining.Task12_complete_date:
            devices.CallCenterTraining.Task12_alert = True
            devices.CallCenterTraining.Status = 'Delayed'
        if devices.CallCenterTraining.Task13_End_Date and Task13_delta < timedelta(0) and not devices.CallCenterTraining.Task13_complete_date:
            devices.CallCenterTraining.Task13_alert = True
            devices.CallCenterTraining.Status = 'Delayed'
        if devices.CallCenterTraining.Task14_End_Date and Task14_delta < timedelta(0) and not devices.CallCenterTraining.Task14_complete_date:
            devices.CallCenterTraining.Task14_alert = True
            devices.CallCenterTraining.Status = 'Delayed'
        if devices.CallCenterTraining.Task15_End_Date and Task15_delta < timedelta(0) and not devices.CallCenterTraining.Task15_complete_date:
            devices.CallCenterTraining.Task15_alert = True
            devices.CallCenterTraining.Status = 'Delayed'
        if devices.CallCenterTraining.Task16_End_Date and Task16_delta < timedelta(0) and not devices.CallCenterTraining.Task16_complete_date:
            devices.CallCenterTraining.Task16_alert = True
            devices.CallCenterTraining.Status = 'Delayed'
        if devices.CallCenterTraining.Task17_End_Date and Task17_delta < timedelta(0)and not devices.CallCenterTraining.Task17_complete_date:
            devices.CallCenterTraining.Task17_alert = True
            devices.CallCenterTraining.Status = 'Delayed'
        if devices.CallCenterTraining.Task18_End_Date and Task18_delta < timedelta(0)and not devices.CallCenterTraining.Task18_complete_date:
            devices.CallCenterTraining.Task18_alert = True
            devices.CallCenterTraining.Status = 'Delayed'
        if devices.CallCenterTraining.Task19_End_Date and Task19_delta < timedelta(0)and not devices.CallCenterTraining.Task19_complete_date:
            devices.CallCenterTraining.Task19_alert = True
            devices.CallCenterTraining.Status = 'Delayed'
        if devices.CallCenterTraining.Task20_End_Date and Task20_delta < timedelta(0)and not devices.CallCenterTraining.Task20_complete_date:
            devices.CallCenterTraining.Task20_alert = True
            devices.CallCenterTraining.Status = 'Delayed'


        devices.CallCenterTraining.completed = int(percent)
        devices.CallCenterTraining.save()
        posts1 = devices.CallCenterTraining.task1statuscallcentertraining_set.all().order_by('-created')
        posts2 = devices.CallCenterTraining.task2statuscallcentertraining_set.all().order_by('-created')
        posts3 = devices.CallCenterTraining.task3statuscallcentertraining_set.all().order_by('-created')
        posts4 = devices.CallCenterTraining.task4statuscallcentertraining_set.all().order_by('-created')
        posts5 = devices.CallCenterTraining.task5statuscallcentertraining_set.all().order_by('-created')
        posts6 = devices.CallCenterTraining.task6statuscallcentertraining_set.all().order_by('-created')
        posts7 = devices.CallCenterTraining.task7statuscallcentertraining_set.all().order_by('-created')
        posts8 = devices.CallCenterTraining.task8statuscallcentertraining_set.all().order_by('-created')
        posts9 = devices.CallCenterTraining.task9statuscallcentertraining_set.all().order_by('-created')
        posts10 = devices.CallCenterTraining.task10statuscallcentertraining_set.all().order_by('-created')
        posts11 = devices.CallCenterTraining.task11statuscallcentertraining_set.all().order_by('-created')
        posts12 = devices.CallCenterTraining.task12statuscallcentertraining_set.all().order_by('-created')
        posts13 = devices.CallCenterTraining.task13statuscallcentertraining_set.all().order_by('-created')
        posts14 = devices.CallCenterTraining.task14statuscallcentertraining_set.all().order_by('-created')
        posts15 = devices.CallCenterTraining.task15statuscallcentertraining_set.all().order_by('-created')
        posts16 = devices.CallCenterTraining.task16statuscallcentertraining_set.all().order_by('-created')
        posts17 = devices.CallCenterTraining.task17statuscallcentertraining_set.all().order_by('-created')
        posts18 = devices.CallCenterTraining.task18statuscallcentertraining_set.all().order_by('-created')
        posts19 = devices.CallCenterTraining.task19statuscallcentertraining_set.all().order_by('-created')
        posts20 = devices.CallCenterTraining.task20statuscallcentertraining_set.all().order_by('-created')

        args = {'devices':devices, 'form1':form1, 'form2':form2, 'form3':form3, 'form4':form4, 'form5':form5, 'form6':form6,
                'form7': form7, 'form8':form8, 'form9':form9, 'form10':form10, 'form11':form11, 'form12':form12, 'form13':form13,
                'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17, 'form18': form18, 'form19': form19,
                'form20': form20, 'posts1':posts1, 'posts2':posts2, 'posts3':posts3, 'posts4':posts4, 'posts5':posts5, 'posts6':posts6,
                'posts7': posts7, 'posts8':posts8, 'posts9':posts9, 'posts10':posts10, 'posts11':posts11, 'posts12':posts12, 'posts13':posts13,
                'posts14': posts14, 'posts15': posts15, 'posts16': posts16, 'posts17': posts17, 'posts18': posts18, 'posts19': posts19,
                'posts20': posts20, 'Task1_vc_dateform':Task1_vc_dateform, 'Task2_vc_dateform':Task2_vc_dateform,
                'Task3_vc_dateform':Task3_vc_dateform, 'Task4_vc_dateform':Task4_vc_dateform,
                'Task5_vc_dateform': Task5_vc_dateform, 'Task6_vc_dateform': Task6_vc_dateform,
                'Task7_vc_dateform': Task7_vc_dateform, 'Task8_vc_dateform': Task8_vc_dateform,
                'Task9_vc_dateform': Task9_vc_dateform, 'Task10_vc_dateform': Task10_vc_dateform,
                'Task11_vc_dateform': Task11_vc_dateform, 'Task12_vc_dateform': Task12_vc_dateform,
                'Task13_vc_dateform': Task13_vc_dateform, 'Task14_vc_dateform': Task14_vc_dateform,
                'Task15_vc_dateform': Task15_vc_dateform, 'Task16_vc_dateform': Task16_vc_dateform,
                'Task17_vc_dateform': Task17_vc_dateform, 'Task18_vc_dateform': Task18_vc_dateform,
                'Task19_vc_dateform': Task19_vc_dateform, 'Task20_vc_dateform': Task20_vc_dateform,
                'Task1_delta':Task1_delta, 'Task7_delta':Task7_delta, 'Task12_delta':Task12_delta, 'Task17_delta':Task17_delta,
                'Task2_delta': Task2_delta, 'Task8_delta': Task8_delta, 'Task13_delta': Task13_delta,
                'Task3_delta': Task3_delta, 'Task9_delta':Task9_delta, 'Task14_delta':Task14_delta, 'Task18_delta':Task18_delta,
                'Task4_delta':Task4_delta, 'Task10_delta':Task10_delta, 'Task15_delta':Task15_delta, 'Task19_delta':Task19_delta,
                'Task5_delta':Task5_delta, 'Task11_delta':Task11_delta, 'Task16_delta':Task16_delta, 'Task20_delta':Task20_delta,
                'Task6_delta':Task6_delta,
                }
        return render(request,self.template_name,args)

    def post(self, request, pk):

        form1 = Task1_cct_form(request.POST)
        form2 = Task2_cct_form(request.POST)
        form3 = Task3_cct_form(request.POST)
        form4 = Task4_cct_form(request.POST)
        form5 = Task5_cct_form(request.POST)
        form6 = Task6_cct_form(request.POST)
        form7 = Task7_cct_form(request.POST)
        form8 = Task8_cct_form(request.POST)
        form9 = Task9_cct_form(request.POST)
        form10 = Task10_cct_form(request.POST)
        form11 = Task11_cct_form(request.POST)
        form12 = Task12_cct_form(request.POST)
        form13 = Task13_cct_form(request.POST)
        form14 = Task14_cct_form(request.POST)
        form15 = Task15_cct_form(request.POST)
        form16 = Task16_cct_form(request.POST)
        form17 = Task17_cct_form(request.POST)
        form18 = Task18_cct_form(request.POST)
        form19 = Task19_cct_form(request.POST)
        form20 = Task20_cct_form(request.POST)
        devices = Device.objects.get(pk=pk)

        Task1_vc_dateform = Task1_cct_date_form(request.POST,instance=devices.CallCenterTraining)
        Task2_vc_dateform = Task2_cct_date_form(request.POST,instance=devices.CallCenterTraining)
        Task3_vc_dateform = Task3_cct_date_form(request.POST,instance=devices.CallCenterTraining)
        Task4_vc_dateform = Task4_cct_date_form(request.POST,instance=devices.CallCenterTraining)
        Task5_vc_dateform = Task5_cct_date_form(request.POST,instance=devices.CallCenterTraining)
        Task6_vc_dateform = Task6_cct_date_form(request.POST,instance=devices.CallCenterTraining)
        Task7_vc_dateform = Task7_cct_date_form(request.POST,instance=devices.CallCenterTraining)
        Task8_vc_dateform = Task8_cct_date_form(request.POST,instance=devices.CallCenterTraining)
        Task9_vc_dateform = Task9_cct_date_form(request.POST,instance=devices.CallCenterTraining)
        Task10_vc_dateform = Task10_cct_date_form(request.POST,instance=devices.CallCenterTraining)
        Task11_vc_dateform = Task11_cct_date_form(request.POST,instance=devices.CallCenterTraining)
        Task12_vc_dateform = Task12_cct_date_form(request.POST,instance=devices.CallCenterTraining)
        Task13_vc_dateform = Task13_cct_date_form(request.POST,instance=devices.CallCenterTraining)
        Task14_vc_dateform = Task14_cct_date_form(request.POST,instance=devices.CallCenterTraining)
        Task15_vc_dateform = Task15_cct_date_form(request.POST,instance=devices.CallCenterTraining)
        Task16_vc_dateform = Task16_cct_date_form(request.POST,instance=devices.CallCenterTraining)
        Task17_vc_dateform = Task17_cct_date_form(request.POST,instance=devices.CallCenterTraining)
        Task18_vc_dateform = Task18_cct_date_form(request.POST,instance=devices.CallCenterTraining)
        Task19_vc_dateform = Task19_cct_date_form(request.POST,instance=devices.CallCenterTraining)
        Task20_vc_dateform = Task20_cct_date_form(request.POST,instance=devices.CallCenterTraining)

        if 'Task1Submit' in request.POST:
            if form1.is_valid() and Task1_vc_dateform.is_valid():
                post = form1.save(commit=False)
                post.user = request.user
                post.CallCenterTraining = devices.CallCenterTraining
                Task1_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk + '/callcentertraining')
            else:
                return redirect('/login/summary/' + pk + '/callcentertraining')
        elif 'Task2Submit' in request.POST:
            if form2.is_valid() and Task2_vc_dateform.is_valid():
                post = form2.save(commit=False)
                post.user = request.user
                post.CallCenterTraining = devices.CallCenterTraining
                Task2_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcentertraining')
            else:
                return redirect('/login/summary/' + pk + '/callcentertraining')
        elif 'Task3Submit' in request.POST:
            if form3.is_valid() and Task3_vc_dateform.is_valid():
                post = form3.save(commit=False)
                post.user = request.user
                post.CallCenterTraining = devices.CallCenterTraining
                Task3_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcentertraining')
            else:
                return redirect('/login/summary/' + pk + '/callcentertraining')
        elif 'Task4Submit' in request.POST:
            if form4.is_valid() and Task4_vc_dateform.is_valid():
                post = form4.save(commit=False)
                post.user = request.user
                post.CallCenterTraining = devices.CallCenterTraining
                Task4_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcentertraining')
            else:
                return redirect('/login/summary/' + pk + '/callcentertraining')
        elif 'Task5Submit' in request.POST:
            if form5.is_valid() and Task5_vc_dateform.is_valid():
                post = form5.save(commit=False)
                post.user = request.user
                post.CallCenterTraining = devices.CallCenterTraining
                Task5_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcentertraining')
            else:
                return redirect('/login/summary/' + pk + '/callcentertraining')
        elif 'Task6Submit' in request.POST:
            if form6.is_valid() and Task6_vc_dateform.is_valid():
                post = form6.save(commit=False)
                post.user = request.user
                post.CallCenterTraining = devices.CallCenterTraining
                Task6_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcentertraining')
            else:
                return redirect('/login/summary/' + pk + '/callcentertraining')
        elif 'Task7Submit' in request.POST:
            if form7.is_valid() and Task7_vc_dateform.is_valid():
                post = form7.save(commit=False)
                post.user = request.user
                post.CallCenterTraining = devices.CallCenterTraining
                Task7_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcentertraining')
            else:
                return redirect('/login/summary/' + pk + '/callcentertraining')
        elif 'Task8Submit' in request.POST:
            if form8.is_valid() and Task8_vc_dateform.is_valid():
                post = form8.save(commit=False)
                post.user = request.user
                post.CallCenterTraining = devices.CallCenterTraining
                Task8_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcentertraining')
            else:
                return redirect('/login/summary/' + pk + '/callcentertraining')
        elif 'Task9Submit' in request.POST:
            if form9.is_valid() and Task9_vc_dateform.is_valid():
                post = form9.save(commit=False)
                post.user = request.user
                post.CallCenterTraining = devices.CallCenterTraining
                Task9_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcentertraining')
            else:
                return redirect('/login/summary/' + pk + '/callcentertraining')
        elif 'Task10Submit' in request.POST:
            if form10.is_valid() and Task10_vc_dateform.is_valid():
                post = form10.save(commit=False)
                post.user = request.user
                post.CallCenterTraining = devices.CallCenterTraining
                Task10_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcentertraining')
            else:
                return redirect('/login/summary/' + pk + '/callcentertraining')
        elif 'Task11Submit' in request.POST:
            if form11.is_valid() and Task11_vc_dateform.is_valid():
                post = form11.save(commit=False)
                post.user = request.user
                post.CallCenterTraining = devices.CallCenterTraining
                Task11_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcentertraining')
            else:
                return redirect('/login/summary/' + pk + '/callcentertraining')
        elif 'Task12Submit' in request.POST:
            if form12.is_valid() and Task12_vc_dateform.is_valid():
                post = form12.save(commit=False)
                post.user = request.user
                post.CallCenterTraining = devices.CallCenterTraining
                Task12_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcentertraining')
            else:
                return redirect('/login/summary/' + pk + '/callcentertraining')
        elif 'Task13Submit' in request.POST:
            if form13.is_valid() and Task13_vc_dateform.is_valid():
                post = form13.save(commit=False)
                post.user = request.user
                post.CallCenterTraining = devices.CallCenterTraining
                Task13_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcentertraining')
            else:
                return redirect('/login/summary/' + pk + '/callcentertraining')
        elif 'Task14Submit' in request.POST:
            if form14.is_valid() and Task14_vc_dateform.is_valid():
                post = form14.save(commit=False)
                post.user = request.user
                post.CallCenterTraining = devices.CallCenterTraining
                Task14_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcentertraining')
            else:
                return redirect('/login/summary/' + pk + '/callcentertraining')
        elif 'Task15Submit' in request.POST:
            if form15.is_valid() and Task15_vc_dateform.is_valid():
                post = form15.save(commit=False)
                post.user = request.user
                post.CallCenterTraining = devices.CallCenterTraining
                Task15_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcentertraining')
            else:
                return redirect('/login/summary/' + pk + '/callcentertraining')
        elif 'Task16Submit' in request.POST:
            if form16.is_valid() and Task16_vc_dateform.is_valid():
                post = form16.save(commit=False)
                post.user = request.user
                post.CallCenterTraining = devices.CallCenterTraining
                Task16_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcentertraining')
            else:
                return redirect('/login/summary/' + pk + '/callcentertraining')
        elif 'Task17Submit' in request.POST:
            if form17.is_valid() and Task17_vc_dateform.is_valid():
                post = form17.save(commit=False)
                post.user = request.user
                post.CallCenterTraining = devices.CallCenterTraining
                Task17_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcentertraining')
            else:
                return redirect('/login/summary/' + pk + '/callcentertraining')
        elif 'Task18Submit' in request.POST:
            if form18.is_valid() and Task18_vc_dateform.is_valid():
                post = form18.save(commit=False)
                post.user = request.user
                post.CallCenterTraining = devices.CallCenterTraining
                Task18_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcentertraining')
            else:
                return redirect('/login/summary/' + pk + '/callcentertraining')
        elif 'Task19Submit' in request.POST:
            if form19.is_valid() and Task19_vc_dateform.is_valid():
                post = form19.save(commit=False)
                post.user = request.user
                post.CallCenterTraining = devices.CallCenterTraining
                Task19_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcentertraining')
            else:
                return redirect('/login/summary/' + pk + '/callcentertraining')
        elif 'Task20Submit' in request.POST:
            if form20.is_valid() and Task20_vc_dateform.is_valid():
                post = form20.save(commit=False)
                post.user = request.user
                post.CallCenterTraining = devices.CallCenterTraining
                Task20_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcentertraining')
            else:
                return redirect('/login/summary/' + pk + '/callcentertraining')

########################################################################################################################

class DigitalContentView(LoginRequiredMixin,TemplateView):
    template_name = 'login/device3.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        form1 = Task1_dc_form()
        form2 = Task2_dc_form()
        form3 = Task3_dc_form()
        form4 = Task4_dc_form()
        form5 = Task5_dc_form()
        form6 = Task6_dc_form()
        form7 = Task7_dc_form()
        form8 = Task8_dc_form()
        form9 = Task9_dc_form()
        form10 = Task10_dc_form()
        form11 = Task11_dc_form()
        form12 = Task12_dc_form()
        form13 = Task13_dc_form()
        form14 = Task14_dc_form()
        form15 = Task15_dc_form()
        form16 = Task16_dc_form()
        form17 = Task17_dc_form()
        form18 = Task18_dc_form()
        form19 = Task19_dc_form()
        form20 = Task20_dc_form()
        devices = Device.objects.get(pk=pk)
        Task1_vc_dateform = Task1_dc_date_form(instance=devices.DigitalContent)
        Task2_vc_dateform = Task2_dc_date_form(instance=devices.DigitalContent)
        Task3_vc_dateform = Task3_dc_date_form(instance=devices.DigitalContent)
        Task4_vc_dateform = Task4_dc_date_form(instance=devices.DigitalContent)
        Task5_vc_dateform = Task5_dc_date_form(instance=devices.DigitalContent)
        Task6_vc_dateform = Task6_dc_date_form(instance=devices.DigitalContent)
        Task7_vc_dateform = Task7_dc_date_form(instance=devices.DigitalContent)
        Task8_vc_dateform = Task8_dc_date_form(instance=devices.DigitalContent)
        Task9_vc_dateform = Task9_dc_date_form(instance=devices.DigitalContent)
        Task10_vc_dateform = Task10_dc_date_form(instance=devices.DigitalContent)
        Task11_vc_dateform = Task11_dc_date_form(instance=devices.DigitalContent)
        Task12_vc_dateform = Task12_dc_date_form(instance=devices.DigitalContent)
        Task13_vc_dateform = Task13_dc_date_form(instance=devices.DigitalContent)
        Task14_vc_dateform = Task14_dc_date_form(instance=devices.DigitalContent)
        Task15_vc_dateform = Task15_dc_date_form(instance=devices.DigitalContent)
        Task16_vc_dateform = Task16_dc_date_form(instance=devices.DigitalContent)
        Task17_vc_dateform = Task17_dc_date_form(instance=devices.DigitalContent)
        Task18_vc_dateform = Task18_dc_date_form(instance=devices.DigitalContent)
        Task19_vc_dateform = Task19_dc_date_form(instance=devices.DigitalContent)
        Task20_vc_dateform = Task20_dc_date_form(instance=devices.DigitalContent)

        #Calculating % completed
        y=0
        if devices.DigitalContent.Task1_Name:
            y=y+1
        if devices.DigitalContent.Task2_Name:
            y=y+1
        if devices.DigitalContent.Task3_Name:
            y=y+1
        if devices.DigitalContent.Task4_Name:
            y=y+1
        if devices.DigitalContent.Task5_Name:
            y=y+1
        if devices.DigitalContent.Task6_Name:
            y=y+1
        if devices.DigitalContent.Task7_Name:
            y=y+1
        if devices.DigitalContent.Task8_Name:
            y=y+1
        if devices.DigitalContent.Task9_Name:
            y=y+1
        if devices.DigitalContent.Task10_Name:
            y=y+1
        if devices.DigitalContent.Task11_Name:
            y=y+1
        if devices.DigitalContent.Task12_Name:
            y=y+1
        if devices.DigitalContent.Task13_Name:
            y=y+1
        if devices.DigitalContent.Task14_Name:
            y=y+1
        if devices.DigitalContent.Task15_Name:
            y=y+1
        if devices.DigitalContent.Task16_Name:
            y=y+1
        if devices.DigitalContent.Task17_Name:
            y=y+1
        if devices.DigitalContent.Task18_Name:
            y=y+1
        if devices.DigitalContent.Task19_Name:
            y=y+1
        if devices.DigitalContent.Task20_Name:
            y=y+1

        x = 0
        if devices.DigitalContent.Task1_complete_date:
            x =x+1
            devices.DigitalContent.Task1_alert = False
            devices.DigitalContent.Task1_warning=False
            devices.DigitalContent.Status='On_Time'
        if devices.DigitalContent.Task2_complete_date:
            x = x + 1
            devices.DigitalContent.Task2_alert = False
            devices.DigitalContent.Task2_warning=False
            devices.DigitalContent.Status = 'On_Time'
        if devices.DigitalContent.Task3_complete_date:
            x = x + 1
            devices.DigitalContent.Task3_alert = False
            devices.DigitalContent.Task3_warning=False
            devices.DigitalContent.Status = 'On_Time'
        if devices.DigitalContent.Task4_complete_date:
            x = x + 1
            devices.DigitalContent.Task4_alert = False
            devices.DigitalContent.Task4_warning=False
            devices.DigitalContent.Status = 'On_Time'
        if devices.DigitalContent.Task5_complete_date:
            x = x + 1
            devices.DigitalContent.Task5_alert = False
            devices.DigitalContent.Task5_warning=False
            devices.DigitalContent.Status = 'On_Time'
        if devices.DigitalContent.Task6_complete_date:
            x = x + 1
            devices.DigitalContent.Task6_alert = False
            devices.DigitalContent.Task6_warning=False
            devices.DigitalContent.Status = 'On_Time'
        if devices.DigitalContent.Task7_complete_date:
            x =x+1
            devices.DigitalContent.Task7_alert = False
            devices.DigitalContent.Task7_warning=False
            devices.DigitalContent.Status = 'On_Time'
        if devices.DigitalContent.Task8_complete_date:
            x =x+1
            devices.DigitalContent.Task8_alert = False
            devices.DigitalContent.Task8_warning=False
            devices.DigitalContent.Status = 'On_Time'
        if devices.DigitalContent.Task9_complete_date:
            x =x+1
            devices.DigitalContent.Task9_alert = False
            devices.DigitalContent.Task9_warning=False
            devices.DigitalContent.Status = 'On_Time'
        if devices.DigitalContent.Task10_complete_date:
            x =x+1
            devices.DigitalContent.Task10_alert = False
            devices.DigitalContent.Task10_warning=False
            devices.DigitalContent.Status = 'On_Time'
        if devices.DigitalContent.Task11_complete_date:
            x =x+1
            devices.DigitalContent.Task11_alert = False
            devices.DigitalContent.Task11_warning=False
            devices.DigitalContent.Status = 'On_Time'
        if devices.DigitalContent.Task12_complete_date:
            x = x + 1
            devices.DigitalContent.Task12_alert = False
            devices.DigitalContent.Task12_warning=False
            devices.DigitalContent.Status = 'On_Time'
        if devices.DigitalContent.Task13_complete_date:
            x = x + 1
            devices.DigitalContent.Task13_alert = False
            devices.DigitalContent.Task13_warning=False
            devices.DigitalContent.Status = 'On_Time'
        if devices.DigitalContent.Task14_complete_date:
            x = x + 1
            devices.DigitalContent.Task14_alert = False
            devices.DigitalContent.Task14_warning=False
            devices.DigitalContent.Status = 'On_Time'
        if devices.DigitalContent.Task15_complete_date:
            x = x + 1
            devices.DigitalContent.Task15_alert = False
            devices.DigitalContent.Task15_warning=False
            devices.DigitalContent.Status = 'On_Time'
        if devices.DigitalContent.Task16_complete_date:
            x = x + 1
            devices.DigitalContent.Task16_alert = False
            devices.DigitalContent.Task16_warning=False
            devices.DigitalContent.Status = 'On_Time'
        if devices.DigitalContent.Task17_complete_date:
            x =x+1
            devices.DigitalContent.Task17_alert = False
            devices.DigitalContent.Task17_warning=False
            devices.DigitalContent.Status = 'On_Time'
        if devices.DigitalContent.Task18_complete_date:
            x =x+1
            devices.DigitalContent.Task18_alert = False
            devices.DigitalContent.Task18_warning=False
            devices.DigitalContent.Status = 'On_Time'
        if devices.DigitalContent.Task19_complete_date:
            x =x+1
            devices.DigitalContent.Task19_alert = False
            devices.DigitalContent.Task19_warning=False
            devices.DigitalContent.Status = 'On_Time'
        if devices.DigitalContent.Task20_complete_date:
            x =x+1
            devices.DigitalContent.Task20_alert = False
            devices.DigitalContent.Task20_warning=False
            devices.DigitalContent.Status = 'On_Time'
        percent = x/y * 100
        print (percent)

        #alerting logic
        today = datetime.date.today()
        if devices.DigitalContent.Task1_End_Date:
            Task1_delta =  devices.DigitalContent.Task1_End_Date - today
        else:
            Task1_delta = None
        if devices.DigitalContent.Task2_End_Date:
            Task2_delta = devices.DigitalContent.Task2_End_Date - today
        else:
            Task2_delta = None
        if devices.DigitalContent.Task3_End_Date:
            Task3_delta = devices.DigitalContent.Task3_End_Date - today
        else:
            Task3_delta = None
        if devices.DigitalContent.Task4_End_Date:
            Task4_delta = devices.DigitalContent.Task4_End_Date - today
        else:
            Task4_delta = None
        if devices.DigitalContent.Task5_End_Date:
            Task5_delta = devices.DigitalContent.Task5_End_Date - today
        else:
            Task5_delta = None
        if devices.DigitalContent.Task6_End_Date:
            Task6_delta = devices.DigitalContent.Task6_End_Date - today
        else:
            Task6_delta = None
        if devices.DigitalContent.Task7_End_Date:
            Task7_delta = devices.DigitalContent.Task7_End_Date - today
        else:
            Task7_delta = None
        if devices.DigitalContent.Task8_End_Date:
            Task8_delta = devices.DigitalContent.Task8_End_Date - today
        else:
            Task8_delta = None
        if devices.DigitalContent.Task9_End_Date:
            Task9_delta = devices.DigitalContent.Task9_End_Date - today
        else:
            Task9_delta = None
        if devices.DigitalContent.Task10_End_Date:
            Task10_delta =  devices.DigitalContent.Task10_End_Date - today
        else:
            Task10_delta = None
        if devices.DigitalContent.Task11_End_Date:
            Task11_delta =  devices.DigitalContent.Task11_End_Date - today
        else:
            Task11_delta = None
        if devices.DigitalContent.Task12_End_Date:
            Task12_delta = devices.DigitalContent.Task12_End_Date - today
        else:
            Task12_delta = None
        if devices.DigitalContent.Task13_End_Date:
            Task13_delta = devices.DigitalContent.Task13_End_Date - today
        else:
            Task13_delta = None
        if devices.DigitalContent.Task14_End_Date:
            Task14_delta = devices.DigitalContent.Task14_End_Date - today
        else:
            Task14_delta = None
        if devices.DigitalContent.Task15_End_Date:
            Task15_delta = devices.DigitalContent.Task15_End_Date - today
        else:
            Task15_delta = None
        if devices.DigitalContent.Task16_End_Date:
            Task16_delta = devices.DigitalContent.Task16_End_Date - today
        else:
            Task16_delta = None
        if devices.DigitalContent.Task17_End_Date:
            Task17_delta = devices.DigitalContent.Task17_End_Date - today
        else:
            Task17_delta = None
        if devices.DigitalContent.Task18_End_Date:
            Task18_delta = devices.DigitalContent.Task18_End_Date - today
        else:
            Task18_delta = None
        if devices.DigitalContent.Task19_End_Date:
            Task19_delta = devices.DigitalContent.Task19_End_Date - today
        else:
            Task19_delta = None
        if devices.DigitalContent.Task20_End_Date:
            Task20_delta = devices.DigitalContent.Task20_End_Date - today
        else:
            Task20_delta = None


        if Task1_delta and Task1_delta < timedelta(devices.DigitalContent.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not devices.DigitalContent.Task1_complete_date:
            devices.DigitalContent.Task1_warning = True
            devices.DigitalContent.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(devices.DigitalContent.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not devices.DigitalContent.Task2_complete_date:
            devices.DigitalContent.Task2_warning = True
            devices.DigitalContent.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(devices.DigitalContent.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not devices.DigitalContent.Task3_complete_date:
            devices.DigitalContent.Task3_warning = True
            devices.DigitalContent.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(devices.DigitalContent.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not devices.DigitalContent.Task4_complete_date:
            devices.DigitalContent.Task4_warning = True
            devices.DigitalContent.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(devices.DigitalContent.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not devices.DigitalContent.Task5_complete_date:
            devices.DigitalContent.Task5_warning = True
            devices.DigitalContent.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(devices.DigitalContent.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not devices.DigitalContent.Task6_complete_date:
            devices.DigitalContent.Task6_warning = True
            devices.DigitalContent.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(devices.DigitalContent.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not devices.DigitalContent.Task7_complete_date:
            devices.DigitalContent.Task7_warning = True
            devices.DigitalContent.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(devices.DigitalContent.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not devices.DigitalContent.Task8_complete_date:
            devices.DigitalContent.Task8_warning = True
            devices.DigitalContent.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(devices.DigitalContent.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not devices.DigitalContent.Task9_complete_date:
            devices.DigitalContent.Task9_warning = True
            devices.DigitalContent.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(devices.DigitalContent.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not devices.DigitalContent.Task10_complete_date:
            devices.DigitalContent.Task10_warning = True
            devices.DigitalContent.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(devices.DigitalContent.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not devices.DigitalContent.Task11_complete_date:
            devices.DigitalContent.Task11_warning = True
            devices.DigitalContent.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(devices.DigitalContent.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not devices.DigitalContent.Task12_complete_date:
            devices.DigitalContent.Task12_warning = True
            devices.DigitalContent.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(devices.DigitalContent.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not devices.DigitalContent.Task13_complete_date:
            devices.DigitalContent.Task13_warning = True
            devices.DigitalContent.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(devices.DigitalContent.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not devices.DigitalContent.Task14_complete_date:
            devices.DigitalContent.Task14_warning = True
            devices.DigitalContent.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(devices.DigitalContent.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not devices.DigitalContent.Task15_complete_date:
            devices.DigitalContent.Task15_warning = True
            devices.DigitalContent.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(devices.DigitalContent.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not devices.DigitalContent.Task16_complete_date:
            devices.DigitalContent.Task16_warning = True
            devices.DigitalContent.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(devices.DigitalContent.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not devices.DigitalContent.Task17_complete_date:
            devices.DigitalContent.Task17_warning = True
            devices.DigitalContent.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(devices.DigitalContent.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not devices.DigitalContent.Task18_complete_date:
            devices.DigitalContent.Task18_warning = True
            devices.DigitalContent.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(devices.DigitalContent.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not devices.DigitalContent.Task19_complete_date:
            devices.DigitalContent.Task19_warning = True
            devices.DigitalContent.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(devices.DigitalContent.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not devices.DigitalContent.Task20_complete_date:
            devices.DigitalContent.Task20_warning = True
            devices.DigitalContent.Status = 'At Risk'

        if devices.DigitalContent.Task1_End_Date and Task1_delta < timedelta(0) and not devices.DigitalContent.Task1_complete_date:
            devices.DigitalContent.Task1_alert = True
            devices.DigitalContent.Status = 'Delayed'
        if devices.DigitalContent.Task2_End_Date and Task2_delta < timedelta(0) and not devices.DigitalContent.Task2_complete_date:
            devices.DigitalContent.Task2_alert = True
            devices.DigitalContent.Status = 'Delayed'
        if devices.DigitalContent.Task3_End_Date and Task3_delta < timedelta(0) and not devices.DigitalContent.Task3_complete_date:
            devices.DigitalContent.Task3_alert = True
            devices.DigitalContent.Status = 'Delayed'
        if devices.DigitalContent.Task4_End_Date and Task4_delta < timedelta(0) and not devices.DigitalContent.Task4_complete_date:
            devices.DigitalContent.Task4_alert = True
            devices.DigitalContent.Status = 'Delayed'
        if devices.DigitalContent.Task5_End_Date and Task5_delta < timedelta(0) and not devices.DigitalContent.Task5_complete_date:
            devices.DigitalContent.Task5_alert = True
            devices.DigitalContent.Status = 'Delayed'
        if devices.DigitalContent.Task6_End_Date and Task6_delta < timedelta(0) and not devices.DigitalContent.Task6_complete_date:
            devices.DigitalContent.Task6_alert = True
            devices.DigitalContent.Status = 'Delayed'
        if devices.DigitalContent.Task7_End_Date and Task7_delta < timedelta(0) and not devices.DigitalContent.Task7_complete_date:
            devices.DigitalContent.Task7_alert = True
            devices.DigitalContent.Status = 'Delayed'
        if devices.DigitalContent.Task8_End_Date and Task8_delta < timedelta(0)and not devices.DigitalContent.Task8_complete_date:
            devices.DigitalContent.Task8_alert = True
            devices.DigitalContent.Status = 'Delayed'
        if devices.DigitalContent.Task9_End_Date and Task9_delta < timedelta(0)and not devices.DigitalContent.Task9_complete_date:
            devices.DigitalContent.Task9_alert = True
            devices.DigitalContent.Status = 'Delayed'
        if devices.DigitalContent.Task10_End_Date and Task10_delta < timedelta(0) and not devices.DigitalContent.Task10_complete_date:
            devices.DigitalContent.Task10_alert = True
            devices.DigitalContent.Status = 'Delayed'
        if devices.DigitalContent.Task11_End_Date and Task11_delta < timedelta(0) and not devices.DigitalContent.Task11_complete_date:
            devices.DigitalContent.Task11_alert = True
            devices.DigitalContent.Status = 'Delayed'
        if devices.DigitalContent.Task12_End_Date and Task12_delta < timedelta(0) and not devices.DigitalContent.Task12_complete_date:
            devices.DigitalContent.Task12_alert = True
            devices.DigitalContent.Status = 'Delayed'
        if devices.DigitalContent.Task13_End_Date and Task13_delta < timedelta(0) and not devices.DigitalContent.Task13_complete_date:
            devices.DigitalContent.Task13_alert = True
            devices.DigitalContent.Status = 'Delayed'
        if devices.DigitalContent.Task14_End_Date and Task14_delta < timedelta(0) and not devices.DigitalContent.Task14_complete_date:
            devices.DigitalContent.Task14_alert = True
            devices.DigitalContent.Status = 'Delayed'
        if devices.DigitalContent.Task15_End_Date and Task15_delta < timedelta(0) and not devices.DigitalContent.Task15_complete_date:
            devices.DigitalContent.Task15_alert = True
            devices.DigitalContent.Status = 'Delayed'
        if devices.DigitalContent.Task16_End_Date and Task16_delta < timedelta(0) and not devices.DigitalContent.Task16_complete_date:
            devices.DigitalContent.Task16_alert = True
            devices.DigitalContent.Status = 'Delayed'
        if devices.DigitalContent.Task17_End_Date and Task17_delta < timedelta(0)and not devices.DigitalContent.Task17_complete_date:
            devices.DigitalContent.Task17_alert = True
            devices.DigitalContent.Status = 'Delayed'
        if devices.DigitalContent.Task18_End_Date and Task18_delta < timedelta(0)and not devices.DigitalContent.Task18_complete_date:
            devices.DigitalContent.Task18_alert = True
            devices.DigitalContent.Status = 'Delayed'
        if devices.DigitalContent.Task19_End_Date and Task19_delta < timedelta(0)and not devices.DigitalContent.Task19_complete_date:
            devices.DigitalContent.Task19_alert = True
            devices.DigitalContent.Status = 'Delayed'
        if devices.DigitalContent.Task20_End_Date and Task20_delta < timedelta(0)and not devices.DigitalContent.Task20_complete_date:
            devices.DigitalContent.Task20_alert = True
            devices.DigitalContent.Status = 'Delayed'

        devices.DigitalContent.completed = int(percent)
        devices.DigitalContent.save()
        posts1 = devices.DigitalContent.task1statusdigitalcontent_set.all().order_by('-created')
        posts2 = devices.DigitalContent.task2statusdigitalcontent_set.all().order_by('-created')
        posts3 = devices.DigitalContent.task3statusdigitalcontent_set.all().order_by('-created')
        posts4 = devices.DigitalContent.task4statusdigitalcontent_set.all().order_by('-created')
        posts5 = devices.DigitalContent.task5statusdigitalcontent_set.all().order_by('-created')
        posts6 = devices.DigitalContent.task6statusdigitalcontent_set.all().order_by('-created')
        posts7 = devices.DigitalContent.task7statusdigitalcontent_set.all().order_by('-created')
        posts8 = devices.DigitalContent.task8statusdigitalcontent_set.all().order_by('-created')
        posts9 = devices.DigitalContent.task9statusdigitalcontent_set.all().order_by('-created')
        posts10 = devices.DigitalContent.task10statusdigitalcontent_set.all().order_by('-created')
        posts11 = devices.DigitalContent.task11statusdigitalcontent_set.all().order_by('-created')
        posts12 = devices.DigitalContent.task12statusdigitalcontent_set.all().order_by('-created')
        posts13 = devices.DigitalContent.task13statusdigitalcontent_set.all().order_by('-created')
        posts14 = devices.DigitalContent.task14statusdigitalcontent_set.all().order_by('-created')
        posts15 = devices.DigitalContent.task15statusdigitalcontent_set.all().order_by('-created')
        posts16 = devices.DigitalContent.task16statusdigitalcontent_set.all().order_by('-created')
        posts17 = devices.DigitalContent.task17statusdigitalcontent_set.all().order_by('-created')
        posts18 = devices.DigitalContent.task18statusdigitalcontent_set.all().order_by('-created')
        posts19 = devices.DigitalContent.task19statusdigitalcontent_set.all().order_by('-created')
        posts20 = devices.DigitalContent.task20statusdigitalcontent_set.all().order_by('-created')

        args = {'devices':devices, 'form1':form1, 'form2':form2, 'form3':form3, 'form4':form4, 'form5':form5, 'form6':form6,
                'form7': form7, 'form8':form8, 'form9':form9, 'form10':form10, 'form11':form11, 'form12':form12, 'form13':form13,
                'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17, 'form18': form18, 'form19': form19,
                'form20': form20, 'posts1':posts1, 'posts2':posts2, 'posts3':posts3, 'posts4':posts4, 'posts5':posts5, 'posts6':posts6,
                'posts7': posts7, 'posts8':posts8, 'posts9':posts9, 'posts10':posts10, 'posts11':posts11, 'posts12':posts12, 'posts13':posts13,
                'posts14': posts14, 'posts15': posts15, 'posts16': posts16, 'posts17': posts17, 'posts18': posts18, 'posts19': posts19,
                'posts20': posts20, 'Task1_vc_dateform':Task1_vc_dateform, 'Task2_vc_dateform':Task2_vc_dateform,
                'Task3_vc_dateform':Task3_vc_dateform, 'Task4_vc_dateform':Task4_vc_dateform,
                'Task5_vc_dateform': Task5_vc_dateform, 'Task6_vc_dateform': Task6_vc_dateform,
                'Task7_vc_dateform': Task7_vc_dateform, 'Task8_vc_dateform': Task8_vc_dateform,
                'Task9_vc_dateform': Task9_vc_dateform, 'Task10_vc_dateform': Task10_vc_dateform,
                'Task11_vc_dateform': Task11_vc_dateform, 'Task12_vc_dateform': Task12_vc_dateform,
                'Task13_vc_dateform': Task13_vc_dateform, 'Task14_vc_dateform': Task14_vc_dateform,
                'Task15_vc_dateform': Task15_vc_dateform, 'Task16_vc_dateform': Task16_vc_dateform,
                'Task17_vc_dateform': Task17_vc_dateform, 'Task18_vc_dateform': Task18_vc_dateform,
                'Task19_vc_dateform': Task19_vc_dateform, 'Task20_vc_dateform': Task20_vc_dateform,
                'Task1_delta':Task1_delta, 'Task7_delta':Task7_delta, 'Task12_delta':Task12_delta, 'Task17_delta':Task17_delta,
                'Task2_delta': Task2_delta, 'Task8_delta': Task8_delta, 'Task13_delta': Task13_delta,
                'Task3_delta': Task3_delta, 'Task9_delta':Task9_delta, 'Task14_delta':Task14_delta, 'Task18_delta':Task18_delta,
                'Task4_delta':Task4_delta, 'Task10_delta':Task10_delta, 'Task15_delta':Task15_delta, 'Task19_delta':Task19_delta,
                'Task5_delta':Task5_delta, 'Task11_delta':Task11_delta, 'Task16_delta':Task16_delta, 'Task20_delta':Task20_delta,
                'Task6_delta':Task6_delta,
                }
        return render(request,self.template_name,args)

    def post(self, request, pk):

        form1 = Task1_dc_form(request.POST)
        form2 = Task2_dc_form(request.POST)
        form3 = Task3_dc_form(request.POST)
        form4 = Task4_dc_form(request.POST)
        form5 = Task5_dc_form(request.POST)
        form6 = Task6_dc_form(request.POST)
        form7 = Task7_dc_form(request.POST)
        form8 = Task8_dc_form(request.POST)
        form9 = Task9_dc_form(request.POST)
        form10 = Task10_dc_form(request.POST)
        form11 = Task11_dc_form(request.POST)
        form12 = Task12_dc_form(request.POST)
        form13 = Task13_dc_form(request.POST)
        form14 = Task14_dc_form(request.POST)
        form15 = Task15_dc_form(request.POST)
        form16 = Task16_dc_form(request.POST)
        form17 = Task17_dc_form(request.POST)
        form18 = Task18_dc_form(request.POST)
        form19 = Task19_dc_form(request.POST)
        form20 = Task20_dc_form(request.POST)
        devices = Device.objects.get(pk=pk)

        Task1_vc_dateform = Task1_dc_date_form(request.POST,instance=devices.DigitalContent)
        Task2_vc_dateform = Task2_dc_date_form(request.POST,instance=devices.DigitalContent)
        Task3_vc_dateform = Task3_dc_date_form(request.POST,instance=devices.DigitalContent)
        Task4_vc_dateform = Task4_dc_date_form(request.POST,instance=devices.DigitalContent)
        Task5_vc_dateform = Task5_dc_date_form(request.POST,instance=devices.DigitalContent)
        Task6_vc_dateform = Task6_dc_date_form(request.POST,instance=devices.DigitalContent)
        Task7_vc_dateform = Task7_dc_date_form(request.POST,instance=devices.DigitalContent)
        Task8_vc_dateform = Task8_dc_date_form(request.POST,instance=devices.DigitalContent)
        Task9_vc_dateform = Task9_dc_date_form(request.POST,instance=devices.DigitalContent)
        Task10_vc_dateform = Task10_dc_date_form(request.POST,instance=devices.DigitalContent)
        Task11_vc_dateform = Task11_dc_date_form(request.POST,instance=devices.DigitalContent)
        Task12_vc_dateform = Task12_dc_date_form(request.POST,instance=devices.DigitalContent)
        Task13_vc_dateform = Task13_dc_date_form(request.POST,instance=devices.DigitalContent)
        Task14_vc_dateform = Task14_dc_date_form(request.POST,instance=devices.DigitalContent)
        Task15_vc_dateform = Task15_dc_date_form(request.POST,instance=devices.DigitalContent)
        Task16_vc_dateform = Task16_dc_date_form(request.POST,instance=devices.DigitalContent)
        Task17_vc_dateform = Task17_dc_date_form(request.POST,instance=devices.DigitalContent)
        Task18_vc_dateform = Task18_dc_date_form(request.POST,instance=devices.DigitalContent)
        Task19_vc_dateform = Task19_dc_date_form(request.POST,instance=devices.DigitalContent)
        Task20_vc_dateform = Task20_dc_date_form(request.POST,instance=devices.DigitalContent)

        if 'Task1Submit' in request.POST:
            if form1.is_valid() and Task1_vc_dateform.is_valid():
                post = form1.save(commit=False)
                post.user = request.user
                post.DigitalContent = devices.DigitalContent
                Task1_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk + '/digitalcontent')
            else:
                return redirect('/login/summary/' + pk + '/digitalcontent')
        elif 'Task2Submit' in request.POST:
            if form2.is_valid() and Task2_vc_dateform.is_valid():
                post = form2.save(commit=False)
                post.user = request.user
                post.DigitalContent = devices.DigitalContent
                Task2_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/digitalcontent')
            else:
                return redirect('/login/summary/' + pk + '/digitalcontent')
        elif 'Task3Submit' in request.POST:
            if form3.is_valid() and Task3_vc_dateform.is_valid():
                post = form3.save(commit=False)
                post.user = request.user
                post.DigitalContent = devices.DigitalContent
                Task3_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/digitalcontent')
            else:
                return redirect('/login/summary/' + pk + '/digitalcontent')
        elif 'Task4Submit' in request.POST:
            if form4.is_valid() and Task4_vc_dateform.is_valid():
                post = form4.save(commit=False)
                post.user = request.user
                post.DigitalContent = devices.DigitalContent
                Task4_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/digitalcontent')
            else:
                return redirect('/login/summary/' + pk + '/digitalcontent')
        elif 'Task5Submit' in request.POST:
            if form5.is_valid() and Task5_vc_dateform.is_valid():
                post = form5.save(commit=False)
                post.user = request.user
                post.DigitalContent = devices.DigitalContent
                Task5_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/digitalcontent')
            else:
                return redirect('/login/summary/' + pk + '/digitalcontent')
        elif 'Task6Submit' in request.POST:
            if form6.is_valid() and Task6_vc_dateform.is_valid():
                post = form6.save(commit=False)
                post.user = request.user
                post.DigitalContent = devices.DigitalContent
                Task6_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/digitalcontent')
            else:
                return redirect('/login/summary/' + pk + '/digitalcontent')
        elif 'Task7Submit' in request.POST:
            if form7.is_valid() and Task7_vc_dateform.is_valid():
                post = form7.save(commit=False)
                post.user = request.user
                post.DigitalContent = devices.DigitalContent
                Task7_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/digitalcontent')
            else:
                return redirect('/login/summary/' + pk + '/digitalcontent')
        elif 'Task8Submit' in request.POST:
            if form8.is_valid() and Task8_vc_dateform.is_valid():
                post = form8.save(commit=False)
                post.user = request.user
                post.DigitalContent = devices.DigitalContent
                Task8_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/digitalcontent')
            else:
                return redirect('/login/summary/' + pk + '/digitalcontent')
        elif 'Task9Submit' in request.POST:
            if form9.is_valid() and Task9_vc_dateform.is_valid():
                post = form9.save(commit=False)
                post.user = request.user
                post.DigitalContent = devices.DigitalContent
                Task9_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/digitalcontent')
            else:
                return redirect('/login/summary/' + pk + '/digitalcontent')
        elif 'Task10Submit' in request.POST:
            if form10.is_valid() and Task10_vc_dateform.is_valid():
                post = form10.save(commit=False)
                post.user = request.user
                post.DigitalContent = devices.DigitalContent
                Task10_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/digitalcontent')
            else:
                return redirect('/login/summary/' + pk + '/digitalcontent')
        elif 'Task11Submit' in request.POST:
            if form11.is_valid() and Task11_vc_dateform.is_valid():
                post = form11.save(commit=False)
                post.user = request.user
                post.DigitalContent = devices.DigitalContent
                Task11_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/digitalcontent')
            else:
                return redirect('/login/summary/' + pk + '/digitalcontent')
        elif 'Task12Submit' in request.POST:
            if form12.is_valid() and Task12_vc_dateform.is_valid():
                post = form12.save(commit=False)
                post.user = request.user
                post.DigitalContent = devices.DigitalContent
                Task12_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/digitalcontent')
            else:
                return redirect('/login/summary/' + pk + '/digitalcontent')
        elif 'Task13Submit' in request.POST:
            if form13.is_valid() and Task13_vc_dateform.is_valid():
                post = form13.save(commit=False)
                post.user = request.user
                post.DigitalContent = devices.DigitalContent
                Task13_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/digitalcontent')
            else:
                return redirect('/login/summary/' + pk + '/digitalcontent')
        elif 'Task14Submit' in request.POST:
            if form14.is_valid() and Task14_vc_dateform.is_valid():
                post = form14.save(commit=False)
                post.user = request.user
                post.DigitalContent = devices.DigitalContent
                Task14_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/digitalcontent')
            else:
                return redirect('/login/summary/' + pk + '/digitalcontent')
        elif 'Task15Submit' in request.POST:
            if form15.is_valid() and Task15_vc_dateform.is_valid():
                post = form15.save(commit=False)
                post.user = request.user
                post.DigitalContent = devices.DigitalContent
                Task15_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/digitalcontent')
            else:
                return redirect('/login/summary/' + pk + '/digitalcontent')
        elif 'Task16Submit' in request.POST:
            if form16.is_valid() and Task16_vc_dateform.is_valid():
                post = form16.save(commit=False)
                post.user = request.user
                post.DigitalContent = devices.DigitalContent
                Task16_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/digitalcontent')
            else:
                return redirect('/login/summary/' + pk + '/digitalcontent')
        elif 'Task17Submit' in request.POST:
            if form17.is_valid() and Task17_vc_dateform.is_valid():
                post = form17.save(commit=False)
                post.user = request.user
                post.DigitalContent = devices.DigitalContent
                Task17_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/digitalcontent')
            else:
                return redirect('/login/summary/' + pk + '/digitalcontent')
        elif 'Task18Submit' in request.POST:
            if form18.is_valid() and Task18_vc_dateform.is_valid():
                post = form18.save(commit=False)
                post.user = request.user
                post.DigitalContent = devices.DigitalContent
                Task18_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/digitalcontent')
            else:
                return redirect('/login/summary/' + pk + '/digitalcontent')
        elif 'Task19Submit' in request.POST:
            if form19.is_valid() and Task19_vc_dateform.is_valid():
                post = form19.save(commit=False)
                post.user = request.user
                post.DigitalContent = devices.DigitalContent
                Task19_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/digitalcontent')
            else:
                return redirect('/login/summary/' + pk + '/digitalcontent')
        elif 'Task20Submit' in request.POST:
            if form20.is_valid() and Task20_vc_dateform.is_valid():
                post = form20.save(commit=False)
                post.user = request.user
                post.DigitalContent = devices.DigitalContent
                Task20_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/digitalcontent')
            else:
                return redirect('/login/summary/' + pk + '/digitalcontent')

########################################################################################################################

class CallCenterOperationsView(LoginRequiredMixin,TemplateView):
    template_name = 'login/device5.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        form1 = Task1_cco_form()
        form2 = Task2_cco_form()
        form3 = Task3_cco_form()
        form4 = Task4_cco_form()
        form5 = Task5_cco_form()
        form6 = Task6_cco_form()
        form7 = Task7_cco_form()
        form8 = Task8_cco_form()
        form9 = Task9_cco_form()
        form10 = Task10_cco_form()
        form11 = Task11_cco_form()
        form12 = Task12_cco_form()
        form13 = Task13_cco_form()
        form14 = Task14_cco_form()
        form15 = Task15_cco_form()
        form16 = Task16_cco_form()
        form17 = Task17_cco_form()
        form18 = Task18_cco_form()
        form19 = Task19_cco_form()
        form20 = Task20_cco_form()
        devices = Device.objects.get(pk=pk)
        Task1_vc_dateform = Task1_cco_date_form(instance=devices.CallCenterOpertaions)
        Task2_vc_dateform = Task2_cco_date_form(instance=devices.CallCenterOpertaions)
        Task3_vc_dateform = Task3_cco_date_form(instance=devices.CallCenterOpertaions)
        Task4_vc_dateform = Task4_cco_date_form(instance=devices.CallCenterOpertaions)
        Task5_vc_dateform = Task5_cco_date_form(instance=devices.CallCenterOpertaions)
        Task6_vc_dateform = Task6_cco_date_form(instance=devices.CallCenterOpertaions)
        Task7_vc_dateform = Task7_cco_date_form(instance=devices.CallCenterOpertaions)
        Task8_vc_dateform = Task8_cco_date_form(instance=devices.CallCenterOpertaions)
        Task9_vc_dateform = Task9_cco_date_form(instance=devices.CallCenterOpertaions)
        Task10_vc_dateform = Task10_cco_date_form(instance=devices.CallCenterOpertaions)
        Task11_vc_dateform = Task11_cco_date_form(instance=devices.CallCenterOpertaions)
        Task12_vc_dateform = Task12_cco_date_form(instance=devices.CallCenterOpertaions)
        Task13_vc_dateform = Task13_cco_date_form(instance=devices.CallCenterOpertaions)
        Task14_vc_dateform = Task14_cco_date_form(instance=devices.CallCenterOpertaions)
        Task15_vc_dateform = Task15_cco_date_form(instance=devices.CallCenterOpertaions)
        Task16_vc_dateform = Task16_cco_date_form(instance=devices.CallCenterOpertaions)
        Task17_vc_dateform = Task17_cco_date_form(instance=devices.CallCenterOpertaions)
        Task18_vc_dateform = Task18_cco_date_form(instance=devices.CallCenterOpertaions)
        Task19_vc_dateform = Task19_cco_date_form(instance=devices.CallCenterOpertaions)
        Task20_vc_dateform = Task20_cco_date_form(instance=devices.CallCenterOpertaions)

        #Calculating % completed
        y=0
        if devices.CallCenterOpertaions.Task1_Name:
            y=y+1
        if devices.CallCenterOpertaions.Task2_Name:
            y=y+1
        if devices.CallCenterOpertaions.Task3_Name:
            y=y+1
        if devices.CallCenterOpertaions.Task4_Name:
            y=y+1
        if devices.CallCenterOpertaions.Task5_Name:
            y=y+1
        if devices.CallCenterOpertaions.Task6_Name:
            y=y+1
        if devices.CallCenterOpertaions.Task7_Name:
            y=y+1
        if devices.CallCenterOpertaions.Task8_Name:
            y=y+1
        if devices.CallCenterOpertaions.Task9_Name:
            y=y+1
        if devices.CallCenterOpertaions.Task10_Name:
            y=y+1
        if devices.CallCenterOpertaions.Task11_Name:
            y=y+1
        if devices.CallCenterOpertaions.Task12_Name:
            y=y+1
        if devices.CallCenterOpertaions.Task13_Name:
            y=y+1
        if devices.CallCenterOpertaions.Task14_Name:
            y=y+1
        if devices.CallCenterOpertaions.Task15_Name:
            y=y+1
        if devices.CallCenterOpertaions.Task16_Name:
            y=y+1
        if devices.CallCenterOpertaions.Task17_Name:
            y=y+1
        if devices.CallCenterOpertaions.Task18_Name:
            y=y+1
        if devices.CallCenterOpertaions.Task19_Name:
            y=y+1
        if devices.CallCenterOpertaions.Task20_Name:
            y=y+1

        x = 0
        if devices.CallCenterOpertaions.Task1_complete_date:
            x =x+1
            devices.CallCenterOpertaions.Task1_alert = False
            devices.CallCenterOpertaions.Task1_warning=False
            devices.CallCenterOpertaions.Status='On_Time'
        if devices.CallCenterOpertaions.Task2_complete_date:
            x = x + 1
            devices.CallCenterOpertaions.Task2_alert = False
            devices.CallCenterOpertaions.Task2_warning=False
            devices.CallCenterOpertaions.Status = 'On_Time'
        if devices.CallCenterOpertaions.Task3_complete_date:
            x = x + 1
            devices.CallCenterOpertaions.Task3_alert = False
            devices.CallCenterOpertaions.Task3_warning=False
            devices.CallCenterOpertaions.Status = 'On_Time'
        if devices.CallCenterOpertaions.Task4_complete_date:
            x = x + 1
            devices.CallCenterOpertaions.Task4_alert = False
            devices.CallCenterOpertaions.Task4_warning=False
            devices.CallCenterOpertaions.Status = 'On_Time'
        if devices.CallCenterOpertaions.Task5_complete_date:
            x = x + 1
            devices.CallCenterOpertaions.Task5_alert = False
            devices.CallCenterOpertaions.Task5_warning=False
            devices.CallCenterOpertaions.Status = 'On_Time'
        if devices.CallCenterOpertaions.Task6_complete_date:
            x = x + 1
            devices.CallCenterOpertaions.Task6_alert = False
            devices.CallCenterOpertaions.Task6_warning=False
            devices.CallCenterOpertaions.Status = 'On_Time'
        if devices.CallCenterOpertaions.Task7_complete_date:
            x =x+1
            devices.CallCenterOpertaions.Task7_alert = False
            devices.CallCenterOpertaions.Task7_warning=False
            devices.CallCenterOpertaions.Status = 'On_Time'
        if devices.CallCenterOpertaions.Task8_complete_date:
            x =x+1
            devices.CallCenterOpertaions.Task8_alert = False
            devices.CallCenterOpertaions.Task8_warning=False
            devices.CallCenterOpertaions.Status = 'On_Time'
        if devices.CallCenterOpertaions.Task9_complete_date:
            x =x+1
            devices.CallCenterOpertaions.Task9_alert = False
            devices.CallCenterOpertaions.Task9_warning=False
            devices.CallCenterOpertaions.Status = 'On_Time'
        if devices.CallCenterOpertaions.Task10_complete_date:
            x =x+1
            devices.CallCenterOpertaions.Task10_alert = False
            devices.CallCenterOpertaions.Task10_warning=False
            devices.CallCenterOpertaions.Status = 'On_Time'
        if devices.CallCenterOpertaions.Task11_complete_date:
            x =x+1
            devices.CallCenterOpertaions.Task11_alert = False
            devices.CallCenterOpertaions.Task11_warning=False
            devices.CallCenterOpertaions.Status = 'On_Time'
        if devices.CallCenterOpertaions.Task12_complete_date:
            x = x + 1
            devices.CallCenterOpertaions.Task12_alert = False
            devices.CallCenterOpertaions.Task12_warning=False
            devices.CallCenterOpertaions.Status = 'On_Time'
        if devices.CallCenterOpertaions.Task13_complete_date:
            x = x + 1
            devices.CallCenterOpertaions.Task13_alert = False
            devices.CallCenterOpertaions.Task13_warning=False
            devices.CallCenterOpertaions.Status = 'On_Time'
        if devices.CallCenterOpertaions.Task14_complete_date:
            x = x + 1
            devices.CallCenterOpertaions.Task14_alert = False
            devices.CallCenterOpertaions.Task14_warning=False
            devices.CallCenterOpertaions.Status = 'On_Time'
        if devices.CallCenterOpertaions.Task15_complete_date:
            x = x + 1
            devices.CallCenterOpertaions.Task15_alert = False
            devices.CallCenterOpertaions.Task15_warning=False
            devices.CallCenterOpertaions.Status = 'On_Time'
        if devices.CallCenterOpertaions.Task16_complete_date:
            x = x + 1
            devices.CallCenterOpertaions.Task16_alert = False
            devices.CallCenterOpertaions.Task16_warning=False
            devices.CallCenterOpertaions.Status = 'On_Time'
        if devices.CallCenterOpertaions.Task17_complete_date:
            x =x+1
            devices.CallCenterOpertaions.Task17_alert = False
            devices.CallCenterOpertaions.Task17_warning=False
            devices.CallCenterOpertaions.Status = 'On_Time'
        if devices.CallCenterOpertaions.Task18_complete_date:
            x =x+1
            devices.CallCenterOpertaions.Task18_alert = False
            devices.CallCenterOpertaions.Task18_warning=False
            devices.CallCenterOpertaions.Status = 'On_Time'
        if devices.CallCenterOpertaions.Task19_complete_date:
            x =x+1
            devices.CallCenterOpertaions.Task19_alert = False
            devices.CallCenterOpertaions.Task19_warning=False
            devices.CallCenterOpertaions.Status = 'On_Time'
        if devices.CallCenterOpertaions.Task20_complete_date:
            x =x+1
            devices.CallCenterOpertaions.Task20_alert = False
            devices.CallCenterOpertaions.Task20_warning=False
            devices.CallCenterOpertaions.Status = 'On_Time'
        percent = x/y * 100
        print (percent)

        #alerting logic
        today = datetime.date.today()
        if devices.CallCenterOpertaions.Task1_End_Date:
            Task1_delta =  devices.CallCenterOpertaions.Task1_End_Date - today
        else:
            Task1_delta = None
        if devices.CallCenterOpertaions.Task2_End_Date:
            Task2_delta = devices.CallCenterOpertaions.Task2_End_Date - today
        else:
            Task2_delta = None
        if devices.CallCenterOpertaions.Task3_End_Date:
            Task3_delta = devices.CallCenterOpertaions.Task3_End_Date - today
        else:
            Task3_delta = None
        if devices.CallCenterOpertaions.Task4_End_Date:
            Task4_delta = devices.CallCenterOpertaions.Task4_End_Date - today
        else:
            Task4_delta = None
        if devices.CallCenterOpertaions.Task5_End_Date:
            Task5_delta = devices.CallCenterOpertaions.Task5_End_Date - today
        else:
            Task5_delta = None
        if devices.CallCenterOpertaions.Task6_End_Date:
            Task6_delta = devices.CallCenterOpertaions.Task6_End_Date - today
        else:
            Task6_delta = None
        if devices.CallCenterOpertaions.Task7_End_Date:
            Task7_delta = devices.CallCenterOpertaions.Task7_End_Date - today
        else:
            Task7_delta = None
        if devices.CallCenterOpertaions.Task8_End_Date:
            Task8_delta = devices.CallCenterOpertaions.Task8_End_Date - today
        else:
            Task8_delta = None
        if devices.CallCenterOpertaions.Task9_End_Date:
            Task9_delta = devices.CallCenterOpertaions.Task9_End_Date - today
        else:
            Task9_delta = None
        if devices.CallCenterOpertaions.Task10_End_Date:
            Task10_delta =  devices.CallCenterOpertaions.Task10_End_Date - today
        else:
            Task10_delta = None
        if devices.CallCenterOpertaions.Task11_End_Date:
            Task11_delta =  devices.CallCenterOpertaions.Task11_End_Date - today
        else:
            Task11_delta = None
        if devices.CallCenterOpertaions.Task12_End_Date:
            Task12_delta = devices.CallCenterOpertaions.Task12_End_Date - today
        else:
            Task12_delta = None
        if devices.CallCenterOpertaions.Task13_End_Date:
            Task13_delta = devices.CallCenterOpertaions.Task13_End_Date - today
        else:
            Task13_delta = None
        if devices.CallCenterOpertaions.Task14_End_Date:
            Task14_delta = devices.CallCenterOpertaions.Task14_End_Date - today
        else:
            Task14_delta = None
        if devices.CallCenterOpertaions.Task15_End_Date:
            Task15_delta = devices.CallCenterOpertaions.Task15_End_Date - today
        else:
            Task15_delta = None
        if devices.CallCenterOpertaions.Task16_End_Date:
            Task16_delta = devices.CallCenterOpertaions.Task16_End_Date - today
        else:
            Task16_delta = None
        if devices.CallCenterOpertaions.Task17_End_Date:
            Task17_delta = devices.CallCenterOpertaions.Task17_End_Date - today
        else:
            Task17_delta = None
        if devices.CallCenterOpertaions.Task18_End_Date:
            Task18_delta = devices.CallCenterOpertaions.Task18_End_Date - today
        else:
            Task18_delta = None
        if devices.CallCenterOpertaions.Task19_End_Date:
            Task19_delta = devices.CallCenterOpertaions.Task19_End_Date - today
        else:
            Task19_delta = None
        if devices.CallCenterOpertaions.Task20_End_Date:
            Task20_delta = devices.CallCenterOpertaions.Task20_End_Date - today
        else:
            Task20_delta = None


        if Task1_delta and Task1_delta < timedelta(devices.CallCenterOpertaions.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not devices.CallCenterOpertaions.Task1_complete_date:
            devices.CallCenterOpertaions.Task1_warning = True
            devices.CallCenterOpertaions.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(devices.CallCenterOpertaions.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not devices.CallCenterOpertaions.Task2_complete_date:
            devices.CallCenterOpertaions.Task2_warning = True
            devices.CallCenterOpertaions.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(devices.CallCenterOpertaions.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not devices.CallCenterOpertaions.Task3_complete_date:
            devices.CallCenterOpertaions.Task3_warning = True
            devices.CallCenterOpertaions.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(devices.CallCenterOpertaions.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not devices.CallCenterOpertaions.Task4_complete_date:
            devices.CallCenterOpertaions.Task4_warning = True
            devices.CallCenterOpertaions.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(devices.CallCenterOpertaions.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not devices.CallCenterOpertaions.Task5_complete_date:
            devices.CallCenterOpertaions.Task5_warning = True
            devices.CallCenterOpertaions.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(devices.CallCenterOpertaions.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not devices.CallCenterOpertaions.Task6_complete_date:
            devices.CallCenterOpertaions.Task6_warning = True
            devices.CallCenterOpertaions.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(devices.CallCenterOpertaions.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not devices.CallCenterOpertaions.Task7_complete_date:
            devices.CallCenterOpertaions.Task7_warning = True
            devices.CallCenterOpertaions.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(devices.CallCenterOpertaions.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not devices.CallCenterOpertaions.Task8_complete_date:
            devices.CallCenterOpertaions.Task8_warning = True
            devices.CallCenterOpertaions.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(devices.CallCenterOpertaions.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not devices.CallCenterOpertaions.Task9_complete_date:
            devices.CallCenterOpertaions.Task9_warning = True
            devices.CallCenterOpertaions.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(devices.CallCenterOpertaions.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not devices.CallCenterOpertaions.Task10_complete_date:
            devices.CallCenterOpertaions.Task10_warning = True
            devices.CallCenterOpertaions.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(devices.CallCenterOpertaions.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not devices.CallCenterOpertaions.Task11_complete_date:
            devices.CallCenterOpertaions.Task11_warning = True
            devices.CallCenterOpertaions.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(devices.CallCenterOpertaions.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not devices.CallCenterOpertaions.Task12_complete_date:
            devices.CallCenterOpertaions.Task12_warning = True
            devices.CallCenterOpertaions.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(devices.CallCenterOpertaions.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not devices.CallCenterOpertaions.Task13_complete_date:
            devices.CallCenterOpertaions.Task13_warning = True
            devices.CallCenterOpertaions.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(devices.CallCenterOpertaions.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not devices.CallCenterOpertaions.Task14_complete_date:
            devices.CallCenterOpertaions.Task14_warning = True
            devices.CallCenterOpertaions.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(devices.CallCenterOpertaions.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not devices.CallCenterOpertaions.Task15_complete_date:
            devices.CallCenterOpertaions.Task15_warning = True
            devices.CallCenterOpertaions.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(devices.CallCenterOpertaions.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not devices.CallCenterOpertaions.Task16_complete_date:
            devices.CallCenterOpertaions.Task16_warning = True
            devices.CallCenterOpertaions.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(devices.CallCenterOpertaions.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not devices.CallCenterOpertaions.Task17_complete_date:
            devices.CallCenterOpertaions.Task17_warning = True
            devices.CallCenterOpertaions.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(devices.CallCenterOpertaions.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not devices.CallCenterOpertaions.Task18_complete_date:
            devices.CallCenterOpertaions.Task18_warning = True
            devices.CallCenterOpertaions.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(devices.CallCenterOpertaions.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not devices.CallCenterOpertaions.Task19_complete_date:
            devices.CallCenterOpertaions.Task19_warning = True
            devices.CallCenterOpertaions.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(devices.CallCenterOpertaions.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not devices.CallCenterOpertaions.Task20_complete_date:
            devices.CallCenterOpertaions.Task20_warning = True
            devices.CallCenterOpertaions.Status = 'At Risk'

        if devices.CallCenterOpertaions.Task1_End_Date and Task1_delta < timedelta(0) and not devices.CallCenterOpertaions.Task1_complete_date:
            devices.CallCenterOpertaions.Task1_alert = True
            devices.CallCenterOpertaions.Status = 'Delayed'
        if devices.CallCenterOpertaions.Task2_End_Date and Task2_delta < timedelta(0) and not devices.CallCenterOpertaions.Task2_complete_date:
            devices.CallCenterOpertaions.Task2_alert = True
            devices.CallCenterOpertaions.Status = 'Delayed'
        if devices.CallCenterOpertaions.Task3_End_Date and Task3_delta < timedelta(0) and not devices.CallCenterOpertaions.Task3_complete_date:
            devices.CallCenterOpertaions.Task3_alert = True
            devices.CallCenterOpertaions.Status = 'Delayed'
        if devices.CallCenterOpertaions.Task4_End_Date and Task4_delta < timedelta(0) and not devices.CallCenterOpertaions.Task4_complete_date:
            devices.CallCenterOpertaions.Task4_alert = True
            devices.CallCenterOpertaions.Status = 'Delayed'
        if devices.CallCenterOpertaions.Task5_End_Date and Task5_delta < timedelta(0) and not devices.CallCenterOpertaions.Task5_complete_date:
            devices.CallCenterOpertaions.Task5_alert = True
            devices.CallCenterOpertaions.Status = 'Delayed'
        if devices.CallCenterOpertaions.Task6_End_Date and Task6_delta < timedelta(0) and not devices.CallCenterOpertaions.Task6_complete_date:
            devices.CallCenterOpertaions.Task6_alert = True
            devices.CallCenterOpertaions.Status = 'Delayed'
        if devices.CallCenterOpertaions.Task7_End_Date and Task7_delta < timedelta(0) and not devices.CallCenterOpertaions.Task7_complete_date:
            devices.CallCenterOpertaions.Task7_alert = True
            devices.CallCenterOpertaions.Status = 'Delayed'
        if devices.CallCenterOpertaions.Task8_End_Date and Task8_delta < timedelta(0)and not devices.CallCenterOpertaions.Task8_complete_date:
            devices.CallCenterOpertaions.Task8_alert = True
            devices.CallCenterOpertaions.Status = 'Delayed'
        if devices.CallCenterOpertaions.Task9_End_Date and Task9_delta < timedelta(0)and not devices.CallCenterOpertaions.Task9_complete_date:
            devices.CallCenterOpertaions.Task9_alert = True
            devices.CallCenterOpertaions.Status = 'Delayed'
        if devices.CallCenterOpertaions.Task10_End_Date and Task10_delta < timedelta(0) and not devices.CallCenterOpertaions.Task10_complete_date:
            devices.CallCenterOpertaions.Task10_alert = True
            devices.CallCenterOpertaions.Status = 'Delayed'
        if devices.CallCenterOpertaions.Task11_End_Date and Task11_delta < timedelta(0) and not devices.CallCenterOpertaions.Task11_complete_date:
            devices.CallCenterOpertaions.Task11_alert = True
            devices.CallCenterOpertaions.Status = 'Delayed'
        if devices.CallCenterOpertaions.Task12_End_Date and Task12_delta < timedelta(0) and not devices.CallCenterOpertaions.Task12_complete_date:
            devices.CallCenterOpertaions.Task12_alert = True
            devices.CallCenterOpertaions.Status = 'Delayed'
        if devices.CallCenterOpertaions.Task13_End_Date and Task13_delta < timedelta(0) and not devices.CallCenterOpertaions.Task13_complete_date:
            devices.CallCenterOpertaions.Task13_alert = True
            devices.CallCenterOpertaions.Status = 'Delayed'
        if devices.CallCenterOpertaions.Task14_End_Date and Task14_delta < timedelta(0) and not devices.CallCenterOpertaions.Task14_complete_date:
            devices.CallCenterOpertaions.Task14_alert = True
            devices.CallCenterOpertaions.Status = 'Delayed'
        if devices.CallCenterOpertaions.Task15_End_Date and Task15_delta < timedelta(0) and not devices.CallCenterOpertaions.Task15_complete_date:
            devices.CallCenterOpertaions.Task15_alert = True
            devices.CallCenterOpertaions.Status = 'Delayed'
        if devices.CallCenterOpertaions.Task16_End_Date and Task16_delta < timedelta(0) and not devices.CallCenterOpertaions.Task16_complete_date:
            devices.CallCenterOpertaions.Task16_alert = True
            devices.CallCenterOpertaions.Status = 'Delayed'
        if devices.CallCenterOpertaions.Task17_End_Date and Task17_delta < timedelta(0)and not devices.CallCenterOpertaions.Task17_complete_date:
            devices.CallCenterOpertaions.Task17_alert = True
            devices.CallCenterOpertaions.Status = 'Delayed'
        if devices.CallCenterOpertaions.Task18_End_Date and Task18_delta < timedelta(0)and not devices.CallCenterOpertaions.Task18_complete_date:
            devices.CallCenterOpertaions.Task18_alert = True
            devices.CallCenterOpertaions.Status = 'Delayed'
        if devices.CallCenterOpertaions.Task19_End_Date and Task19_delta < timedelta(0)and not devices.CallCenterOpertaions.Task19_complete_date:
            devices.CallCenterOpertaions.Task19_alert = True
            devices.CallCenterOpertaions.Status = 'Delayed'
        if devices.CallCenterOpertaions.Task20_End_Date and Task20_delta < timedelta(0)and not devices.CallCenterOpertaions.Task20_complete_date:
            devices.CallCenterOpertaions.Task20_alert = True
            devices.CallCenterOpertaions.Status = 'Delayed'

        devices.CallCenterOpertaions.completed = int(percent)
        devices.CallCenterOpertaions.save()
        posts1 = devices.CallCenterOpertaions.task1statuscallcenteropertaions_set.all().order_by('-created')
        posts2 = devices.CallCenterOpertaions.task2statuscallcenteropertaions_set.all().order_by('-created')
        posts3 = devices.CallCenterOpertaions.task3statuscallcenteropertaions_set.all().order_by('-created')
        posts4 = devices.CallCenterOpertaions.task4statuscallcenteropertaions_set.all().order_by('-created')
        posts5 = devices.CallCenterOpertaions.task5statuscallcenteropertaions_set.all().order_by('-created')
        posts6 = devices.CallCenterOpertaions.task6statuscallcenteropertaions_set.all().order_by('-created')
        posts7 = devices.CallCenterOpertaions.task7statuscallcenteropertaions_set.all().order_by('-created')
        posts8 = devices.CallCenterOpertaions.task8statuscallcenteropertaions_set.all().order_by('-created')
        posts9 = devices.CallCenterOpertaions.task9statuscallcenteropertaions_set.all().order_by('-created')
        posts10 = devices.CallCenterOpertaions.task10statuscallcenteropertaions_set.all().order_by('-created')
        posts11 = devices.CallCenterOpertaions.task11statuscallcenteropertaions_set.all().order_by('-created')
        posts12 = devices.CallCenterOpertaions.task12statuscallcenteropertaions_set.all().order_by('-created')
        posts13 = devices.CallCenterOpertaions.task13statuscallcenteropertaions_set.all().order_by('-created')
        posts14 = devices.CallCenterOpertaions.task14statuscallcenteropertaions_set.all().order_by('-created')
        posts15 = devices.CallCenterOpertaions.task15statuscallcenteropertaions_set.all().order_by('-created')
        posts16 = devices.CallCenterOpertaions.task16statuscallcenteropertaions_set.all().order_by('-created')
        posts17 = devices.CallCenterOpertaions.task17statuscallcenteropertaions_set.all().order_by('-created')
        posts18 = devices.CallCenterOpertaions.task18statuscallcenteropertaions_set.all().order_by('-created')
        posts19 = devices.CallCenterOpertaions.task19statuscallcenteropertaions_set.all().order_by('-created')
        posts20 = devices.CallCenterOpertaions.task20statuscallcenteropertaions_set.all().order_by('-created')

        args = {'devices':devices, 'form1':form1, 'form2':form2, 'form3':form3, 'form4':form4, 'form5':form5, 'form6':form6,
                'form7': form7, 'form8':form8, 'form9':form9, 'form10':form10, 'form11':form11, 'form12':form12, 'form13':form13,
                'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17, 'form18': form18, 'form19': form19,
                'form20': form20, 'posts1':posts1, 'posts2':posts2, 'posts3':posts3, 'posts4':posts4, 'posts5':posts5, 'posts6':posts6,
                'posts7': posts7, 'posts8':posts8, 'posts9':posts9, 'posts10':posts10, 'posts11':posts11, 'posts12':posts12, 'posts13':posts13,
                'posts14': posts14, 'posts15': posts15, 'posts16': posts16, 'posts17': posts17, 'posts18': posts18, 'posts19': posts19,
                'posts20': posts20, 'Task1_vc_dateform':Task1_vc_dateform, 'Task2_vc_dateform':Task2_vc_dateform,
                'Task3_vc_dateform':Task3_vc_dateform, 'Task4_vc_dateform':Task4_vc_dateform,
                'Task5_vc_dateform': Task5_vc_dateform, 'Task6_vc_dateform': Task6_vc_dateform,
                'Task7_vc_dateform': Task7_vc_dateform, 'Task8_vc_dateform': Task8_vc_dateform,
                'Task9_vc_dateform': Task9_vc_dateform, 'Task10_vc_dateform': Task10_vc_dateform,
                'Task11_vc_dateform': Task11_vc_dateform, 'Task12_vc_dateform': Task12_vc_dateform,
                'Task13_vc_dateform': Task13_vc_dateform, 'Task14_vc_dateform': Task14_vc_dateform,
                'Task15_vc_dateform': Task15_vc_dateform, 'Task16_vc_dateform': Task16_vc_dateform,
                'Task17_vc_dateform': Task17_vc_dateform, 'Task18_vc_dateform': Task18_vc_dateform,
                'Task19_vc_dateform': Task19_vc_dateform, 'Task20_vc_dateform': Task20_vc_dateform,
                'Task1_delta':Task1_delta, 'Task7_delta':Task7_delta, 'Task12_delta':Task12_delta, 'Task17_delta':Task17_delta,
                'Task2_delta': Task2_delta, 'Task8_delta': Task8_delta, 'Task13_delta': Task13_delta,
                'Task3_delta': Task3_delta, 'Task9_delta':Task9_delta, 'Task14_delta':Task14_delta, 'Task18_delta':Task18_delta,
                'Task4_delta':Task4_delta, 'Task10_delta':Task10_delta, 'Task15_delta':Task15_delta, 'Task19_delta':Task19_delta,
                'Task5_delta':Task5_delta, 'Task11_delta':Task11_delta, 'Task16_delta':Task16_delta, 'Task20_delta':Task20_delta,
                'Task6_delta':Task6_delta,
                }
        return render(request,self.template_name,args)

    def post(self, request, pk):

        form1 = Task1_cco_form(request.POST)
        form2 = Task2_cco_form(request.POST)
        form3 = Task3_cco_form(request.POST)
        form4 = Task4_cco_form(request.POST)
        form5 = Task5_cco_form(request.POST)
        form6 = Task6_cco_form(request.POST)
        form7 = Task7_cco_form(request.POST)
        form8 = Task8_cco_form(request.POST)
        form9 = Task9_cco_form(request.POST)
        form10 = Task10_cco_form(request.POST)
        form11 = Task11_cco_form(request.POST)
        form12 = Task12_cco_form(request.POST)
        form13 = Task13_cco_form(request.POST)
        form14 = Task14_cco_form(request.POST)
        form15 = Task15_cco_form(request.POST)
        form16 = Task16_cco_form(request.POST)
        form17 = Task17_cco_form(request.POST)
        form18 = Task18_cco_form(request.POST)
        form19 = Task19_cco_form(request.POST)
        form20 = Task20_cco_form(request.POST)
        devices = Device.objects.get(pk=pk)

        Task1_vc_dateform = Task1_cco_date_form(request.POST,instance=devices.CallCenterOpertaions)
        Task2_vc_dateform = Task2_cco_date_form(request.POST,instance=devices.CallCenterOpertaions)
        Task3_vc_dateform = Task3_cco_date_form(request.POST,instance=devices.CallCenterOpertaions)
        Task4_vc_dateform = Task4_cco_date_form(request.POST,instance=devices.CallCenterOpertaions)
        Task5_vc_dateform = Task5_cco_date_form(request.POST,instance=devices.CallCenterOpertaions)
        Task6_vc_dateform = Task6_cco_date_form(request.POST,instance=devices.CallCenterOpertaions)
        Task7_vc_dateform = Task7_cco_date_form(request.POST,instance=devices.CallCenterOpertaions)
        Task8_vc_dateform = Task8_cco_date_form(request.POST,instance=devices.CallCenterOpertaions)
        Task9_vc_dateform = Task9_cco_date_form(request.POST,instance=devices.CallCenterOpertaions)
        Task10_vc_dateform = Task10_cco_date_form(request.POST,instance=devices.CallCenterOpertaions)
        Task11_vc_dateform = Task11_cco_date_form(request.POST,instance=devices.CallCenterOpertaions)
        Task12_vc_dateform = Task12_cco_date_form(request.POST,instance=devices.CallCenterOpertaions)
        Task13_vc_dateform = Task13_cco_date_form(request.POST,instance=devices.CallCenterOpertaions)
        Task14_vc_dateform = Task14_cco_date_form(request.POST,instance=devices.CallCenterOpertaions)
        Task15_vc_dateform = Task15_cco_date_form(request.POST,instance=devices.CallCenterOpertaions)
        Task16_vc_dateform = Task16_cco_date_form(request.POST,instance=devices.CallCenterOpertaions)
        Task17_vc_dateform = Task17_cco_date_form(request.POST,instance=devices.CallCenterOpertaions)
        Task18_vc_dateform = Task18_cco_date_form(request.POST,instance=devices.CallCenterOpertaions)
        Task19_vc_dateform = Task19_cco_date_form(request.POST,instance=devices.CallCenterOpertaions)
        Task20_vc_dateform = Task20_cco_date_form(request.POST,instance=devices.CallCenterOpertaions)

        if 'Task1Submit' in request.POST:
            if form1.is_valid() and Task1_vc_dateform.is_valid():
                post = form1.save(commit=False)
                post.user = request.user
                post.CallCenterOpertaions = devices.CallCenterOpertaions
                Task1_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk + '/callcenteroperations')
            else:
                return redirect('/login/summary/' + pk + '/callcenteroperations')
        elif 'Task2Submit' in request.POST:
            if form2.is_valid() and Task2_vc_dateform.is_valid():
                post = form2.save(commit=False)
                post.user = request.user
                post.CallCenterOpertaions = devices.CallCenterOpertaions
                Task2_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcenteroperations')
            else:
                return redirect('/login/summary/' + pk + '/callcenteroperations')
        elif 'Task3Submit' in request.POST:
            if form3.is_valid() and Task3_vc_dateform.is_valid():
                post = form3.save(commit=False)
                post.user = request.user
                post.CallCenterOpertaions = devices.CallCenterOpertaions
                Task3_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcenteroperations')
            else:
                return redirect('/login/summary/' + pk + '/callcenteroperations')
        elif 'Task4Submit' in request.POST:
            if form4.is_valid() and Task4_vc_dateform.is_valid():
                post = form4.save(commit=False)
                post.user = request.user
                post.CallCenterOpertaions = devices.CallCenterOpertaions
                Task4_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcenteroperations')
            else:
                return redirect('/login/summary/' + pk + '/callcenteroperations')
        elif 'Task5Submit' in request.POST:
            if form5.is_valid() and Task5_vc_dateform.is_valid():
                post = form5.save(commit=False)
                post.user = request.user
                post.CallCenterOpertaions = devices.CallCenterOpertaions
                Task5_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcenteroperations')
            else:
                return redirect('/login/summary/' + pk + '/callcenteroperations')
        elif 'Task6Submit' in request.POST:
            if form6.is_valid() and Task6_vc_dateform.is_valid():
                post = form6.save(commit=False)
                post.user = request.user
                post.CallCenterOpertaions = devices.CallCenterOpertaions
                Task6_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcenteroperations')
            else:
                return redirect('/login/summary/' + pk + '/callcenteroperations')
        elif 'Task7Submit' in request.POST:
            if form7.is_valid() and Task7_vc_dateform.is_valid():
                post = form7.save(commit=False)
                post.user = request.user
                post.CallCenterOpertaions = devices.CallCenterOpertaions
                Task7_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcenteroperations')
            else:
                return redirect('/login/summary/' + pk + '/callcenteroperations')
        elif 'Task8Submit' in request.POST:
            if form8.is_valid() and Task8_vc_dateform.is_valid():
                post = form8.save(commit=False)
                post.user = request.user
                post.CallCenterOpertaions = devices.CallCenterOpertaions
                Task8_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcenteroperations')
            else:
                return redirect('/login/summary/' + pk + '/callcenteroperations')
        elif 'Task9Submit' in request.POST:
            if form9.is_valid() and Task9_vc_dateform.is_valid():
                post = form9.save(commit=False)
                post.user = request.user
                post.CallCenterOpertaions = devices.CallCenterOpertaions
                Task9_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcenteroperations')
            else:
                return redirect('/login/summary/' + pk + '/callcenteroperations')
        elif 'Task10Submit' in request.POST:
            if form10.is_valid() and Task10_vc_dateform.is_valid():
                post = form10.save(commit=False)
                post.user = request.user
                post.CallCenterOpertaions = devices.CallCenterOpertaions
                Task10_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcenteroperations')
            else:
                return redirect('/login/summary/' + pk + '/callcenteroperations')
        elif 'Task11Submit' in request.POST:
            if form11.is_valid() and Task11_vc_dateform.is_valid():
                post = form11.save(commit=False)
                post.user = request.user
                post.CallCenterOpertaions = devices.CallCenterOpertaions
                Task11_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcenteroperations')
            else:
                return redirect('/login/summary/' + pk + '/callcenteroperations')
        elif 'Task12Submit' in request.POST:
            if form12.is_valid() and Task12_vc_dateform.is_valid():
                post = form12.save(commit=False)
                post.user = request.user
                post.CallCenterOpertaions = devices.CallCenterOpertaions
                Task12_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcenteroperations')
            else:
                return redirect('/login/summary/' + pk + '/callcenteroperations')
        elif 'Task13Submit' in request.POST:
            if form13.is_valid() and Task13_vc_dateform.is_valid():
                post = form13.save(commit=False)
                post.user = request.user
                post.CallCenterOpertaions = devices.CallCenterOpertaions
                Task13_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcenteroperations')
            else:
                return redirect('/login/summary/' + pk + '/callcenteroperations')
        elif 'Task14Submit' in request.POST:
            if form14.is_valid() and Task14_vc_dateform.is_valid():
                post = form14.save(commit=False)
                post.user = request.user
                post.CallCenterOpertaions = devices.CallCenterOpertaions
                Task14_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcenteroperations')
            else:
                return redirect('/login/summary/' + pk + '/callcenteroperations')
        elif 'Task15Submit' in request.POST:
            if form15.is_valid() and Task15_vc_dateform.is_valid():
                post = form15.save(commit=False)
                post.user = request.user
                post.CallCenterOpertaions = devices.CallCenterOpertaions
                Task15_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcenteroperations')
            else:
                return redirect('/login/summary/' + pk + '/callcenteroperations')
        elif 'Task16Submit' in request.POST:
            if form16.is_valid() and Task16_vc_dateform.is_valid():
                post = form16.save(commit=False)
                post.user = request.user
                post.CallCenterOpertaions = devices.CallCenterOpertaions
                Task16_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcenteroperations')
            else:
                return redirect('/login/summary/' + pk + '/callcenteroperations')
        elif 'Task17Submit' in request.POST:
            if form17.is_valid() and Task17_vc_dateform.is_valid():
                post = form17.save(commit=False)
                post.user = request.user
                post.CallCenterOpertaions = devices.CallCenterOpertaions
                Task17_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcenteroperations')
            else:
                return redirect('/login/summary/' + pk + '/callcenteroperations')
        elif 'Task18Submit' in request.POST:
            if form18.is_valid() and Task18_vc_dateform.is_valid():
                post = form18.save(commit=False)
                post.user = request.user
                post.CallCenterOpertaions = devices.CallCenterOpertaions
                Task18_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcenteroperations')
            else:
                return redirect('/login/summary/' + pk + '/callcenteroperations')
        elif 'Task19Submit' in request.POST:
            if form19.is_valid() and Task19_vc_dateform.is_valid():
                post = form19.save(commit=False)
                post.user = request.user
                post.CallCenterOpertaions = devices.CallCenterOpertaions
                Task19_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcenteroperations')
            else:
                return redirect('/login/summary/' + pk + '/callcenteroperations')
        elif 'Task20Submit' in request.POST:
            if form20.is_valid() and Task20_vc_dateform.is_valid():
                post = form20.save(commit=False)
                post.user = request.user
                post.CallCenterOpertaions = devices.CallCenterOpertaions
                Task20_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/callcenteroperations')
            else:
                return redirect('/login/summary/' + pk + '/callcenteroperations')

########################################################################################################################

class ProductSupportView(LoginRequiredMixin,TemplateView):
    template_name = 'login/device6.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        form1 = Task1_ps_form()
        form2 = Task2_ps_form()
        form3 = Task3_ps_form()
        form4 = Task4_ps_form()
        form5 = Task5_ps_form()
        form6 = Task6_ps_form()
        form7 = Task7_ps_form()
        form8 = Task8_ps_form()
        form9 = Task9_ps_form()
        form10 = Task10_ps_form()
        form11 = Task11_ps_form()
        form12 = Task12_ps_form()
        form13 = Task13_ps_form()
        form14 = Task14_ps_form()
        form15 = Task15_ps_form()
        form16 = Task16_ps_form()
        form17 = Task17_ps_form()
        form18 = Task18_ps_form()
        form19 = Task19_ps_form()
        form20 = Task20_ps_form()
        devices = Device.objects.get(pk=pk)
        Task1_vc_dateform = Task1_ps_date_form(instance=devices.ProductSupport)
        Task2_vc_dateform = Task2_ps_date_form(instance=devices.ProductSupport)
        Task3_vc_dateform = Task3_ps_date_form(instance=devices.ProductSupport)
        Task4_vc_dateform = Task4_ps_date_form(instance=devices.ProductSupport)
        Task5_vc_dateform = Task5_ps_date_form(instance=devices.ProductSupport)
        Task6_vc_dateform = Task6_ps_date_form(instance=devices.ProductSupport)
        Task7_vc_dateform = Task7_ps_date_form(instance=devices.ProductSupport)
        Task8_vc_dateform = Task8_ps_date_form(instance=devices.ProductSupport)
        Task9_vc_dateform = Task9_ps_date_form(instance=devices.ProductSupport)
        Task10_vc_dateform = Task10_ps_date_form(instance=devices.ProductSupport)
        Task11_vc_dateform = Task11_ps_date_form(instance=devices.ProductSupport)
        Task12_vc_dateform = Task12_ps_date_form(instance=devices.ProductSupport)
        Task13_vc_dateform = Task13_ps_date_form(instance=devices.ProductSupport)
        Task14_vc_dateform = Task14_ps_date_form(instance=devices.ProductSupport)
        Task15_vc_dateform = Task15_ps_date_form(instance=devices.ProductSupport)
        Task16_vc_dateform = Task16_ps_date_form(instance=devices.ProductSupport)
        Task17_vc_dateform = Task17_ps_date_form(instance=devices.ProductSupport)
        Task18_vc_dateform = Task18_ps_date_form(instance=devices.ProductSupport)
        Task19_vc_dateform = Task19_ps_date_form(instance=devices.ProductSupport)
        Task20_vc_dateform = Task20_ps_date_form(instance=devices.ProductSupport)

        #Calculating % completed
        y=0
        if devices.ProductSupport.Task1_Name:
            y=y+1
        if devices.ProductSupport.Task2_Name:
            y=y+1
        if devices.ProductSupport.Task3_Name:
            y=y+1
        if devices.ProductSupport.Task4_Name:
            y=y+1
        if devices.ProductSupport.Task5_Name:
            y=y+1
        if devices.ProductSupport.Task6_Name:
            y=y+1
        if devices.ProductSupport.Task7_Name:
            y=y+1
        if devices.ProductSupport.Task8_Name:
            y=y+1
        if devices.ProductSupport.Task9_Name:
            y=y+1
        if devices.ProductSupport.Task10_Name:
            y=y+1
        if devices.ProductSupport.Task11_Name:
            y=y+1
        if devices.ProductSupport.Task12_Name:
            y=y+1
        if devices.ProductSupport.Task13_Name:
            y=y+1
        if devices.ProductSupport.Task14_Name:
            y=y+1
        if devices.ProductSupport.Task15_Name:
            y=y+1
        if devices.ProductSupport.Task16_Name:
            y=y+1
        if devices.ProductSupport.Task17_Name:
            y=y+1
        if devices.ProductSupport.Task18_Name:
            y=y+1
        if devices.ProductSupport.Task19_Name:
            y=y+1
        if devices.ProductSupport.Task20_Name:
            y=y+1

        x = 0
        if devices.ProductSupport.Task1_complete_date:
            x =x+1
            devices.ProductSupport.Task1_alert = False
            devices.ProductSupport.Task1_warning=False
            devices.ProductSupport.Status='On_Time'
        if devices.ProductSupport.Task2_complete_date:
            x = x + 1
            devices.ProductSupport.Task2_alert = False
            devices.ProductSupport.Task2_warning=False
            devices.ProductSupport.Status = 'On_Time'
        if devices.ProductSupport.Task3_complete_date:
            x = x + 1
            devices.ProductSupport.Task3_alert = False
            devices.ProductSupport.Task3_warning=False
            devices.ProductSupport.Status = 'On_Time'
        if devices.ProductSupport.Task4_complete_date:
            x = x + 1
            devices.ProductSupport.Task4_alert = False
            devices.ProductSupport.Task4_warning=False
            devices.ProductSupport.Status = 'On_Time'
        if devices.ProductSupport.Task5_complete_date:
            x = x + 1
            devices.ProductSupport.Task5_alert = False
            devices.ProductSupport.Task5_warning=False
            devices.ProductSupport.Status = 'On_Time'
        if devices.ProductSupport.Task6_complete_date:
            x = x + 1
            devices.ProductSupport.Task6_alert = False
            devices.ProductSupport.Task6_warning=False
            devices.ProductSupport.Status = 'On_Time'
        if devices.ProductSupport.Task7_complete_date:
            x =x+1
            devices.ProductSupport.Task7_alert = False
            devices.ProductSupport.Task7_warning=False
            devices.ProductSupport.Status = 'On_Time'
        if devices.ProductSupport.Task8_complete_date:
            x =x+1
            devices.ProductSupport.Task8_alert = False
            devices.ProductSupport.Task8_warning=False
            devices.ProductSupport.Status = 'On_Time'
        if devices.ProductSupport.Task9_complete_date:
            x =x+1
            devices.ProductSupport.Task9_alert = False
            devices.ProductSupport.Task9_warning=False
            devices.ProductSupport.Status = 'On_Time'
        if devices.ProductSupport.Task10_complete_date:
            x =x+1
            devices.ProductSupport.Task10_alert = False
            devices.ProductSupport.Task10_warning=False
            devices.ProductSupport.Status = 'On_Time'
        if devices.ProductSupport.Task11_complete_date:
            x =x+1
            devices.ProductSupport.Task11_alert = False
            devices.ProductSupport.Task11_warning=False
            devices.ProductSupport.Status = 'On_Time'
        if devices.ProductSupport.Task12_complete_date:
            x = x + 1
            devices.ProductSupport.Task12_alert = False
            devices.ProductSupport.Task12_warning=False
            devices.ProductSupport.Status = 'On_Time'
        if devices.ProductSupport.Task13_complete_date:
            x = x + 1
            devices.ProductSupport.Task13_alert = False
            devices.ProductSupport.Task13_warning=False
            devices.ProductSupport.Status = 'On_Time'
        if devices.ProductSupport.Task14_complete_date:
            x = x + 1
            devices.ProductSupport.Task14_alert = False
            devices.ProductSupport.Task14_warning=False
            devices.ProductSupport.Status = 'On_Time'
        if devices.ProductSupport.Task15_complete_date:
            x = x + 1
            devices.ProductSupport.Task15_alert = False
            devices.ProductSupport.Task15_warning=False
            devices.ProductSupport.Status = 'On_Time'
        if devices.ProductSupport.Task16_complete_date:
            x = x + 1
            devices.ProductSupport.Task16_alert = False
            devices.ProductSupport.Task16_warning=False
            devices.ProductSupport.Status = 'On_Time'
        if devices.ProductSupport.Task17_complete_date:
            x =x+1
            devices.ProductSupport.Task17_alert = False
            devices.ProductSupport.Task17_warning=False
            devices.ProductSupport.Status = 'On_Time'
        if devices.ProductSupport.Task18_complete_date:
            x =x+1
            devices.ProductSupport.Task18_alert = False
            devices.ProductSupport.Task18_warning=False
            devices.ProductSupport.Status = 'On_Time'
        if devices.ProductSupport.Task19_complete_date:
            x =x+1
            devices.ProductSupport.Task19_alert = False
            devices.ProductSupport.Task19_warning=False
            devices.ProductSupport.Status = 'On_Time'
        if devices.ProductSupport.Task20_complete_date:
            x =x+1
            devices.ProductSupport.Task20_alert = False
            devices.ProductSupport.Task20_warning=False
            devices.ProductSupport.Status = 'On_Time'
        percent = x/y * 100
        print (percent)

        #alerting logic
        today = datetime.date.today()
        if devices.ProductSupport.Task1_End_Date:
            Task1_delta =  devices.ProductSupport.Task1_End_Date - today
        else:
            Task1_delta = None
        if devices.ProductSupport.Task2_End_Date:
            Task2_delta = devices.ProductSupport.Task2_End_Date - today
        else:
            Task2_delta = None
        if devices.ProductSupport.Task3_End_Date:
            Task3_delta = devices.ProductSupport.Task3_End_Date - today
        else:
            Task3_delta = None
        if devices.ProductSupport.Task4_End_Date:
            Task4_delta = devices.ProductSupport.Task4_End_Date - today
        else:
            Task4_delta = None
        if devices.ProductSupport.Task5_End_Date:
            Task5_delta = devices.ProductSupport.Task5_End_Date - today
        else:
            Task5_delta = None
        if devices.ProductSupport.Task6_End_Date:
            Task6_delta = devices.ProductSupport.Task6_End_Date - today
        else:
            Task6_delta = None
        if devices.ProductSupport.Task7_End_Date:
            Task7_delta = devices.ProductSupport.Task7_End_Date - today
        else:
            Task7_delta = None
        if devices.ProductSupport.Task8_End_Date:
            Task8_delta = devices.ProductSupport.Task8_End_Date - today
        else:
            Task8_delta = None
        if devices.ProductSupport.Task9_End_Date:
            Task9_delta = devices.ProductSupport.Task9_End_Date - today
        else:
            Task9_delta = None
        if devices.ProductSupport.Task10_End_Date:
            Task10_delta =  devices.ProductSupport.Task10_End_Date - today
        else:
            Task10_delta = None
        if devices.ProductSupport.Task11_End_Date:
            Task11_delta =  devices.ProductSupport.Task11_End_Date - today
        else:
            Task11_delta = None
        if devices.ProductSupport.Task12_End_Date:
            Task12_delta = devices.ProductSupport.Task12_End_Date - today
        else:
            Task12_delta = None
        if devices.ProductSupport.Task13_End_Date:
            Task13_delta = devices.ProductSupport.Task13_End_Date - today
        else:
            Task13_delta = None
        if devices.ProductSupport.Task14_End_Date:
            Task14_delta = devices.ProductSupport.Task14_End_Date - today
        else:
            Task14_delta = None
        if devices.ProductSupport.Task15_End_Date:
            Task15_delta = devices.ProductSupport.Task15_End_Date - today
        else:
            Task15_delta = None
        if devices.ProductSupport.Task16_End_Date:
            Task16_delta = devices.ProductSupport.Task16_End_Date - today
        else:
            Task16_delta = None
        if devices.ProductSupport.Task17_End_Date:
            Task17_delta = devices.ProductSupport.Task17_End_Date - today
        else:
            Task17_delta = None
        if devices.ProductSupport.Task18_End_Date:
            Task18_delta = devices.ProductSupport.Task18_End_Date - today
        else:
            Task18_delta = None
        if devices.ProductSupport.Task19_End_Date:
            Task19_delta = devices.ProductSupport.Task19_End_Date - today
        else:
            Task19_delta = None
        if devices.ProductSupport.Task20_End_Date:
            Task20_delta = devices.ProductSupport.Task20_End_Date - today
        else:
            Task20_delta = None

        if Task1_delta and Task1_delta < timedelta(devices.ProductSupport.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not devices.ProductSupport.Task1_complete_date:
            devices.ProductSupport.Task1_warning = True
            devices.ProductSupport.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(devices.ProductSupport.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not devices.ProductSupport.Task2_complete_date:
            devices.ProductSupport.Task2_warning = True
            devices.ProductSupport.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(devices.ProductSupport.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not devices.ProductSupport.Task3_complete_date:
            devices.ProductSupport.Task3_warning = True
            devices.ProductSupport.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(devices.ProductSupport.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not devices.ProductSupport.Task4_complete_date:
            devices.ProductSupport.Task4_warning = True
            devices.ProductSupport.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(devices.ProductSupport.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not devices.ProductSupport.Task5_complete_date:
            devices.ProductSupport.Task5_warning = True
            devices.ProductSupport.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(devices.ProductSupport.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not devices.ProductSupport.Task6_complete_date:
            devices.ProductSupport.Task6_warning = True
            devices.ProductSupport.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(devices.ProductSupport.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not devices.ProductSupport.Task7_complete_date:
            devices.ProductSupport.Task7_warning = True
            devices.ProductSupport.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(devices.ProductSupport.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not devices.ProductSupport.Task8_complete_date:
            devices.ProductSupport.Task8_warning = True
            devices.ProductSupport.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(devices.ProductSupport.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not devices.ProductSupport.Task9_complete_date:
            devices.ProductSupport.Task9_warning = True
            devices.ProductSupport.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(devices.ProductSupport.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not devices.ProductSupport.Task10_complete_date:
            devices.ProductSupport.Task10_warning = True
            devices.ProductSupport.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(devices.ProductSupport.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not devices.ProductSupport.Task11_complete_date:
            devices.ProductSupport.Task11_warning = True
            devices.ProductSupport.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(devices.ProductSupport.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not devices.ProductSupport.Task12_complete_date:
            devices.ProductSupport.Task12_warning = True
            devices.ProductSupport.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(devices.ProductSupport.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not devices.ProductSupport.Task13_complete_date:
            devices.ProductSupport.Task13_warning = True
            devices.ProductSupport.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(devices.ProductSupport.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not devices.ProductSupport.Task14_complete_date:
            devices.ProductSupport.Task14_warning = True
            devices.ProductSupport.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(devices.ProductSupport.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not devices.ProductSupport.Task15_complete_date:
            devices.ProductSupport.Task15_warning = True
            devices.ProductSupport.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(devices.ProductSupport.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not devices.ProductSupport.Task16_complete_date:
            devices.ProductSupport.Task16_warning = True
            devices.ProductSupport.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(devices.ProductSupport.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not devices.ProductSupport.Task17_complete_date:
            devices.ProductSupport.Task17_warning = True
            devices.ProductSupport.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(devices.ProductSupport.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not devices.ProductSupport.Task18_complete_date:
            devices.ProductSupport.Task18_warning = True
            devices.ProductSupport.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(devices.ProductSupport.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not devices.ProductSupport.Task19_complete_date:
            devices.ProductSupport.Task19_warning = True
            devices.ProductSupport.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(devices.ProductSupport.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not devices.ProductSupport.Task20_complete_date:
            devices.ProductSupport.Task20_warning = True
            devices.ProductSupport.Status = 'At Risk'


        if devices.ProductSupport.Task1_End_Date and Task1_delta < timedelta(0) and not devices.ProductSupport.Task1_complete_date:
            devices.ProductSupport.Task1_alert = True
            devices.ProductSupport.Status = 'Delayed'
        if devices.ProductSupport.Task2_End_Date and Task2_delta < timedelta(0) and not devices.ProductSupport.Task2_complete_date:
            devices.ProductSupport.Task2_alert = True
            devices.ProductSupport.Status = 'Delayed'
        if devices.ProductSupport.Task3_End_Date and Task3_delta < timedelta(0) and not devices.ProductSupport.Task3_complete_date:
            devices.ProductSupport.Task3_alert = True
            devices.ProductSupport.Status = 'Delayed'
        if devices.ProductSupport.Task4_End_Date and Task4_delta < timedelta(0) and not devices.ProductSupport.Task4_complete_date:
            devices.ProductSupport.Task4_alert = True
            devices.ProductSupport.Status = 'Delayed'
        if devices.ProductSupport.Task5_End_Date and Task5_delta < timedelta(0) and not devices.ProductSupport.Task5_complete_date:
            devices.ProductSupport.Task5_alert = True
            devices.ProductSupport.Status = 'Delayed'
        if devices.ProductSupport.Task6_End_Date and Task6_delta < timedelta(0) and not devices.ProductSupport.Task6_complete_date:
            devices.ProductSupport.Task6_alert = True
            devices.ProductSupport.Status = 'Delayed'
        if devices.ProductSupport.Task7_End_Date and Task7_delta < timedelta(0) and not devices.ProductSupport.Task7_complete_date:
            devices.ProductSupport.Task7_alert = True
            devices.ProductSupport.Status = 'Delayed'
        if devices.ProductSupport.Task8_End_Date and Task8_delta < timedelta(0)and not devices.ProductSupport.Task8_complete_date:
            devices.ProductSupport.Task8_alert = True
            devices.ProductSupport.Status = 'Delayed'
        if devices.ProductSupport.Task9_End_Date and Task9_delta < timedelta(0)and not devices.ProductSupport.Task9_complete_date:
            devices.ProductSupport.Task9_alert = True
            devices.ProductSupport.Status = 'Delayed'
        if devices.ProductSupport.Task10_End_Date and Task10_delta < timedelta(0) and not devices.ProductSupport.Task10_complete_date:
            devices.ProductSupport.Task10_alert = True
            devices.ProductSupport.Status = 'Delayed'
        if devices.ProductSupport.Task11_End_Date and Task11_delta < timedelta(0) and not devices.ProductSupport.Task11_complete_date:
            devices.ProductSupport.Task11_alert = True
            devices.ProductSupport.Status = 'Delayed'
        if devices.ProductSupport.Task12_End_Date and Task12_delta < timedelta(0) and not devices.ProductSupport.Task12_complete_date:
            devices.ProductSupport.Task12_alert = True
            devices.ProductSupport.Status = 'Delayed'
        if devices.ProductSupport.Task13_End_Date and Task13_delta < timedelta(0) and not devices.ProductSupport.Task13_complete_date:
            devices.ProductSupport.Task13_alert = True
            devices.ProductSupport.Status = 'Delayed'
        if devices.ProductSupport.Task14_End_Date and Task14_delta < timedelta(0) and not devices.ProductSupport.Task14_complete_date:
            devices.ProductSupport.Task14_alert = True
            devices.ProductSupport.Status = 'Delayed'
        if devices.ProductSupport.Task15_End_Date and Task15_delta < timedelta(0) and not devices.ProductSupport.Task15_complete_date:
            devices.ProductSupport.Task15_alert = True
            devices.ProductSupport.Status = 'Delayed'
        if devices.ProductSupport.Task16_End_Date and Task16_delta < timedelta(0) and not devices.ProductSupport.Task16_complete_date:
            devices.ProductSupport.Task16_alert = True
            devices.ProductSupport.Status = 'Delayed'
        if devices.ProductSupport.Task17_End_Date and Task17_delta < timedelta(0)and not devices.ProductSupport.Task17_complete_date:
            devices.ProductSupport.Task17_alert = True
            devices.ProductSupport.Status = 'Delayed'
        if devices.ProductSupport.Task18_End_Date and Task18_delta < timedelta(0)and not devices.ProductSupport.Task18_complete_date:
            devices.ProductSupport.Task18_alert = True
            devices.ProductSupport.Status = 'Delayed'
        if devices.ProductSupport.Task19_End_Date and Task19_delta < timedelta(0)and not devices.ProductSupport.Task19_complete_date:
            devices.ProductSupport.Task19_alert = True
            devices.ProductSupport.Status = 'Delayed'
        if devices.ProductSupport.Task20_End_Date and Task20_delta < timedelta(0)and not devices.ProductSupport.Task20_complete_date:
            devices.ProductSupport.Task20_alert = True
            devices.ProductSupport.Status = 'Delayed'

        devices.ProductSupport.completed = int(percent)
        devices.ProductSupport.save()
        posts1 = devices.ProductSupport.task1statusproductsupport_set.all().order_by('-created')
        posts2 = devices.ProductSupport.task2statusproductsupport_set.all().order_by('-created')
        posts3 = devices.ProductSupport.task3statusproductsupport_set.all().order_by('-created')
        posts4 = devices.ProductSupport.task4statusproductsupport_set.all().order_by('-created')
        posts5 = devices.ProductSupport.task5statusproductsupport_set.all().order_by('-created')
        posts6 = devices.ProductSupport.task6statusproductsupport_set.all().order_by('-created')
        posts7 = devices.ProductSupport.task7statusproductsupport_set.all().order_by('-created')
        posts8 = devices.ProductSupport.task8statusproductsupport_set.all().order_by('-created')
        posts9 = devices.ProductSupport.task9statusproductsupport_set.all().order_by('-created')
        posts10 = devices.ProductSupport.task10statusproductsupport_set.all().order_by('-created')
        posts11 = devices.ProductSupport.task11statusproductsupport_set.all().order_by('-created')
        posts12 = devices.ProductSupport.task12statusproductsupport_set.all().order_by('-created')
        posts13 = devices.ProductSupport.task13statusproductsupport_set.all().order_by('-created')
        posts14 = devices.ProductSupport.task14statusproductsupport_set.all().order_by('-created')
        posts15 = devices.ProductSupport.task15statusproductsupport_set.all().order_by('-created')
        posts16 = devices.ProductSupport.task16statusproductsupport_set.all().order_by('-created')
        posts17 = devices.ProductSupport.task17statusproductsupport_set.all().order_by('-created')
        posts18 = devices.ProductSupport.task18statusproductsupport_set.all().order_by('-created')
        posts19 = devices.ProductSupport.task19statusproductsupport_set.all().order_by('-created')
        posts20 = devices.ProductSupport.task20statusproductsupport_set.all().order_by('-created')

        args = {'devices':devices, 'form1':form1, 'form2':form2, 'form3':form3, 'form4':form4, 'form5':form5, 'form6':form6,
                'form7': form7, 'form8':form8, 'form9':form9, 'form10':form10, 'form11':form11, 'form12':form12, 'form13':form13,
                'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17, 'form18': form18, 'form19': form19,
                'form20': form20, 'posts1':posts1, 'posts2':posts2, 'posts3':posts3, 'posts4':posts4, 'posts5':posts5, 'posts6':posts6,
                'posts7': posts7, 'posts8':posts8, 'posts9':posts9, 'posts10':posts10, 'posts11':posts11, 'posts12':posts12, 'posts13':posts13,
                'posts14': posts14, 'posts15': posts15, 'posts16': posts16, 'posts17': posts17, 'posts18': posts18, 'posts19': posts19,
                'posts20': posts20, 'Task1_vc_dateform':Task1_vc_dateform, 'Task2_vc_dateform':Task2_vc_dateform,
                'Task3_vc_dateform':Task3_vc_dateform, 'Task4_vc_dateform':Task4_vc_dateform,
                'Task5_vc_dateform': Task5_vc_dateform, 'Task6_vc_dateform': Task6_vc_dateform,
                'Task7_vc_dateform': Task7_vc_dateform, 'Task8_vc_dateform': Task8_vc_dateform,
                'Task9_vc_dateform': Task9_vc_dateform, 'Task10_vc_dateform': Task10_vc_dateform,
                'Task11_vc_dateform': Task11_vc_dateform, 'Task12_vc_dateform': Task12_vc_dateform,
                'Task13_vc_dateform': Task13_vc_dateform, 'Task14_vc_dateform': Task14_vc_dateform,
                'Task15_vc_dateform': Task15_vc_dateform, 'Task16_vc_dateform': Task16_vc_dateform,
                'Task17_vc_dateform': Task17_vc_dateform, 'Task18_vc_dateform': Task18_vc_dateform,
                'Task19_vc_dateform': Task19_vc_dateform, 'Task20_vc_dateform': Task20_vc_dateform,
                'Task1_delta':Task1_delta, 'Task7_delta':Task7_delta, 'Task12_delta':Task12_delta, 'Task17_delta':Task17_delta,
                'Task2_delta': Task2_delta, 'Task8_delta': Task8_delta, 'Task13_delta': Task13_delta,
                'Task3_delta': Task3_delta, 'Task9_delta':Task9_delta, 'Task14_delta':Task14_delta, 'Task18_delta':Task18_delta,
                'Task4_delta':Task4_delta, 'Task10_delta':Task10_delta, 'Task15_delta':Task15_delta, 'Task19_delta':Task19_delta,
                'Task5_delta':Task5_delta, 'Task11_delta':Task11_delta, 'Task16_delta':Task16_delta, 'Task20_delta':Task20_delta,
                'Task6_delta':Task6_delta,
                }
        return render(request,self.template_name,args)

    def post(self, request, pk):

        form1 = Task1_ps_form(request.POST)
        form2 = Task2_ps_form(request.POST)
        form3 = Task3_ps_form(request.POST)
        form4 = Task4_ps_form(request.POST)
        form5 = Task5_ps_form(request.POST)
        form6 = Task6_ps_form(request.POST)
        form7 = Task7_ps_form(request.POST)
        form8 = Task8_ps_form(request.POST)
        form9 = Task9_ps_form(request.POST)
        form10 = Task10_ps_form(request.POST)
        form11 = Task11_ps_form(request.POST)
        form12 = Task12_ps_form(request.POST)
        form13 = Task13_ps_form(request.POST)
        form14 = Task14_ps_form(request.POST)
        form15 = Task15_ps_form(request.POST)
        form16 = Task16_ps_form(request.POST)
        form17 = Task17_ps_form(request.POST)
        form18 = Task18_ps_form(request.POST)
        form19 = Task19_ps_form(request.POST)
        form20 = Task20_ps_form(request.POST)
        devices = Device.objects.get(pk=pk)

        Task1_vc_dateform = Task1_ps_date_form(request.POST,instance=devices.ProductSupport)
        Task2_vc_dateform = Task2_ps_date_form(request.POST,instance=devices.ProductSupport)
        Task3_vc_dateform = Task3_ps_date_form(request.POST,instance=devices.ProductSupport)
        Task4_vc_dateform = Task4_ps_date_form(request.POST,instance=devices.ProductSupport)
        Task5_vc_dateform = Task5_ps_date_form(request.POST,instance=devices.ProductSupport)
        Task6_vc_dateform = Task6_ps_date_form(request.POST,instance=devices.ProductSupport)
        Task7_vc_dateform = Task7_ps_date_form(request.POST,instance=devices.ProductSupport)
        Task8_vc_dateform = Task8_ps_date_form(request.POST,instance=devices.ProductSupport)
        Task9_vc_dateform = Task9_ps_date_form(request.POST,instance=devices.ProductSupport)
        Task10_vc_dateform = Task10_ps_date_form(request.POST,instance=devices.ProductSupport)
        Task11_vc_dateform = Task11_ps_date_form(request.POST,instance=devices.ProductSupport)
        Task12_vc_dateform = Task12_ps_date_form(request.POST,instance=devices.ProductSupport)
        Task13_vc_dateform = Task13_ps_date_form(request.POST,instance=devices.ProductSupport)
        Task14_vc_dateform = Task14_ps_date_form(request.POST,instance=devices.ProductSupport)
        Task15_vc_dateform = Task15_ps_date_form(request.POST,instance=devices.ProductSupport)
        Task16_vc_dateform = Task16_ps_date_form(request.POST,instance=devices.ProductSupport)
        Task17_vc_dateform = Task17_ps_date_form(request.POST,instance=devices.ProductSupport)
        Task18_vc_dateform = Task18_ps_date_form(request.POST,instance=devices.ProductSupport)
        Task19_vc_dateform = Task19_ps_date_form(request.POST,instance=devices.ProductSupport)
        Task20_vc_dateform = Task20_ps_date_form(request.POST,instance=devices.ProductSupport)

        if 'Task1Submit' in request.POST:
            if form1.is_valid() and Task1_vc_dateform.is_valid():
                post = form1.save(commit=False)
                post.user = request.user
                post.ProductSupport = devices.ProductSupport
                Task1_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk + '/productsupport')
            else:
                return redirect('/login/summary/' + pk + '/productsupport')
        elif 'Task2Submit' in request.POST:
            if form2.is_valid() and Task2_vc_dateform.is_valid():
                post = form2.save(commit=False)
                post.user = request.user
                post.ProductSupport = devices.ProductSupport
                Task2_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/productsupport')
            else:
                return redirect('/login/summary/' + pk + '/productsupport')
        elif 'Task3Submit' in request.POST:
            if form3.is_valid() and Task3_vc_dateform.is_valid():
                post = form3.save(commit=False)
                post.user = request.user
                post.ProductSupport = devices.ProductSupport
                Task3_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/productsupport')
            else:
                return redirect('/login/summary/' + pk + '/productsupport')
        elif 'Task4Submit' in request.POST:
            if form4.is_valid() and Task4_vc_dateform.is_valid():
                post = form4.save(commit=False)
                post.user = request.user
                post.ProductSupport = devices.ProductSupport
                Task4_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/productsupport')
            else:
                return redirect('/login/summary/' + pk + '/productsupport')
        elif 'Task5Submit' in request.POST:
            if form5.is_valid() and Task5_vc_dateform.is_valid():
                post = form5.save(commit=False)
                post.user = request.user
                post.ProductSupport = devices.ProductSupport
                Task5_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/productsupport')
            else:
                return redirect('/login/summary/' + pk + '/productsupport')
        elif 'Task6Submit' in request.POST:
            if form6.is_valid() and Task6_vc_dateform.is_valid():
                post = form6.save(commit=False)
                post.user = request.user
                post.ProductSupport = devices.ProductSupport
                Task6_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/productsupport')
            else:
                return redirect('/login/summary/' + pk + '/productsupport')
        elif 'Task7Submit' in request.POST:
            if form7.is_valid() and Task7_vc_dateform.is_valid():
                post = form7.save(commit=False)
                post.user = request.user
                post.ProductSupport = devices.ProductSupport
                Task7_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/productsupport')
            else:
                return redirect('/login/summary/' + pk + '/productsupport')
        elif 'Task8Submit' in request.POST:
            if form8.is_valid() and Task8_vc_dateform.is_valid():
                post = form8.save(commit=False)
                post.user = request.user
                post.ProductSupport = devices.ProductSupport
                Task8_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/productsupport')
            else:
                return redirect('/login/summary/' + pk + '/productsupport')
        elif 'Task9Submit' in request.POST:
            if form9.is_valid() and Task9_vc_dateform.is_valid():
                post = form9.save(commit=False)
                post.user = request.user
                post.ProductSupport = devices.ProductSupport
                Task9_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/productsupport')
            else:
                return redirect('/login/summary/' + pk + '/productsupport')
        elif 'Task10Submit' in request.POST:
            if form10.is_valid() and Task10_vc_dateform.is_valid():
                post = form10.save(commit=False)
                post.user = request.user
                post.ProductSupport = devices.ProductSupport
                Task10_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/productsupport')
            else:
                return redirect('/login/summary/' + pk + '/productsupport')
        elif 'Task11Submit' in request.POST:
            if form11.is_valid() and Task11_vc_dateform.is_valid():
                post = form11.save(commit=False)
                post.user = request.user
                post.ProductSupport = devices.ProductSupport
                Task11_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/productsupport')
            else:
                return redirect('/login/summary/' + pk + '/productsupport')
        elif 'Task12Submit' in request.POST:
            if form12.is_valid() and Task12_vc_dateform.is_valid():
                post = form12.save(commit=False)
                post.user = request.user
                post.ProductSupport = devices.ProductSupport
                Task12_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/productsupport')
            else:
                return redirect('/login/summary/' + pk + '/productsupport')
        elif 'Task13Submit' in request.POST:
            if form13.is_valid() and Task13_vc_dateform.is_valid():
                post = form13.save(commit=False)
                post.user = request.user
                post.ProductSupport = devices.ProductSupport
                Task13_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/productsupport')
            else:
                return redirect('/login/summary/' + pk + '/productsupport')
        elif 'Task14Submit' in request.POST:
            if form14.is_valid() and Task14_vc_dateform.is_valid():
                post = form14.save(commit=False)
                post.user = request.user
                post.ProductSupport = devices.ProductSupport
                Task14_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/productsupport')
            else:
                return redirect('/login/summary/' + pk + '/productsupport')
        elif 'Task15Submit' in request.POST:
            if form15.is_valid() and Task15_vc_dateform.is_valid():
                post = form15.save(commit=False)
                post.user = request.user
                post.ProductSupport = devices.ProductSupport
                Task15_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/productsupport')
            else:
                return redirect('/login/summary/' + pk + '/productsupport')
        elif 'Task16Submit' in request.POST:
            if form16.is_valid() and Task16_vc_dateform.is_valid():
                post = form16.save(commit=False)
                post.user = request.user
                post.ProductSupport = devices.ProductSupport
                Task16_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/productsupport')
            else:
                return redirect('/login/summary/' + pk + '/productsupport')
        elif 'Task17Submit' in request.POST:
            if form17.is_valid() and Task17_vc_dateform.is_valid():
                post = form17.save(commit=False)
                post.user = request.user
                post.ProductSupport = devices.ProductSupport
                Task17_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/productsupport')
            else:
                return redirect('/login/summary/' + pk + '/productsupport')
        elif 'Task18Submit' in request.POST:
            if form18.is_valid() and Task18_vc_dateform.is_valid():
                post = form18.save(commit=False)
                post.user = request.user
                post.ProductSupport = devices.ProductSupport
                Task18_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/productsupport')
            else:
                return redirect('/login/summary/' + pk + '/productsupport')
        elif 'Task19Submit' in request.POST:
            if form19.is_valid() and Task19_vc_dateform.is_valid():
                post = form19.save(commit=False)
                post.user = request.user
                post.ProductSupport = devices.ProductSupport
                Task19_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/productsupport')
            else:
                return redirect('/login/summary/' + pk + '/productsupport')
        elif 'Task20Submit' in request.POST:
            if form20.is_valid() and Task20_vc_dateform.is_valid():
                post = form20.save(commit=False)
                post.user = request.user
                post.ProductSupport = devices.ProductSupport
                Task20_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/productsupport')
            else:
                return redirect('/login/summary/' + pk + '/productsupport')

########################################################################################################################

class WarehouseView(LoginRequiredMixin,TemplateView):
    template_name = 'login/device7.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        form1 = Task1_w_form()
        form2 = Task2_w_form()
        form3 = Task3_w_form()
        form4 = Task4_w_form()
        form5 = Task5_w_form()
        form6 = Task6_w_form()
        form7 = Task7_w_form()
        form8 = Task8_w_form()
        form9 = Task9_w_form()
        form10 = Task10_w_form()
        form11 = Task11_w_form()
        form12 = Task12_w_form()
        form13 = Task13_w_form()
        form14 = Task14_w_form()
        form15 = Task15_w_form()
        form16 = Task16_w_form()
        form17 = Task17_w_form()
        form18 = Task18_w_form()
        form19 = Task19_w_form()
        form20 = Task20_w_form()
        devices = Device.objects.get(pk=pk)
        Task1_vc_dateform = Task1_w_date_form(instance=devices.Warehouse)
        Task2_vc_dateform = Task2_w_date_form(instance=devices.Warehouse)
        Task3_vc_dateform = Task3_w_date_form(instance=devices.Warehouse)
        Task4_vc_dateform = Task4_w_date_form(instance=devices.Warehouse)
        Task5_vc_dateform = Task5_w_date_form(instance=devices.Warehouse)
        Task6_vc_dateform = Task6_w_date_form(instance=devices.Warehouse)
        Task7_vc_dateform = Task7_w_date_form(instance=devices.Warehouse)
        Task8_vc_dateform = Task8_w_date_form(instance=devices.Warehouse)
        Task9_vc_dateform = Task9_w_date_form(instance=devices.Warehouse)
        Task10_vc_dateform = Task10_w_date_form(instance=devices.Warehouse)
        Task11_vc_dateform = Task11_w_date_form(instance=devices.Warehouse)
        Task12_vc_dateform = Task12_w_date_form(instance=devices.Warehouse)
        Task13_vc_dateform = Task13_w_date_form(instance=devices.Warehouse)
        Task14_vc_dateform = Task14_w_date_form(instance=devices.Warehouse)
        Task15_vc_dateform = Task15_w_date_form(instance=devices.Warehouse)
        Task16_vc_dateform = Task16_w_date_form(instance=devices.Warehouse)
        Task17_vc_dateform = Task17_w_date_form(instance=devices.Warehouse)
        Task18_vc_dateform = Task18_w_date_form(instance=devices.Warehouse)
        Task19_vc_dateform = Task19_w_date_form(instance=devices.Warehouse)
        Task20_vc_dateform = Task20_w_date_form(instance=devices.Warehouse)

        #Calculating % completed
        y=0
        if devices.Warehouse.Task1_Name:
            y=y+1
        if devices.Warehouse.Task2_Name:
            y=y+1
        if devices.Warehouse.Task3_Name:
            y=y+1
        if devices.Warehouse.Task4_Name:
            y=y+1
        if devices.Warehouse.Task5_Name:
            y=y+1
        if devices.Warehouse.Task6_Name:
            y=y+1
        if devices.Warehouse.Task7_Name:
            y=y+1
        if devices.Warehouse.Task8_Name:
            y=y+1
        if devices.Warehouse.Task9_Name:
            y=y+1
        if devices.Warehouse.Task10_Name:
            y=y+1
        if devices.Warehouse.Task11_Name:
            y=y+1
        if devices.Warehouse.Task12_Name:
            y=y+1
        if devices.Warehouse.Task13_Name:
            y=y+1
        if devices.Warehouse.Task14_Name:
            y=y+1
        if devices.Warehouse.Task15_Name:
            y=y+1
        if devices.Warehouse.Task16_Name:
            y=y+1
        if devices.Warehouse.Task17_Name:
            y=y+1
        if devices.Warehouse.Task18_Name:
            y=y+1
        if devices.Warehouse.Task19_Name:
            y=y+1
        if devices.Warehouse.Task20_Name:
            y=y+1


        x = 0
        if devices.Warehouse.Task1_complete_date:
            x =x+1
            devices.Warehouse.Task1_alert = False
            devices.Warehouse.Task1_warning=False
            devices.Warehouse.Status='On_Time'
        if devices.Warehouse.Task2_complete_date:
            x = x + 1
            devices.Warehouse.Task2_alert = False
            devices.Warehouse.Task2_warning=False
            devices.Warehouse.Status = 'On_Time'
        if devices.Warehouse.Task3_complete_date:
            x = x + 1
            devices.Warehouse.Task3_alert = False
            devices.Warehouse.Task3_warning=False
            devices.Warehouse.Status = 'On_Time'
        if devices.Warehouse.Task4_complete_date:
            x = x + 1
            devices.Warehouse.Task4_alert = False
            devices.Warehouse.Task4_warning=False
            devices.Warehouse.Status = 'On_Time'
        if devices.Warehouse.Task5_complete_date:
            x = x + 1
            devices.Warehouse.Task5_alert = False
            devices.Warehouse.Task5_warning=False
            devices.Warehouse.Status = 'On_Time'
        if devices.Warehouse.Task6_complete_date:
            x = x + 1
            devices.Warehouse.Task6_alert = False
            devices.Warehouse.Task6_warning=False
            devices.Warehouse.Status = 'On_Time'
        if devices.Warehouse.Task7_complete_date:
            x =x+1
            devices.Warehouse.Task7_alert = False
            devices.Warehouse.Task7_warning=False
            devices.Warehouse.Status = 'On_Time'
        if devices.Warehouse.Task8_complete_date:
            x =x+1
            devices.Warehouse.Task8_alert = False
            devices.Warehouse.Task8_warning=False
            devices.Warehouse.Status = 'On_Time'
        if devices.Warehouse.Task9_complete_date:
            x =x+1
            devices.Warehouse.Task9_alert = False
            devices.Warehouse.Task9_warning=False
            devices.Warehouse.Status = 'On_Time'
        if devices.Warehouse.Task10_complete_date:
            x =x+1
            devices.Warehouse.Task10_alert = False
            devices.Warehouse.Task10_warning=False
            devices.Warehouse.Status = 'On_Time'
        if devices.Warehouse.Task11_complete_date:
            x =x+1
            devices.Warehouse.Task11_alert = False
            devices.Warehouse.Task11_warning=False
            devices.Warehouse.Status = 'On_Time'
        if devices.Warehouse.Task12_complete_date:
            x = x + 1
            devices.Warehouse.Task12_alert = False
            devices.Warehouse.Task12_warning=False
            devices.Warehouse.Status = 'On_Time'
        if devices.Warehouse.Task13_complete_date:
            x = x + 1
            devices.Warehouse.Task13_alert = False
            devices.Warehouse.Task13_warning=False
            devices.Warehouse.Status = 'On_Time'
        if devices.Warehouse.Task14_complete_date:
            x = x + 1
            devices.Warehouse.Task14_alert = False
            devices.Warehouse.Task14_warning=False
            devices.Warehouse.Status = 'On_Time'
        if devices.Warehouse.Task15_complete_date:
            x = x + 1
            devices.Warehouse.Task15_alert = False
            devices.Warehouse.Task15_warning=False
            devices.Warehouse.Status = 'On_Time'
        if devices.Warehouse.Task16_complete_date:
            x = x + 1
            devices.Warehouse.Task16_alert = False
            devices.Warehouse.Task16_warning=False
            devices.Warehouse.Status = 'On_Time'
        if devices.Warehouse.Task17_complete_date:
            x =x+1
            devices.Warehouse.Task17_alert = False
            devices.Warehouse.Task17_warning=False
            devices.Warehouse.Status = 'On_Time'
        if devices.Warehouse.Task18_complete_date:
            x =x+1
            devices.Warehouse.Task18_alert = False
            devices.Warehouse.Task18_warning=False
            devices.Warehouse.Status = 'On_Time'
        if devices.Warehouse.Task19_complete_date:
            x =x+1
            devices.Warehouse.Task19_alert = False
            devices.Warehouse.Task19_warning=False
            devices.Warehouse.Status = 'On_Time'
        if devices.Warehouse.Task20_complete_date:
            x =x+1
            devices.Warehouse.Task20_alert = False
            devices.Warehouse.Task20_warning=False
            devices.Warehouse.Status = 'On_Time'
        percent = x/y * 100
        print (percent)

        #alerting logic
        today = datetime.date.today()
        if devices.Warehouse.Task1_End_Date:
            Task1_delta =  devices.Warehouse.Task1_End_Date - today
        else:
            Task1_delta = None
        if devices.Warehouse.Task2_End_Date:
            Task2_delta = devices.Warehouse.Task2_End_Date - today
        else:
            Task2_delta = None
        if devices.Warehouse.Task3_End_Date:
            Task3_delta = devices.Warehouse.Task3_End_Date - today
        else:
            Task3_delta = None
        if devices.Warehouse.Task4_End_Date:
            Task4_delta = devices.Warehouse.Task4_End_Date - today
        else:
            Task4_delta = None
        if devices.Warehouse.Task5_End_Date:
            Task5_delta = devices.Warehouse.Task5_End_Date - today
        else:
            Task5_delta = None
        if devices.Warehouse.Task6_End_Date:
            Task6_delta = devices.Warehouse.Task6_End_Date - today
        else:
            Task6_delta = None
        if devices.Warehouse.Task7_End_Date:
            Task7_delta = devices.Warehouse.Task7_End_Date - today
        else:
            Task7_delta = None
        if devices.Warehouse.Task8_End_Date:
            Task8_delta = devices.Warehouse.Task8_End_Date - today
        else:
            Task8_delta = None
        if devices.Warehouse.Task9_End_Date:
            Task9_delta = devices.Warehouse.Task9_End_Date - today
        else:
            Task9_delta = None
        if devices.Warehouse.Task10_End_Date:
            Task10_delta =  devices.Warehouse.Task10_End_Date - today
        else:
            Task10_delta = None
        if devices.Warehouse.Task11_End_Date:
            Task11_delta =  devices.Warehouse.Task11_End_Date - today
        else:
            Task11_delta = None
        if devices.Warehouse.Task12_End_Date:
            Task12_delta = devices.Warehouse.Task12_End_Date - today
        else:
            Task12_delta = None
        if devices.Warehouse.Task13_End_Date:
            Task13_delta = devices.Warehouse.Task13_End_Date - today
        else:
            Task13_delta = None
        if devices.Warehouse.Task14_End_Date:
            Task14_delta = devices.Warehouse.Task14_End_Date - today
        else:
            Task14_delta = None
        if devices.Warehouse.Task15_End_Date:
            Task15_delta = devices.Warehouse.Task15_End_Date - today
        else:
            Task15_delta = None
        if devices.Warehouse.Task16_End_Date:
            Task16_delta = devices.Warehouse.Task16_End_Date - today
        else:
            Task16_delta = None
        if devices.Warehouse.Task17_End_Date:
            Task17_delta = devices.Warehouse.Task17_End_Date - today
        else:
            Task17_delta = None
        if devices.Warehouse.Task18_End_Date:
            Task18_delta = devices.Warehouse.Task18_End_Date - today
        else:
            Task18_delta = None
        if devices.Warehouse.Task19_End_Date:
            Task19_delta = devices.Warehouse.Task19_End_Date - today
        else:
            Task19_delta = None
        if devices.Warehouse.Task20_End_Date:
            Task20_delta = devices.Warehouse.Task20_End_Date - today
        else:
            Task20_delta = None

        if Task1_delta and Task1_delta < timedelta(devices.Warehouse.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not devices.Warehouse.Task1_complete_date:
            devices.Warehouse.Task1_warning = True
            devices.Warehouse.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(devices.Warehouse.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not devices.Warehouse.Task2_complete_date:
            devices.Warehouse.Task2_warning = True
            devices.Warehouse.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(devices.Warehouse.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not devices.Warehouse.Task3_complete_date:
            devices.Warehouse.Task3_warning = True
            devices.Warehouse.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(devices.Warehouse.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not devices.Warehouse.Task4_complete_date:
            devices.Warehouse.Task4_warning = True
            devices.Warehouse.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(devices.Warehouse.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not devices.Warehouse.Task5_complete_date:
            devices.Warehouse.Task5_warning = True
            devices.Warehouse.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(devices.Warehouse.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not devices.Warehouse.Task6_complete_date:
            devices.Warehouse.Task6_warning = True
            devices.Warehouse.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(devices.Warehouse.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not devices.Warehouse.Task7_complete_date:
            devices.Warehouse.Task7_warning = True
            devices.Warehouse.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(devices.Warehouse.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not devices.Warehouse.Task8_complete_date:
            devices.Warehouse.Task8_warning = True
            devices.Warehouse.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(devices.Warehouse.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not devices.Warehouse.Task9_complete_date:
            devices.Warehouse.Task9_warning = True
            devices.Warehouse.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(devices.Warehouse.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not devices.Warehouse.Task10_complete_date:
            devices.Warehouse.Task10_warning = True
            devices.Warehouse.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(devices.Warehouse.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not devices.Warehouse.Task11_complete_date:
            devices.Warehouse.Task11_warning = True
            devices.Warehouse.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(devices.Warehouse.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not devices.Warehouse.Task12_complete_date:
            devices.Warehouse.Task12_warning = True
            devices.Warehouse.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(devices.Warehouse.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not devices.Warehouse.Task13_complete_date:
            devices.Warehouse.Task13_warning = True
            devices.Warehouse.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(devices.Warehouse.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not devices.Warehouse.Task14_complete_date:
            devices.Warehouse.Task14_warning = True
            devices.Warehouse.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(devices.Warehouse.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not devices.Warehouse.Task15_complete_date:
            devices.Warehouse.Task15_warning = True
            devices.Warehouse.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(devices.Warehouse.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not devices.Warehouse.Task16_complete_date:
            devices.Warehouse.Task16_warning = True
            devices.Warehouse.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(devices.Warehouse.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not devices.Warehouse.Task17_complete_date:
            devices.Warehouse.Task17_warning = True
            devices.Warehouse.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(devices.Warehouse.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not devices.Warehouse.Task18_complete_date:
            devices.Warehouse.Task18_warning = True
            devices.Warehouse.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(devices.Warehouse.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not devices.Warehouse.Task19_complete_date:
            devices.Warehouse.Task19_warning = True
            devices.Warehouse.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(devices.Warehouse.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not devices.Warehouse.Task20_complete_date:
            devices.Warehouse.Task20_warning = True
            devices.Warehouse.Status = 'At Risk'


        if devices.Warehouse.Task1_End_Date and Task1_delta < timedelta(0) and not devices.Warehouse.Task1_complete_date:
            devices.Warehouse.Task1_alert = True
            devices.Warehouse.Status = 'Delayed'
        if devices.Warehouse.Task2_End_Date and Task2_delta < timedelta(0) and not devices.Warehouse.Task2_complete_date:
            devices.Warehouse.Task2_alert = True
            devices.Warehouse.Status = 'Delayed'
        if devices.Warehouse.Task3_End_Date and Task3_delta < timedelta(0) and not devices.Warehouse.Task3_complete_date:
            devices.Warehouse.Task3_alert = True
            devices.Warehouse.Status = 'Delayed'
        if devices.Warehouse.Task4_End_Date and Task4_delta < timedelta(0) and not devices.Warehouse.Task4_complete_date:
            devices.Warehouse.Task4_alert = True
            devices.Warehouse.Status = 'Delayed'
        if devices.Warehouse.Task5_End_Date and Task5_delta < timedelta(0) and not devices.Warehouse.Task5_complete_date:
            devices.Warehouse.Task5_alert = True
            devices.Warehouse.Status = 'Delayed'
        if devices.Warehouse.Task6_End_Date and Task6_delta < timedelta(0) and not devices.Warehouse.Task6_complete_date:
            devices.Warehouse.Task6_alert = True
            devices.Warehouse.Status = 'Delayed'
        if devices.Warehouse.Task7_End_Date and Task7_delta < timedelta(0) and not devices.Warehouse.Task7_complete_date:
            devices.Warehouse.Task7_alert = True
            devices.Warehouse.Status = 'Delayed'
        if devices.Warehouse.Task8_End_Date and Task8_delta < timedelta(0)and not devices.Warehouse.Task8_complete_date:
            devices.Warehouse.Task8_alert = True
            devices.Warehouse.Status = 'Delayed'
        if devices.Warehouse.Task9_End_Date and Task9_delta < timedelta(0)and not devices.Warehouse.Task9_complete_date:
            devices.Warehouse.Task9_alert = True
            devices.Warehouse.Status = 'Delayed'
        if devices.Warehouse.Task10_End_Date and Task10_delta < timedelta(0) and not devices.Warehouse.Task10_complete_date:
            devices.Warehouse.Task10_alert = True
            devices.Warehouse.Status = 'Delayed'
        if devices.Warehouse.Task11_End_Date and Task11_delta < timedelta(0) and not devices.Warehouse.Task11_complete_date:
            devices.Warehouse.Task11_alert = True
            devices.Warehouse.Status = 'Delayed'
        if devices.Warehouse.Task12_End_Date and Task12_delta < timedelta(0) and not devices.Warehouse.Task12_complete_date:
            devices.Warehouse.Task12_alert = True
            devices.Warehouse.Status = 'Delayed'
        if devices.Warehouse.Task13_End_Date and Task13_delta < timedelta(0) and not devices.Warehouse.Task13_complete_date:
            devices.Warehouse.Task13_alert = True
            devices.Warehouse.Status = 'Delayed'
        if devices.Warehouse.Task14_End_Date and Task14_delta < timedelta(0) and not devices.Warehouse.Task14_complete_date:
            devices.Warehouse.Task14_alert = True
            devices.Warehouse.Status = 'Delayed'
        if devices.Warehouse.Task15_End_Date and Task15_delta < timedelta(0) and not devices.Warehouse.Task15_complete_date:
            devices.Warehouse.Task15_alert = True
            devices.Warehouse.Status = 'Delayed'
        if devices.Warehouse.Task16_End_Date and Task16_delta < timedelta(0) and not devices.Warehouse.Task16_complete_date:
            devices.Warehouse.Task16_alert = True
            devices.Warehouse.Status = 'Delayed'
        if devices.Warehouse.Task17_End_Date and Task17_delta < timedelta(0)and not devices.Warehouse.Task17_complete_date:
            devices.Warehouse.Task17_alert = True
            devices.Warehouse.Status = 'Delayed'
        if devices.Warehouse.Task18_End_Date and Task18_delta < timedelta(0)and not devices.Warehouse.Task18_complete_date:
            devices.Warehouse.Task18_alert = True
            devices.Warehouse.Status = 'Delayed'
        if devices.Warehouse.Task19_End_Date and Task19_delta < timedelta(0)and not devices.Warehouse.Task19_complete_date:
            devices.Warehouse.Task19_alert = True
            devices.Warehouse.Status = 'Delayed'
        if devices.Warehouse.Task20_End_Date and Task20_delta < timedelta(0)and not devices.Warehouse.Task20_complete_date:
            devices.Warehouse.Task20_alert = True
            devices.Warehouse.Status = 'Delayed'

        devices.Warehouse.completed = int(percent)
        devices.Warehouse.save()
        posts1 = devices.Warehouse.task1statuswarehouse_set.all().order_by('-created')
        posts2 = devices.Warehouse.task2statuswarehouse_set.all().order_by('-created')
        posts3 = devices.Warehouse.task3statuswarehouse_set.all().order_by('-created')
        posts4 = devices.Warehouse.task4statuswarehouse_set.all().order_by('-created')
        posts5 = devices.Warehouse.task5statuswarehouse_set.all().order_by('-created')
        posts6 = devices.Warehouse.task6statuswarehouse_set.all().order_by('-created')
        posts7 = devices.Warehouse.task7statuswarehouse_set.all().order_by('-created')
        posts8 = devices.Warehouse.task8statuswarehouse_set.all().order_by('-created')
        posts9 = devices.Warehouse.task9statuswarehouse_set.all().order_by('-created')
        posts10 = devices.Warehouse.task10statuswarehouse_set.all().order_by('-created')
        posts11 = devices.Warehouse.task11statuswarehouse_set.all().order_by('-created')
        posts12 = devices.Warehouse.task12statuswarehouse_set.all().order_by('-created')
        posts13 = devices.Warehouse.task13statuswarehouse_set.all().order_by('-created')
        posts14 = devices.Warehouse.task14statuswarehouse_set.all().order_by('-created')
        posts15 = devices.Warehouse.task15statuswarehouse_set.all().order_by('-created')
        posts16 = devices.Warehouse.task16statuswarehouse_set.all().order_by('-created')
        posts17 = devices.Warehouse.task17statuswarehouse_set.all().order_by('-created')
        posts18 = devices.Warehouse.task18statuswarehouse_set.all().order_by('-created')
        posts19 = devices.Warehouse.task19statuswarehouse_set.all().order_by('-created')
        posts20 = devices.Warehouse.task20statuswarehouse_set.all().order_by('-created')

        args = {'devices':devices, 'form1':form1, 'form2':form2, 'form3':form3, 'form4':form4, 'form5':form5, 'form6':form6,
                'form7': form7, 'form8':form8, 'form9':form9, 'form10':form10, 'form11':form11, 'form12':form12, 'form13':form13,
                'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17, 'form18': form18, 'form19': form19,
                'form20': form20, 'posts1':posts1, 'posts2':posts2, 'posts3':posts3, 'posts4':posts4, 'posts5':posts5, 'posts6':posts6,
                'posts7': posts7, 'posts8':posts8, 'posts9':posts9, 'posts10':posts10, 'posts11':posts11, 'posts12':posts12, 'posts13':posts13,
                'posts14': posts14, 'posts15': posts15, 'posts16': posts16, 'posts17': posts17, 'posts18': posts18, 'posts19': posts19,
                'posts20': posts20, 'Task1_vc_dateform':Task1_vc_dateform, 'Task2_vc_dateform':Task2_vc_dateform,
                'Task3_vc_dateform':Task3_vc_dateform, 'Task4_vc_dateform':Task4_vc_dateform,
                'Task5_vc_dateform': Task5_vc_dateform, 'Task6_vc_dateform': Task6_vc_dateform,
                'Task7_vc_dateform': Task7_vc_dateform, 'Task8_vc_dateform': Task8_vc_dateform,
                'Task9_vc_dateform': Task9_vc_dateform, 'Task10_vc_dateform': Task10_vc_dateform,
                'Task11_vc_dateform': Task11_vc_dateform, 'Task12_vc_dateform': Task12_vc_dateform,
                'Task13_vc_dateform': Task13_vc_dateform, 'Task14_vc_dateform': Task14_vc_dateform,
                'Task15_vc_dateform': Task15_vc_dateform, 'Task16_vc_dateform': Task16_vc_dateform,
                'Task17_vc_dateform': Task17_vc_dateform, 'Task18_vc_dateform': Task18_vc_dateform,
                'Task19_vc_dateform': Task19_vc_dateform, 'Task20_vc_dateform': Task20_vc_dateform,
                'Task1_delta':Task1_delta, 'Task7_delta':Task7_delta, 'Task12_delta':Task12_delta, 'Task17_delta':Task17_delta,
                'Task2_delta': Task2_delta, 'Task8_delta': Task8_delta, 'Task13_delta': Task13_delta,
                'Task3_delta': Task3_delta, 'Task9_delta':Task9_delta, 'Task14_delta':Task14_delta, 'Task18_delta':Task18_delta,
                'Task4_delta':Task4_delta, 'Task10_delta':Task10_delta, 'Task15_delta':Task15_delta, 'Task19_delta':Task19_delta,
                'Task5_delta':Task5_delta, 'Task11_delta':Task11_delta, 'Task16_delta':Task16_delta, 'Task20_delta':Task20_delta,
                'Task6_delta':Task6_delta,
                }
        return render(request,self.template_name,args)

    def post(self, request, pk):

        form1 = Task1_w_form(request.POST)
        form2 = Task2_w_form(request.POST)
        form3 = Task3_w_form(request.POST)
        form4 = Task4_w_form(request.POST)
        form5 = Task5_w_form(request.POST)
        form6 = Task6_w_form(request.POST)
        form7 = Task7_w_form(request.POST)
        form8 = Task8_w_form(request.POST)
        form9 = Task9_w_form(request.POST)
        form10 = Task10_w_form(request.POST)
        form11 = Task11_w_form(request.POST)
        form12 = Task12_w_form(request.POST)
        form13 = Task13_w_form(request.POST)
        form14 = Task14_w_form(request.POST)
        form15 = Task15_w_form(request.POST)
        form16 = Task16_w_form(request.POST)
        form17 = Task17_w_form(request.POST)
        form18 = Task18_w_form(request.POST)
        form19 = Task19_w_form(request.POST)
        form20 = Task20_w_form(request.POST)
        devices = Device.objects.get(pk=pk)

        Task1_vc_dateform = Task1_w_date_form(request.POST,instance=devices.Warehouse)
        Task2_vc_dateform = Task2_w_date_form(request.POST,instance=devices.Warehouse)
        Task3_vc_dateform = Task3_w_date_form(request.POST,instance=devices.Warehouse)
        Task4_vc_dateform = Task4_w_date_form(request.POST,instance=devices.Warehouse)
        Task5_vc_dateform = Task5_w_date_form(request.POST,instance=devices.Warehouse)
        Task6_vc_dateform = Task6_w_date_form(request.POST,instance=devices.Warehouse)
        Task7_vc_dateform = Task7_w_date_form(request.POST,instance=devices.Warehouse)
        Task8_vc_dateform = Task8_w_date_form(request.POST,instance=devices.Warehouse)
        Task9_vc_dateform = Task9_w_date_form(request.POST,instance=devices.Warehouse)
        Task10_vc_dateform = Task10_w_date_form(request.POST,instance=devices.Warehouse)
        Task11_vc_dateform = Task11_w_date_form(request.POST,instance=devices.Warehouse)
        Task12_vc_dateform = Task12_w_date_form(request.POST,instance=devices.Warehouse)
        Task13_vc_dateform = Task13_w_date_form(request.POST,instance=devices.Warehouse)
        Task14_vc_dateform = Task14_w_date_form(request.POST,instance=devices.Warehouse)
        Task15_vc_dateform = Task15_w_date_form(request.POST,instance=devices.Warehouse)
        Task16_vc_dateform = Task16_w_date_form(request.POST,instance=devices.Warehouse)
        Task17_vc_dateform = Task17_w_date_form(request.POST,instance=devices.Warehouse)
        Task18_vc_dateform = Task18_w_date_form(request.POST,instance=devices.Warehouse)
        Task19_vc_dateform = Task19_w_date_form(request.POST,instance=devices.Warehouse)
        Task20_vc_dateform = Task20_w_date_form(request.POST,instance=devices.Warehouse)

        if 'Task1Submit' in request.POST:
            if form1.is_valid() and Task1_vc_dateform.is_valid():
                post = form1.save(commit=False)
                post.user = request.user
                post.Warehouse = devices.Warehouse
                Task1_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk + '/warehouse')
            else:
                return redirect('/login/summary/' + pk + '/warehouse')
        elif 'Task2Submit' in request.POST:
            if form2.is_valid() and Task2_vc_dateform.is_valid():
                post = form2.save(commit=False)
                post.user = request.user
                post.Warehouse = devices.Warehouse
                Task2_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/warehouse')
            else:
                return redirect('/login/summary/' + pk + '/warehouse')
        elif 'Task3Submit' in request.POST:
            if form3.is_valid() and Task3_vc_dateform.is_valid():
                post = form3.save(commit=False)
                post.user = request.user
                post.Warehouse = devices.Warehouse
                Task3_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/warehouse')
            else:
                return redirect('/login/summary/' + pk + '/warehouse')
        elif 'Task4Submit' in request.POST:
            if form4.is_valid() and Task4_vc_dateform.is_valid():
                post = form4.save(commit=False)
                post.user = request.user
                post.Warehouse = devices.Warehouse
                Task4_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/warehouse')
            else:
                return redirect('/login/summary/' + pk + '/warehouse')
        elif 'Task5Submit' in request.POST:
            if form5.is_valid() and Task5_vc_dateform.is_valid():
                post = form5.save(commit=False)
                post.user = request.user
                post.Warehouse = devices.Warehouse
                Task5_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/warehouse')
            else:
                return redirect('/login/summary/' + pk + '/warehouse')
        elif 'Task6Submit' in request.POST:
            if form6.is_valid() and Task6_vc_dateform.is_valid():
                post = form6.save(commit=False)
                post.user = request.user
                post.Warehouse = devices.Warehouse
                Task6_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/warehouse')
            else:
                return redirect('/login/summary/' + pk + '/warehouse')
        elif 'Task7Submit' in request.POST:
            if form7.is_valid() and Task7_vc_dateform.is_valid():
                post = form7.save(commit=False)
                post.user = request.user
                post.Warehouse = devices.Warehouse
                Task7_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/warehouse')
            else:
                return redirect('/login/summary/' + pk + '/warehouse')
        elif 'Task8Submit' in request.POST:
            if form8.is_valid() and Task8_vc_dateform.is_valid():
                post = form8.save(commit=False)
                post.user = request.user
                post.Warehouse = devices.Warehouse
                Task8_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/warehouse')
            else:
                return redirect('/login/summary/' + pk + '/warehouse')
        elif 'Task9Submit' in request.POST:
            if form9.is_valid() and Task9_vc_dateform.is_valid():
                post = form9.save(commit=False)
                post.user = request.user
                post.Warehouse = devices.Warehouse
                Task9_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/warehouse')
            else:
                return redirect('/login/summary/' + pk + '/warehouse')
        elif 'Task10Submit' in request.POST:
            if form10.is_valid() and Task10_vc_dateform.is_valid():
                post = form10.save(commit=False)
                post.user = request.user
                post.Warehouse = devices.Warehouse
                Task10_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/warehouse')
            else:
                return redirect('/login/summary/' + pk + '/warehouse')
        elif 'Task11Submit' in request.POST:
            if form11.is_valid() and Task11_vc_dateform.is_valid():
                post = form11.save(commit=False)
                post.user = request.user
                post.Warehouse = devices.Warehouse
                Task11_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/warehouse')
            else:
                return redirect('/login/summary/' + pk + '/warehouse')
        elif 'Task12Submit' in request.POST:
            if form12.is_valid() and Task12_vc_dateform.is_valid():
                post = form12.save(commit=False)
                post.user = request.user
                post.Warehouse = devices.Warehouse
                Task12_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/warehouse')
            else:
                return redirect('/login/summary/' + pk + '/warehouse')
        elif 'Task13Submit' in request.POST:
            if form13.is_valid() and Task13_vc_dateform.is_valid():
                post = form13.save(commit=False)
                post.user = request.user
                post.Warehouse = devices.Warehouse
                Task13_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/warehouse')
            else:
                return redirect('/login/summary/' + pk + '/warehouse')
        elif 'Task14Submit' in request.POST:
            if form14.is_valid() and Task14_vc_dateform.is_valid():
                post = form14.save(commit=False)
                post.user = request.user
                post.Warehouse = devices.Warehouse
                Task14_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/warehouse')
            else:
                return redirect('/login/summary/' + pk + '/warehouse')
        elif 'Task15Submit' in request.POST:
            if form15.is_valid() and Task15_vc_dateform.is_valid():
                post = form15.save(commit=False)
                post.user = request.user
                post.Warehouse = devices.Warehouse
                Task15_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/warehouse')
            else:
                return redirect('/login/summary/' + pk + '/warehouse')
        elif 'Task16Submit' in request.POST:
            if form16.is_valid() and Task16_vc_dateform.is_valid():
                post = form16.save(commit=False)
                post.user = request.user
                post.Warehouse = devices.Warehouse
                Task16_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/warehouse')
            else:
                return redirect('/login/summary/' + pk + '/warehouse')
        elif 'Task17Submit' in request.POST:
            if form17.is_valid() and Task17_vc_dateform.is_valid():
                post = form17.save(commit=False)
                post.user = request.user
                post.Warehouse = devices.Warehouse
                Task17_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/warehouse')
            else:
                return redirect('/login/summary/' + pk + '/warehouse')
        elif 'Task18Submit' in request.POST:
            if form18.is_valid() and Task18_vc_dateform.is_valid():
                post = form18.save(commit=False)
                post.user = request.user
                post.Warehouse = devices.Warehouse
                Task18_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/warehouse')
            else:
                return redirect('/login/summary/' + pk + '/warehouse')
        elif 'Task19Submit' in request.POST:
            if form19.is_valid() and Task19_vc_dateform.is_valid():
                post = form19.save(commit=False)
                post.user = request.user
                post.Warehouse = devices.Warehouse
                Task19_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/warehouse')
            else:
                return redirect('/login/summary/' + pk + '/warehouse')
        elif 'Task20Submit' in request.POST:
            if form20.is_valid() and Task20_vc_dateform.is_valid():
                post = form20.save(commit=False)
                post.user = request.user
                post.Warehouse = devices.Warehouse
                Task20_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/warehouse')
            else:
                return redirect('/login/summary/' + pk + '/warehouse')

########################################################################################################################

class FieldServiceView(LoginRequiredMixin,TemplateView):
    template_name = 'login/device8.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        form1 = Task1_fs_form()
        form2 = Task2_fs_form()
        form3 = Task3_fs_form()
        form4 = Task4_fs_form()
        form5 = Task5_fs_form()
        form6 = Task6_fs_form()
        form7 = Task7_fs_form()
        form8 = Task8_fs_form()
        form9 = Task9_fs_form()
        form10 = Task10_fs_form()
        form11 = Task11_fs_form()
        form12 = Task12_fs_form()
        form13 = Task13_fs_form()
        form14 = Task14_fs_form()
        form15 = Task15_fs_form()
        form16 = Task16_fs_form()
        form17 = Task17_fs_form()
        form18 = Task18_fs_form()
        form19 = Task19_fs_form()
        form20 = Task20_fs_form()
        devices = Device.objects.get(pk=pk)
        Task1_vc_dateform = Task1_fs_date_form(instance=devices.FieldService)
        Task2_vc_dateform = Task2_fs_date_form(instance=devices.FieldService)
        Task3_vc_dateform = Task3_fs_date_form(instance=devices.FieldService)
        Task4_vc_dateform = Task4_fs_date_form(instance=devices.FieldService)
        Task5_vc_dateform = Task5_fs_date_form(instance=devices.FieldService)
        Task6_vc_dateform = Task6_fs_date_form(instance=devices.FieldService)
        Task7_vc_dateform = Task7_fs_date_form(instance=devices.FieldService)
        Task8_vc_dateform = Task8_fs_date_form(instance=devices.FieldService)
        Task9_vc_dateform = Task9_fs_date_form(instance=devices.FieldService)
        Task10_vc_dateform = Task10_fs_date_form(instance=devices.FieldService)
        Task11_vc_dateform = Task11_fs_date_form(instance=devices.FieldService)
        Task12_vc_dateform = Task12_fs_date_form(instance=devices.FieldService)
        Task13_vc_dateform = Task13_fs_date_form(instance=devices.FieldService)
        Task14_vc_dateform = Task14_fs_date_form(instance=devices.FieldService)
        Task15_vc_dateform = Task15_fs_date_form(instance=devices.FieldService)
        Task16_vc_dateform = Task16_fs_date_form(instance=devices.FieldService)
        Task17_vc_dateform = Task17_fs_date_form(instance=devices.FieldService)
        Task18_vc_dateform = Task18_fs_date_form(instance=devices.FieldService)
        Task19_vc_dateform = Task19_fs_date_form(instance=devices.FieldService)
        Task20_vc_dateform = Task20_fs_date_form(instance=devices.FieldService)

        #Calculating % completed
        y=0
        if devices.FieldService.Task1_Name:
            y=y+1
        if devices.FieldService.Task2_Name:
            y=y+1
        if devices.FieldService.Task3_Name:
            y=y+1
        if devices.FieldService.Task4_Name:
            y=y+1
        if devices.FieldService.Task5_Name:
            y=y+1
        if devices.FieldService.Task6_Name:
            y=y+1
        if devices.FieldService.Task7_Name:
            y=y+1
        if devices.FieldService.Task8_Name:
            y=y+1
        if devices.FieldService.Task9_Name:
            y=y+1
        if devices.FieldService.Task10_Name:
            y=y+1
        if devices.FieldService.Task11_Name:
            y=y+1
        if devices.FieldService.Task12_Name:
            y=y+1
        if devices.FieldService.Task13_Name:
            y=y+1
        if devices.FieldService.Task14_Name:
            y=y+1
        if devices.FieldService.Task15_Name:
            y=y+1
        if devices.FieldService.Task16_Name:
            y=y+1
        if devices.FieldService.Task17_Name:
            y=y+1
        if devices.FieldService.Task18_Name:
            y=y+1
        if devices.FieldService.Task19_Name:
            y=y+1
        if devices.FieldService.Task20_Name:
            y=y+1


        x = 0
        if devices.FieldService.Task1_complete_date:
            x =x+1
            devices.FieldService.Task1_alert = False
            devices.FieldService.Task1_warning=False
            devices.FieldService.Status='On_Time'
        if devices.FieldService.Task2_complete_date:
            x = x + 1
            devices.FieldService.Task2_alert = False
            devices.FieldService.Task2_warning=False
            devices.FieldService.Status = 'On_Time'
        if devices.FieldService.Task3_complete_date:
            x = x + 1
            devices.FieldService.Task3_alert = False
            devices.FieldService.Task3_warning=False
            devices.FieldService.Status = 'On_Time'
        if devices.FieldService.Task4_complete_date:
            x = x + 1
            devices.FieldService.Task4_alert = False
            devices.FieldService.Task4_warning=False
            devices.FieldService.Status = 'On_Time'
        if devices.FieldService.Task5_complete_date:
            x = x + 1
            devices.FieldService.Task5_alert = False
            devices.FieldService.Task5_warning=False
            devices.FieldService.Status = 'On_Time'
        if devices.FieldService.Task6_complete_date:
            x = x + 1
            devices.FieldService.Task6_alert = False
            devices.FieldService.Task6_warning=False
            devices.FieldService.Status = 'On_Time'
        if devices.FieldService.Task7_complete_date:
            x =x+1
            devices.FieldService.Task7_alert = False
            devices.FieldService.Task7_warning=False
            devices.FieldService.Status = 'On_Time'
        if devices.FieldService.Task8_complete_date:
            x =x+1
            devices.FieldService.Task8_alert = False
            devices.FieldService.Task8_warning=False
            devices.FieldService.Status = 'On_Time'
        if devices.FieldService.Task9_complete_date:
            x =x+1
            devices.FieldService.Task9_alert = False
            devices.FieldService.Task9_warning=False
            devices.FieldService.Status = 'On_Time'
        if devices.FieldService.Task10_complete_date:
            x =x+1
            devices.FieldService.Task10_alert = False
            devices.FieldService.Task10_warning=False
            devices.FieldService.Status = 'On_Time'
        if devices.FieldService.Task11_complete_date:
            x =x+1
            devices.FieldService.Task11_alert = False
            devices.FieldService.Task11_warning=False
            devices.FieldService.Status = 'On_Time'
        if devices.FieldService.Task12_complete_date:
            x = x + 1
            devices.FieldService.Task12_alert = False
            devices.FieldService.Task12_warning=False
            devices.FieldService.Status = 'On_Time'
        if devices.FieldService.Task13_complete_date:
            x = x + 1
            devices.FieldService.Task13_alert = False
            devices.FieldService.Task13_warning=False
            devices.FieldService.Status = 'On_Time'
        if devices.FieldService.Task14_complete_date:
            x = x + 1
            devices.FieldService.Task14_alert = False
            devices.FieldService.Task14_warning=False
            devices.FieldService.Status = 'On_Time'
        if devices.FieldService.Task15_complete_date:
            x = x + 1
            devices.FieldService.Task15_alert = False
            devices.FieldService.Task15_warning=False
            devices.FieldService.Status = 'On_Time'
        if devices.FieldService.Task16_complete_date:
            x = x + 1
            devices.FieldService.Task16_alert = False
            devices.FieldService.Task16_warning=False
            devices.FieldService.Status = 'On_Time'
        if devices.FieldService.Task17_complete_date:
            x =x+1
            devices.FieldService.Task17_alert = False
            devices.FieldService.Task17_warning=False
            devices.FieldService.Status = 'On_Time'
        if devices.FieldService.Task18_complete_date:
            x =x+1
            devices.FieldService.Task18_alert = False
            devices.FieldService.Task18_warning=False
            devices.FieldService.Status = 'On_Time'
        if devices.FieldService.Task19_complete_date:
            x =x+1
            devices.FieldService.Task19_alert = False
            devices.FieldService.Task19_warning=False
            devices.FieldService.Status = 'On_Time'
        if devices.FieldService.Task20_complete_date:
            x =x+1
            devices.FieldService.Task20_alert = False
            devices.FieldService.Task20_warning=False
            devices.FieldService.Status = 'On_Time'
        percent = x/y * 100
        print (percent)

        #alerting logic
        today = datetime.date.today()
        if devices.FieldService.Task1_End_Date:
            Task1_delta =  devices.FieldService.Task1_End_Date - today
        else:
            Task1_delta = None
        if devices.FieldService.Task2_End_Date:
            Task2_delta = devices.FieldService.Task2_End_Date - today
        else:
            Task2_delta = None
        if devices.FieldService.Task3_End_Date:
            Task3_delta = devices.FieldService.Task3_End_Date - today
        else:
            Task3_delta = None
        if devices.FieldService.Task4_End_Date:
            Task4_delta = devices.FieldService.Task4_End_Date - today
        else:
            Task4_delta = None
        if devices.FieldService.Task5_End_Date:
            Task5_delta = devices.FieldService.Task5_End_Date - today
        else:
            Task5_delta = None
        if devices.FieldService.Task6_End_Date:
            Task6_delta = devices.FieldService.Task6_End_Date - today
        else:
            Task6_delta = None
        if devices.FieldService.Task7_End_Date:
            Task7_delta = devices.FieldService.Task7_End_Date - today
        else:
            Task7_delta = None
        if devices.FieldService.Task8_End_Date:
            Task8_delta = devices.FieldService.Task8_End_Date - today
        else:
            Task8_delta = None
        if devices.FieldService.Task9_End_Date:
            Task9_delta = devices.FieldService.Task9_End_Date - today
        else:
            Task9_delta = None
        if devices.FieldService.Task10_End_Date:
            Task10_delta =  devices.FieldService.Task10_End_Date - today
        else:
            Task10_delta = None
        if devices.FieldService.Task11_End_Date:
            Task11_delta =  devices.FieldService.Task11_End_Date - today
        else:
            Task11_delta = None
        if devices.FieldService.Task12_End_Date:
            Task12_delta = devices.FieldService.Task12_End_Date - today
        else:
            Task12_delta = None
        if devices.FieldService.Task13_End_Date:
            Task13_delta = devices.FieldService.Task13_End_Date - today
        else:
            Task13_delta = None
        if devices.FieldService.Task14_End_Date:
            Task14_delta = devices.FieldService.Task14_End_Date - today
        else:
            Task14_delta = None
        if devices.FieldService.Task15_End_Date:
            Task15_delta = devices.FieldService.Task15_End_Date - today
        else:
            Task15_delta = None
        if devices.FieldService.Task16_End_Date:
            Task16_delta = devices.FieldService.Task16_End_Date - today
        else:
            Task16_delta = None
        if devices.FieldService.Task17_End_Date:
            Task17_delta = devices.FieldService.Task17_End_Date - today
        else:
            Task17_delta = None
        if devices.FieldService.Task18_End_Date:
            Task18_delta = devices.FieldService.Task18_End_Date - today
        else:
            Task18_delta = None
        if devices.FieldService.Task19_End_Date:
            Task19_delta = devices.FieldService.Task19_End_Date - today
        else:
            Task19_delta = None
        if devices.FieldService.Task20_End_Date:
            Task20_delta = devices.FieldService.Task20_End_Date - today
        else:
            Task20_delta = None

        if Task1_delta and Task1_delta < timedelta(devices.FieldService.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not devices.FieldService.Task1_complete_date:
            devices.FieldService.Task1_warning = True
            devices.FieldService.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(devices.FieldService.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not devices.FieldService.Task2_complete_date:
            devices.FieldService.Task2_warning = True
            devices.FieldService.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(devices.FieldService.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not devices.FieldService.Task3_complete_date:
            devices.FieldService.Task3_warning = True
            devices.FieldService.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(devices.FieldService.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not devices.FieldService.Task4_complete_date:
            devices.FieldService.Task4_warning = True
            devices.FieldService.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(devices.FieldService.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not devices.FieldService.Task5_complete_date:
            devices.FieldService.Task5_warning = True
            devices.FieldService.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(devices.FieldService.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not devices.FieldService.Task6_complete_date:
            devices.FieldService.Task6_warning = True
            devices.FieldService.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(devices.FieldService.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not devices.FieldService.Task7_complete_date:
            devices.FieldService.Task7_warning = True
            devices.FieldService.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(devices.FieldService.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not devices.FieldService.Task8_complete_date:
            devices.FieldService.Task8_warning = True
            devices.FieldService.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(devices.FieldService.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not devices.FieldService.Task9_complete_date:
            devices.FieldService.Task9_warning = True
            devices.FieldService.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(devices.FieldService.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not devices.FieldService.Task10_complete_date:
            devices.FieldService.Task10_warning = True
            devices.FieldService.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(devices.FieldService.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not devices.FieldService.Task11_complete_date:
            devices.FieldService.Task11_warning = True
            devices.FieldService.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(devices.FieldService.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not devices.FieldService.Task12_complete_date:
            devices.FieldService.Task12_warning = True
            devices.FieldService.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(devices.FieldService.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not devices.FieldService.Task13_complete_date:
            devices.FieldService.Task13_warning = True
            devices.FieldService.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(devices.FieldService.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not devices.FieldService.Task14_complete_date:
            devices.FieldService.Task14_warning = True
            devices.FieldService.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(devices.FieldService.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not devices.FieldService.Task15_complete_date:
            devices.FieldService.Task15_warning = True
            devices.FieldService.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(devices.FieldService.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not devices.FieldService.Task16_complete_date:
            devices.FieldService.Task16_warning = True
            devices.FieldService.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(devices.FieldService.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not devices.FieldService.Task17_complete_date:
            devices.FieldService.Task17_warning = True
            devices.FieldService.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(devices.FieldService.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not devices.FieldService.Task18_complete_date:
            devices.FieldService.Task18_warning = True
            devices.FieldService.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(devices.FieldService.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not devices.FieldService.Task19_complete_date:
            devices.FieldService.Task19_warning = True
            devices.FieldService.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(devices.FieldService.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not devices.FieldService.Task20_complete_date:
            devices.FieldService.Task20_warning = True
            devices.FieldService.Status = 'At Risk'


        if devices.FieldService.Task1_End_Date and Task1_delta < timedelta(0) and not devices.FieldService.Task1_complete_date:
            devices.FieldService.Task1_alert = True
            devices.FieldService.Status = 'Delayed'
        if devices.FieldService.Task2_End_Date and Task2_delta < timedelta(0) and not devices.FieldService.Task2_complete_date:
            devices.FieldService.Task2_alert = True
            devices.FieldService.Status = 'Delayed'
        if devices.FieldService.Task3_End_Date and Task3_delta < timedelta(0) and not devices.FieldService.Task3_complete_date:
            devices.FieldService.Task3_alert = True
            devices.FieldService.Status = 'Delayed'
        if devices.FieldService.Task4_End_Date and Task4_delta < timedelta(0) and not devices.FieldService.Task4_complete_date:
            devices.FieldService.Task4_alert = True
            devices.FieldService.Status = 'Delayed'
        if devices.FieldService.Task5_End_Date and Task5_delta < timedelta(0) and not devices.FieldService.Task5_complete_date:
            devices.FieldService.Task5_alert = True
            devices.FieldService.Status = 'Delayed'
        if devices.FieldService.Task6_End_Date and Task6_delta < timedelta(0) and not devices.FieldService.Task6_complete_date:
            devices.FieldService.Task6_alert = True
            devices.FieldService.Status = 'Delayed'
        if devices.FieldService.Task7_End_Date and Task7_delta < timedelta(0) and not devices.FieldService.Task7_complete_date:
            devices.FieldService.Task7_alert = True
            devices.FieldService.Status = 'Delayed'
        if devices.FieldService.Task8_End_Date and Task8_delta < timedelta(0)and not devices.FieldService.Task8_complete_date:
            devices.FieldService.Task8_alert = True
            devices.FieldService.Status = 'Delayed'
        if devices.FieldService.Task9_End_Date and Task9_delta < timedelta(0)and not devices.FieldService.Task9_complete_date:
            devices.FieldService.Task9_alert = True
            devices.FieldService.Status = 'Delayed'
        if devices.FieldService.Task10_End_Date and Task10_delta < timedelta(0) and not devices.FieldService.Task10_complete_date:
            devices.FieldService.Task10_alert = True
            devices.FieldService.Status = 'Delayed'
        if devices.FieldService.Task11_End_Date and Task11_delta < timedelta(0) and not devices.FieldService.Task11_complete_date:
            devices.FieldService.Task11_alert = True
            devices.FieldService.Status = 'Delayed'
        if devices.FieldService.Task12_End_Date and Task12_delta < timedelta(0) and not devices.FieldService.Task12_complete_date:
            devices.FieldService.Task12_alert = True
            devices.FieldService.Status = 'Delayed'
        if devices.FieldService.Task13_End_Date and Task13_delta < timedelta(0) and not devices.FieldService.Task13_complete_date:
            devices.FieldService.Task13_alert = True
            devices.FieldService.Status = 'Delayed'
        if devices.FieldService.Task14_End_Date and Task14_delta < timedelta(0) and not devices.FieldService.Task14_complete_date:
            devices.FieldService.Task14_alert = True
            devices.FieldService.Status = 'Delayed'
        if devices.FieldService.Task15_End_Date and Task15_delta < timedelta(0) and not devices.FieldService.Task15_complete_date:
            devices.FieldService.Task15_alert = True
            devices.FieldService.Status = 'Delayed'
        if devices.FieldService.Task16_End_Date and Task16_delta < timedelta(0) and not devices.FieldService.Task16_complete_date:
            devices.FieldService.Task16_alert = True
            devices.FieldService.Status = 'Delayed'
        if devices.FieldService.Task17_End_Date and Task17_delta < timedelta(0)and not devices.FieldService.Task17_complete_date:
            devices.FieldService.Task17_alert = True
            devices.FieldService.Status = 'Delayed'
        if devices.FieldService.Task18_End_Date and Task18_delta < timedelta(0)and not devices.FieldService.Task18_complete_date:
            devices.FieldService.Task18_alert = True
            devices.FieldService.Status = 'Delayed'
        if devices.FieldService.Task19_End_Date and Task19_delta < timedelta(0)and not devices.FieldService.Task19_complete_date:
            devices.FieldService.Task19_alert = True
            devices.FieldService.Status = 'Delayed'
        if devices.FieldService.Task20_End_Date and Task20_delta < timedelta(0)and not devices.FieldService.Task20_complete_date:
            devices.FieldService.Task20_alert = True
            devices.FieldService.Status = 'Delayed'

        devices.FieldService.completed = int(percent)
        devices.FieldService.save()
        posts1 = devices.FieldService.task1statusfieldservice_set.all().order_by('-created')
        posts2 = devices.FieldService.task2statusfieldservice_set.all().order_by('-created')
        posts3 = devices.FieldService.task3statusfieldservice_set.all().order_by('-created')
        posts4 = devices.FieldService.task4statusfieldservice_set.all().order_by('-created')
        posts5 = devices.FieldService.task5statusfieldservice_set.all().order_by('-created')
        posts6 = devices.FieldService.task6statusfieldservice_set.all().order_by('-created')
        posts7 = devices.FieldService.task7statusfieldservice_set.all().order_by('-created')
        posts8 = devices.FieldService.task8statusfieldservice_set.all().order_by('-created')
        posts9 = devices.FieldService.task9statusfieldservice_set.all().order_by('-created')
        posts10 = devices.FieldService.task10statusfieldservice_set.all().order_by('-created')
        posts11 = devices.FieldService.task11statusfieldservice_set.all().order_by('-created')
        posts12 = devices.FieldService.task12statusfieldservice_set.all().order_by('-created')
        posts13 = devices.FieldService.task13statusfieldservice_set.all().order_by('-created')
        posts14 = devices.FieldService.task14statusfieldservice_set.all().order_by('-created')
        posts15 = devices.FieldService.task15statusfieldservice_set.all().order_by('-created')
        posts16 = devices.FieldService.task16statusfieldservice_set.all().order_by('-created')
        posts17 = devices.FieldService.task17statusfieldservice_set.all().order_by('-created')
        posts18 = devices.FieldService.task18statusfieldservice_set.all().order_by('-created')
        posts19 = devices.FieldService.task19statusfieldservice_set.all().order_by('-created')
        posts20 = devices.FieldService.task20statusfieldservice_set.all().order_by('-created')

        args = {'devices':devices, 'form1':form1, 'form2':form2, 'form3':form3, 'form4':form4, 'form5':form5, 'form6':form6,
                'form7': form7, 'form8':form8, 'form9':form9, 'form10':form10, 'form11':form11, 'form12':form12, 'form13':form13,
                'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17, 'form18': form18, 'form19': form19,
                'form20': form20, 'posts1':posts1, 'posts2':posts2, 'posts3':posts3, 'posts4':posts4, 'posts5':posts5, 'posts6':posts6,
                'posts7': posts7, 'posts8':posts8, 'posts9':posts9, 'posts10':posts10, 'posts11':posts11, 'posts12':posts12, 'posts13':posts13,
                'posts14': posts14, 'posts15': posts15, 'posts16': posts16, 'posts17': posts17, 'posts18': posts18, 'posts19': posts19,
                'posts20': posts20, 'Task1_vc_dateform':Task1_vc_dateform, 'Task2_vc_dateform':Task2_vc_dateform,
                'Task3_vc_dateform':Task3_vc_dateform, 'Task4_vc_dateform':Task4_vc_dateform,
                'Task5_vc_dateform': Task5_vc_dateform, 'Task6_vc_dateform': Task6_vc_dateform,
                'Task7_vc_dateform': Task7_vc_dateform, 'Task8_vc_dateform': Task8_vc_dateform,
                'Task9_vc_dateform': Task9_vc_dateform, 'Task10_vc_dateform': Task10_vc_dateform,
                'Task11_vc_dateform': Task11_vc_dateform, 'Task12_vc_dateform': Task12_vc_dateform,
                'Task13_vc_dateform': Task13_vc_dateform, 'Task14_vc_dateform': Task14_vc_dateform,
                'Task15_vc_dateform': Task15_vc_dateform, 'Task16_vc_dateform': Task16_vc_dateform,
                'Task17_vc_dateform': Task17_vc_dateform, 'Task18_vc_dateform': Task18_vc_dateform,
                'Task19_vc_dateform': Task19_vc_dateform, 'Task20_vc_dateform': Task20_vc_dateform,
                'Task1_delta':Task1_delta, 'Task7_delta':Task7_delta, 'Task12_delta':Task12_delta, 'Task17_delta':Task17_delta,
                'Task2_delta': Task2_delta, 'Task8_delta': Task8_delta, 'Task13_delta': Task13_delta,
                'Task3_delta': Task3_delta, 'Task9_delta':Task9_delta, 'Task14_delta':Task14_delta, 'Task18_delta':Task18_delta,
                'Task4_delta':Task4_delta, 'Task10_delta':Task10_delta, 'Task15_delta':Task15_delta, 'Task19_delta':Task19_delta,
                'Task5_delta':Task5_delta, 'Task11_delta':Task11_delta, 'Task16_delta':Task16_delta, 'Task20_delta':Task20_delta,
                'Task6_delta':Task6_delta,
                }
        return render(request,self.template_name,args)

    def post(self, request, pk):

        form1 = Task1_fs_form(request.POST)
        form2 = Task2_fs_form(request.POST)
        form3 = Task3_fs_form(request.POST)
        form4 = Task4_fs_form(request.POST)
        form5 = Task5_fs_form(request.POST)
        form6 = Task6_fs_form(request.POST)
        form7 = Task7_fs_form(request.POST)
        form8 = Task8_fs_form(request.POST)
        form9 = Task9_fs_form(request.POST)
        form10 = Task10_fs_form(request.POST)
        form11 = Task11_fs_form(request.POST)
        form12 = Task12_fs_form(request.POST)
        form13 = Task13_fs_form(request.POST)
        form14 = Task14_fs_form(request.POST)
        form15 = Task15_fs_form(request.POST)
        form16 = Task16_fs_form(request.POST)
        form17 = Task17_fs_form(request.POST)
        form18 = Task18_fs_form(request.POST)
        form19 = Task19_fs_form(request.POST)
        form20 = Task20_fs_form(request.POST)
        devices = Device.objects.get(pk=pk)

        Task1_vc_dateform = Task1_fs_date_form(request.POST,instance=devices.FieldService)
        Task2_vc_dateform = Task2_fs_date_form(request.POST,instance=devices.FieldService)
        Task3_vc_dateform = Task3_fs_date_form(request.POST,instance=devices.FieldService)
        Task4_vc_dateform = Task4_fs_date_form(request.POST,instance=devices.FieldService)
        Task5_vc_dateform = Task5_fs_date_form(request.POST,instance=devices.FieldService)
        Task6_vc_dateform = Task6_fs_date_form(request.POST,instance=devices.FieldService)
        Task7_vc_dateform = Task7_fs_date_form(request.POST,instance=devices.FieldService)
        Task8_vc_dateform = Task8_fs_date_form(request.POST,instance=devices.FieldService)
        Task9_vc_dateform = Task9_fs_date_form(request.POST,instance=devices.FieldService)
        Task10_vc_dateform = Task10_fs_date_form(request.POST,instance=devices.FieldService)
        Task11_vc_dateform = Task11_fs_date_form(request.POST,instance=devices.FieldService)
        Task12_vc_dateform = Task12_fs_date_form(request.POST,instance=devices.FieldService)
        Task13_vc_dateform = Task13_fs_date_form(request.POST,instance=devices.FieldService)
        Task14_vc_dateform = Task14_fs_date_form(request.POST,instance=devices.FieldService)
        Task15_vc_dateform = Task15_fs_date_form(request.POST,instance=devices.FieldService)
        Task16_vc_dateform = Task16_fs_date_form(request.POST,instance=devices.FieldService)
        Task17_vc_dateform = Task17_fs_date_form(request.POST,instance=devices.FieldService)
        Task18_vc_dateform = Task18_fs_date_form(request.POST,instance=devices.FieldService)
        Task19_vc_dateform = Task19_fs_date_form(request.POST,instance=devices.FieldService)
        Task20_vc_dateform = Task20_fs_date_form(request.POST,instance=devices.FieldService)

        if 'Task1Submit' in request.POST:
            if form1.is_valid() and Task1_vc_dateform.is_valid():
                post = form1.save(commit=False)
                post.user = request.user
                post.FieldService = devices.FieldService
                Task1_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk + '/fieldservice')
            else:
                return redirect('/login/summary/' + pk + '/fieldservice')
        elif 'Task2Submit' in request.POST:
            if form2.is_valid() and Task2_vc_dateform.is_valid():
                post = form2.save(commit=False)
                post.user = request.user
                post.FieldService = devices.FieldService
                Task2_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/fieldservice')
            else:
                return redirect('/login/summary/' + pk + '/fieldservice')
        elif 'Task3Submit' in request.POST:
            if form3.is_valid() and Task3_vc_dateform.is_valid():
                post = form3.save(commit=False)
                post.user = request.user
                post.FieldService = devices.FieldService
                Task3_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/fieldservice')
            else:
                return redirect('/login/summary/' + pk + '/fieldservice')
        elif 'Task4Submit' in request.POST:
            if form4.is_valid() and Task4_vc_dateform.is_valid():
                post = form4.save(commit=False)
                post.user = request.user
                post.FieldService = devices.FieldService
                Task4_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/fieldservice')
            else:
                return redirect('/login/summary/' + pk + '/fieldservice')
        elif 'Task5Submit' in request.POST:
            if form5.is_valid() and Task5_vc_dateform.is_valid():
                post = form5.save(commit=False)
                post.user = request.user
                post.FieldService = devices.FieldService
                Task5_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/fieldservice')
            else:
                return redirect('/login/summary/' + pk + '/fieldservice')
        elif 'Task6Submit' in request.POST:
            if form6.is_valid() and Task6_vc_dateform.is_valid():
                post = form6.save(commit=False)
                post.user = request.user
                post.FieldService = devices.FieldService
                Task6_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/fieldservice')
            else:
                return redirect('/login/summary/' + pk + '/fieldservice')
        elif 'Task7Submit' in request.POST:
            if form7.is_valid() and Task7_vc_dateform.is_valid():
                post = form7.save(commit=False)
                post.user = request.user
                post.FieldService = devices.FieldService
                Task7_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/fieldservice')
            else:
                return redirect('/login/summary/' + pk + '/fieldservice')
        elif 'Task8Submit' in request.POST:
            if form8.is_valid() and Task8_vc_dateform.is_valid():
                post = form8.save(commit=False)
                post.user = request.user
                post.FieldService = devices.FieldService
                Task8_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/fieldservice')
            else:
                return redirect('/login/summary/' + pk + '/fieldservice')
        elif 'Task9Submit' in request.POST:
            if form9.is_valid() and Task9_vc_dateform.is_valid():
                post = form9.save(commit=False)
                post.user = request.user
                post.FieldService = devices.FieldService
                Task9_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/fieldservice')
            else:
                return redirect('/login/summary/' + pk + '/fieldservice')
        elif 'Task10Submit' in request.POST:
            if form10.is_valid() and Task10_vc_dateform.is_valid():
                post = form10.save(commit=False)
                post.user = request.user
                post.FieldService = devices.FieldService
                Task10_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/fieldservice')
            else:
                return redirect('/login/summary/' + pk + '/fieldservice')
        elif 'Task11Submit' in request.POST:
            if form11.is_valid() and Task11_vc_dateform.is_valid():
                post = form11.save(commit=False)
                post.user = request.user
                post.FieldService = devices.FieldService
                Task11_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/fieldservice')
            else:
                return redirect('/login/summary/' + pk + '/fieldservice')
        elif 'Task12Submit' in request.POST:
            if form12.is_valid() and Task12_vc_dateform.is_valid():
                post = form12.save(commit=False)
                post.user = request.user
                post.FieldService = devices.FieldService
                Task12_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/fieldservice')
            else:
                return redirect('/login/summary/' + pk + '/fieldservice')
        elif 'Task13Submit' in request.POST:
            if form13.is_valid() and Task13_vc_dateform.is_valid():
                post = form13.save(commit=False)
                post.user = request.user
                post.FieldService = devices.FieldService
                Task13_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/fieldservice')
            else:
                return redirect('/login/summary/' + pk + '/fieldservice')
        elif 'Task14Submit' in request.POST:
            if form14.is_valid() and Task14_vc_dateform.is_valid():
                post = form14.save(commit=False)
                post.user = request.user
                post.FieldService = devices.FieldService
                Task14_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/fieldservice')
            else:
                return redirect('/login/summary/' + pk + '/fieldservice')
        elif 'Task15Submit' in request.POST:
            if form15.is_valid() and Task15_vc_dateform.is_valid():
                post = form15.save(commit=False)
                post.user = request.user
                post.FieldService = devices.FieldService
                Task15_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/fieldservice')
            else:
                return redirect('/login/summary/' + pk + '/fieldservice')
        elif 'Task16Submit' in request.POST:
            if form16.is_valid() and Task16_vc_dateform.is_valid():
                post = form16.save(commit=False)
                post.user = request.user
                post.FieldService = devices.FieldService
                Task16_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/fieldservice')
            else:
                return redirect('/login/summary/' + pk + '/fieldservice')
        elif 'Task17Submit' in request.POST:
            if form17.is_valid() and Task17_vc_dateform.is_valid():
                post = form17.save(commit=False)
                post.user = request.user
                post.FieldService = devices.FieldService
                Task17_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/fieldservice')
            else:
                return redirect('/login/summary/' + pk + '/fieldservice')
        elif 'Task18Submit' in request.POST:
            if form18.is_valid() and Task18_vc_dateform.is_valid():
                post = form18.save(commit=False)
                post.user = request.user
                post.FieldService = devices.FieldService
                Task18_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/fieldservice')
            else:
                return redirect('/login/summary/' + pk + '/fieldservice')
        elif 'Task19Submit' in request.POST:
            if form19.is_valid() and Task19_vc_dateform.is_valid():
                post = form19.save(commit=False)
                post.user = request.user
                post.FieldService = devices.FieldService
                Task19_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/fieldservice')
            else:
                return redirect('/login/summary/' + pk + '/fieldservice')
        elif 'Task20Submit' in request.POST:
            if form20.is_valid() and Task20_vc_dateform.is_valid():
                post = form20.save(commit=False)
                post.user = request.user
                post.FieldService = devices.FieldService
                Task20_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/fieldservice')
            else:
                return redirect('/login/summary/' + pk + '/fieldservice')

########################################################################################################################

class TechSupportView(LoginRequiredMixin,TemplateView):
    template_name = 'login/device9.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        form1 = Task1_ts_form()
        form2 = Task2_ts_form()
        form3 = Task3_ts_form()
        form4 = Task4_ts_form()
        form5 = Task5_ts_form()
        form6 = Task6_ts_form()
        form7 = Task7_ts_form()
        form8 = Task8_ts_form()
        form9 = Task9_ts_form()
        form10 = Task10_ts_form()
        form11 = Task11_ts_form()
        form12 = Task12_ts_form()
        form13 = Task13_ts_form()
        form14 = Task14_ts_form()
        form15 = Task15_ts_form()
        form16 = Task16_ts_form()
        form17 = Task17_ts_form()
        form18 = Task18_ts_form()
        form19 = Task19_ts_form()
        form20 = Task20_ts_form()
        devices = Device.objects.get(pk=pk)
        Task1_vc_dateform = Task1_ts_date_form(instance=devices.TechSupport)
        Task2_vc_dateform = Task2_ts_date_form(instance=devices.TechSupport)
        Task3_vc_dateform = Task3_ts_date_form(instance=devices.TechSupport)
        Task4_vc_dateform = Task4_ts_date_form(instance=devices.TechSupport)
        Task5_vc_dateform = Task5_ts_date_form(instance=devices.TechSupport)
        Task6_vc_dateform = Task6_ts_date_form(instance=devices.TechSupport)
        Task7_vc_dateform = Task7_ts_date_form(instance=devices.TechSupport)
        Task8_vc_dateform = Task8_ts_date_form(instance=devices.TechSupport)
        Task9_vc_dateform = Task9_ts_date_form(instance=devices.TechSupport)
        Task10_vc_dateform = Task10_ts_date_form(instance=devices.TechSupport)
        Task11_vc_dateform = Task11_ts_date_form(instance=devices.TechSupport)
        Task12_vc_dateform = Task12_ts_date_form(instance=devices.TechSupport)
        Task13_vc_dateform = Task13_ts_date_form(instance=devices.TechSupport)
        Task14_vc_dateform = Task14_ts_date_form(instance=devices.TechSupport)
        Task15_vc_dateform = Task15_ts_date_form(instance=devices.TechSupport)
        Task16_vc_dateform = Task16_ts_date_form(instance=devices.TechSupport)
        Task17_vc_dateform = Task17_ts_date_form(instance=devices.TechSupport)
        Task18_vc_dateform = Task18_ts_date_form(instance=devices.TechSupport)
        Task19_vc_dateform = Task19_ts_date_form(instance=devices.TechSupport)
        Task20_vc_dateform = Task20_ts_date_form(instance=devices.TechSupport)

        #Calculating % completed
        y=0
        if devices.TechSupport.Task1_Name:
            y=y+1
        if devices.TechSupport.Task2_Name:
            y=y+1
        if devices.TechSupport.Task3_Name:
            y=y+1
        if devices.TechSupport.Task4_Name:
            y=y+1
        if devices.TechSupport.Task5_Name:
            y=y+1
        if devices.TechSupport.Task6_Name:
            y=y+1
        if devices.TechSupport.Task7_Name:
            y=y+1
        if devices.TechSupport.Task8_Name:
            y=y+1
        if devices.TechSupport.Task9_Name:
            y=y+1
        if devices.TechSupport.Task10_Name:
            y=y+1
        if devices.TechSupport.Task11_Name:
            y=y+1
        if devices.TechSupport.Task12_Name:
            y=y+1
        if devices.TechSupport.Task13_Name:
            y=y+1
        if devices.TechSupport.Task14_Name:
            y=y+1
        if devices.TechSupport.Task15_Name:
            y=y+1
        if devices.TechSupport.Task16_Name:
            y=y+1
        if devices.TechSupport.Task17_Name:
            y=y+1
        if devices.TechSupport.Task18_Name:
            y=y+1
        if devices.TechSupport.Task19_Name:
            y=y+1
        if devices.TechSupport.Task20_Name:
            y=y+1


        x = 0
        if devices.TechSupport.Task1_complete_date:
            x =x+1
            devices.TechSupport.Task1_alert = False
            devices.TechSupport.Task1_warning=False
            devices.TechSupport.Status='On_Time'
        if devices.TechSupport.Task2_complete_date:
            x = x + 1
            devices.TechSupport.Task2_alert = False
            devices.TechSupport.Task2_warning=False
            devices.TechSupport.Status = 'On_Time'
        if devices.TechSupport.Task3_complete_date:
            x = x + 1
            devices.TechSupport.Task3_alert = False
            devices.TechSupport.Task3_warning=False
            devices.TechSupport.Status = 'On_Time'
        if devices.TechSupport.Task4_complete_date:
            x = x + 1
            devices.TechSupport.Task4_alert = False
            devices.TechSupport.Task4_warning=False
            devices.TechSupport.Status = 'On_Time'
        if devices.TechSupport.Task5_complete_date:
            x = x + 1
            devices.TechSupport.Task5_alert = False
            devices.TechSupport.Task5_warning=False
            devices.TechSupport.Status = 'On_Time'
        if devices.TechSupport.Task6_complete_date:
            x = x + 1
            devices.TechSupport.Task6_alert = False
            devices.TechSupport.Task6_warning=False
            devices.TechSupport.Status = 'On_Time'
        if devices.TechSupport.Task7_complete_date:
            x =x+1
            devices.TechSupport.Task7_alert = False
            devices.TechSupport.Task7_warning=False
            devices.TechSupport.Status = 'On_Time'
        if devices.TechSupport.Task8_complete_date:
            x =x+1
            devices.TechSupport.Task8_alert = False
            devices.TechSupport.Task8_warning=False
            devices.TechSupport.Status = 'On_Time'
        if devices.TechSupport.Task9_complete_date:
            x =x+1
            devices.TechSupport.Task9_alert = False
            devices.TechSupport.Task9_warning=False
            devices.TechSupport.Status = 'On_Time'
        if devices.TechSupport.Task10_complete_date:
            x =x+1
            devices.TechSupport.Task10_alert = False
            devices.TechSupport.Task10_warning=False
            devices.TechSupport.Status = 'On_Time'
        if devices.TechSupport.Task11_complete_date:
            x =x+1
            devices.TechSupport.Task11_alert = False
            devices.TechSupport.Task11_warning=False
            devices.TechSupport.Status = 'On_Time'
        if devices.TechSupport.Task12_complete_date:
            x = x + 1
            devices.TechSupport.Task12_alert = False
            devices.TechSupport.Task12_warning=False
            devices.TechSupport.Status = 'On_Time'
        if devices.TechSupport.Task13_complete_date:
            x = x + 1
            devices.TechSupport.Task13_alert = False
            devices.TechSupport.Task13_warning=False
            devices.TechSupport.Status = 'On_Time'
        if devices.TechSupport.Task14_complete_date:
            x = x + 1
            devices.TechSupport.Task14_alert = False
            devices.TechSupport.Task14_warning=False
            devices.TechSupport.Status = 'On_Time'
        if devices.TechSupport.Task15_complete_date:
            x = x + 1
            devices.TechSupport.Task15_alert = False
            devices.TechSupport.Task15_warning=False
            devices.TechSupport.Status = 'On_Time'
        if devices.TechSupport.Task16_complete_date:
            x = x + 1
            devices.TechSupport.Task16_alert = False
            devices.TechSupport.Task16_warning=False
            devices.TechSupport.Status = 'On_Time'
        if devices.TechSupport.Task17_complete_date:
            x =x+1
            devices.TechSupport.Task17_alert = False
            devices.TechSupport.Task17_warning=False
            devices.TechSupport.Status = 'On_Time'
        if devices.TechSupport.Task18_complete_date:
            x =x+1
            devices.TechSupport.Task18_alert = False
            devices.TechSupport.Task18_warning=False
            devices.TechSupport.Status = 'On_Time'
        if devices.TechSupport.Task19_complete_date:
            x =x+1
            devices.TechSupport.Task19_alert = False
            devices.TechSupport.Task19_warning=False
            devices.TechSupport.Status = 'On_Time'
        if devices.TechSupport.Task20_complete_date:
            x =x+1
            devices.TechSupport.Task20_alert = False
            devices.TechSupport.Task20_warning=False
            devices.TechSupport.Status = 'On_Time'
        percent = x/y * 100
        print (percent)

        #alerting logic
        today = datetime.date.today()
        if devices.TechSupport.Task1_End_Date:
            Task1_delta =  devices.TechSupport.Task1_End_Date - today
        else:
            Task1_delta = None
        if devices.TechSupport.Task2_End_Date:
            Task2_delta = devices.TechSupport.Task2_End_Date - today
        else:
            Task2_delta = None
        if devices.TechSupport.Task3_End_Date:
            Task3_delta = devices.TechSupport.Task3_End_Date - today
        else:
            Task3_delta = None
        if devices.TechSupport.Task4_End_Date:
            Task4_delta = devices.TechSupport.Task4_End_Date - today
        else:
            Task4_delta = None
        if devices.TechSupport.Task5_End_Date:
            Task5_delta = devices.TechSupport.Task5_End_Date - today
        else:
            Task5_delta = None
        if devices.TechSupport.Task6_End_Date:
            Task6_delta = devices.TechSupport.Task6_End_Date - today
        else:
            Task6_delta = None
        if devices.TechSupport.Task7_End_Date:
            Task7_delta = devices.TechSupport.Task7_End_Date - today
        else:
            Task7_delta = None
        if devices.TechSupport.Task8_End_Date:
            Task8_delta = devices.TechSupport.Task8_End_Date - today
        else:
            Task8_delta = None
        if devices.TechSupport.Task9_End_Date:
            Task9_delta = devices.TechSupport.Task9_End_Date - today
        else:
            Task9_delta = None
        if devices.TechSupport.Task10_End_Date:
            Task10_delta =  devices.TechSupport.Task10_End_Date - today
        else:
            Task10_delta = None
        if devices.TechSupport.Task11_End_Date:
            Task11_delta =  devices.TechSupport.Task11_End_Date - today
        else:
            Task11_delta = None
        if devices.TechSupport.Task12_End_Date:
            Task12_delta = devices.TechSupport.Task12_End_Date - today
        else:
            Task12_delta = None
        if devices.TechSupport.Task13_End_Date:
            Task13_delta = devices.TechSupport.Task13_End_Date - today
        else:
            Task13_delta = None
        if devices.TechSupport.Task14_End_Date:
            Task14_delta = devices.TechSupport.Task14_End_Date - today
        else:
            Task14_delta = None
        if devices.TechSupport.Task15_End_Date:
            Task15_delta = devices.TechSupport.Task15_End_Date - today
        else:
            Task15_delta = None
        if devices.TechSupport.Task16_End_Date:
            Task16_delta = devices.TechSupport.Task16_End_Date - today
        else:
            Task16_delta = None
        if devices.TechSupport.Task17_End_Date:
            Task17_delta = devices.TechSupport.Task17_End_Date - today
        else:
            Task17_delta = None
        if devices.TechSupport.Task18_End_Date:
            Task18_delta = devices.TechSupport.Task18_End_Date - today
        else:
            Task18_delta = None
        if devices.TechSupport.Task19_End_Date:
            Task19_delta = devices.TechSupport.Task19_End_Date - today
        else:
            Task19_delta = None
        if devices.TechSupport.Task20_End_Date:
            Task20_delta = devices.TechSupport.Task20_End_Date - today
        else:
            Task20_delta = None

        if Task1_delta and Task1_delta < timedelta(devices.TechSupport.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not devices.TechSupport.Task1_complete_date:
            devices.TechSupport.Task1_warning = True
            devices.TechSupport.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(devices.TechSupport.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not devices.TechSupport.Task2_complete_date:
            devices.TechSupport.Task2_warning = True
            devices.TechSupport.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(devices.TechSupport.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not devices.TechSupport.Task3_complete_date:
            devices.TechSupport.Task3_warning = True
            devices.TechSupport.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(devices.TechSupport.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not devices.TechSupport.Task4_complete_date:
            devices.TechSupport.Task4_warning = True
            devices.TechSupport.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(devices.TechSupport.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not devices.TechSupport.Task5_complete_date:
            devices.TechSupport.Task5_warning = True
            devices.TechSupport.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(devices.TechSupport.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not devices.TechSupport.Task6_complete_date:
            devices.TechSupport.Task6_warning = True
            devices.TechSupport.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(devices.TechSupport.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not devices.TechSupport.Task7_complete_date:
            devices.TechSupport.Task7_warning = True
            devices.TechSupport.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(devices.TechSupport.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not devices.TechSupport.Task8_complete_date:
            devices.TechSupport.Task8_warning = True
            devices.TechSupport.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(devices.TechSupport.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not devices.TechSupport.Task9_complete_date:
            devices.TechSupport.Task9_warning = True
            devices.TechSupport.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(devices.TechSupport.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not devices.TechSupport.Task10_complete_date:
            devices.TechSupport.Task10_warning = True
            devices.TechSupport.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(devices.TechSupport.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not devices.TechSupport.Task11_complete_date:
            devices.TechSupport.Task11_warning = True
            devices.TechSupport.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(devices.TechSupport.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not devices.TechSupport.Task12_complete_date:
            devices.TechSupport.Task12_warning = True
            devices.TechSupport.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(devices.TechSupport.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not devices.TechSupport.Task13_complete_date:
            devices.TechSupport.Task13_warning = True
            devices.TechSupport.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(devices.TechSupport.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not devices.TechSupport.Task14_complete_date:
            devices.TechSupport.Task14_warning = True
            devices.TechSupport.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(devices.TechSupport.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not devices.TechSupport.Task15_complete_date:
            devices.TechSupport.Task15_warning = True
            devices.TechSupport.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(devices.TechSupport.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not devices.TechSupport.Task16_complete_date:
            devices.TechSupport.Task16_warning = True
            devices.TechSupport.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(devices.TechSupport.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not devices.TechSupport.Task17_complete_date:
            devices.TechSupport.Task17_warning = True
            devices.TechSupport.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(devices.TechSupport.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not devices.TechSupport.Task18_complete_date:
            devices.TechSupport.Task18_warning = True
            devices.TechSupport.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(devices.TechSupport.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not devices.TechSupport.Task19_complete_date:
            devices.TechSupport.Task19_warning = True
            devices.TechSupport.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(devices.TechSupport.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not devices.TechSupport.Task20_complete_date:
            devices.TechSupport.Task20_warning = True
            devices.TechSupport.Status = 'At Risk'

        if devices.TechSupport.Task1_End_Date and Task1_delta < timedelta(0) and not devices.TechSupport.Task1_complete_date:
            devices.TechSupport.Task1_alert = True
            devices.TechSupport.Status = 'Delayed'
        if devices.TechSupport.Task2_End_Date and Task2_delta < timedelta(0) and not devices.TechSupport.Task2_complete_date:
            devices.TechSupport.Task2_alert = True
            devices.TechSupport.Status = 'Delayed'
        if devices.TechSupport.Task3_End_Date and Task3_delta < timedelta(0) and not devices.TechSupport.Task3_complete_date:
            devices.TechSupport.Task3_alert = True
            devices.TechSupport.Status = 'Delayed'
        if devices.TechSupport.Task4_End_Date and Task4_delta < timedelta(0) and not devices.TechSupport.Task4_complete_date:
            devices.TechSupport.Task4_alert = True
            devices.TechSupport.Status = 'Delayed'
        if devices.TechSupport.Task5_End_Date and Task5_delta < timedelta(0) and not devices.TechSupport.Task5_complete_date:
            devices.TechSupport.Task5_alert = True
            devices.TechSupport.Status = 'Delayed'
        if devices.TechSupport.Task6_End_Date and Task6_delta < timedelta(0) and not devices.TechSupport.Task6_complete_date:
            devices.TechSupport.Task6_alert = True
            devices.TechSupport.Status = 'Delayed'
        if devices.TechSupport.Task7_End_Date and Task7_delta < timedelta(0) and not devices.TechSupport.Task7_complete_date:
            devices.TechSupport.Task7_alert = True
            devices.TechSupport.Status = 'Delayed'
        if devices.TechSupport.Task8_End_Date and Task8_delta < timedelta(0)and not devices.TechSupport.Task8_complete_date:
            devices.TechSupport.Task8_alert = True
            devices.TechSupport.Status = 'Delayed'
        if devices.TechSupport.Task9_End_Date and Task9_delta < timedelta(0)and not devices.TechSupport.Task9_complete_date:
            devices.TechSupport.Task9_alert = True
            devices.TechSupport.Status = 'Delayed'
        if devices.TechSupport.Task10_End_Date and Task10_delta < timedelta(0) and not devices.TechSupport.Task10_complete_date:
            devices.TechSupport.Task10_alert = True
            devices.TechSupport.Status = 'Delayed'
        if devices.TechSupport.Task11_End_Date and Task11_delta < timedelta(0) and not devices.TechSupport.Task11_complete_date:
            devices.TechSupport.Task11_alert = True
            devices.TechSupport.Status = 'Delayed'
        if devices.TechSupport.Task12_End_Date and Task12_delta < timedelta(0) and not devices.TechSupport.Task12_complete_date:
            devices.TechSupport.Task12_alert = True
            devices.TechSupport.Status = 'Delayed'
        if devices.TechSupport.Task13_End_Date and Task13_delta < timedelta(0) and not devices.TechSupport.Task13_complete_date:
            devices.TechSupport.Task13_alert = True
            devices.TechSupport.Status = 'Delayed'
        if devices.TechSupport.Task14_End_Date and Task14_delta < timedelta(0) and not devices.TechSupport.Task14_complete_date:
            devices.TechSupport.Task14_alert = True
            devices.TechSupport.Status = 'Delayed'
        if devices.TechSupport.Task15_End_Date and Task15_delta < timedelta(0) and not devices.TechSupport.Task15_complete_date:
            devices.TechSupport.Task15_alert = True
            devices.TechSupport.Status = 'Delayed'
        if devices.TechSupport.Task16_End_Date and Task16_delta < timedelta(0) and not devices.TechSupport.Task16_complete_date:
            devices.TechSupport.Task16_alert = True
            devices.TechSupport.Status = 'Delayed'
        if devices.TechSupport.Task17_End_Date and Task17_delta < timedelta(0)and not devices.TechSupport.Task17_complete_date:
            devices.TechSupport.Task17_alert = True
            devices.TechSupport.Status = 'Delayed'
        if devices.TechSupport.Task18_End_Date and Task18_delta < timedelta(0)and not devices.TechSupport.Task18_complete_date:
            devices.TechSupport.Task18_alert = True
            devices.TechSupport.Status = 'Delayed'
        if devices.TechSupport.Task19_End_Date and Task19_delta < timedelta(0)and not devices.TechSupport.Task19_complete_date:
            devices.TechSupport.Task19_alert = True
            devices.TechSupport.Status = 'Delayed'
        if devices.TechSupport.Task20_End_Date and Task20_delta < timedelta(0)and not devices.TechSupport.Task20_complete_date:
            devices.TechSupport.Task20_alert = True
            devices.TechSupport.Status = 'Delayed'

        devices.TechSupport.completed = int(percent)
        devices.TechSupport.save()
        posts1 = devices.TechSupport.task1statustechsupport_set.all().order_by('-created')
        posts2 = devices.TechSupport.task2statustechsupport_set.all().order_by('-created')
        posts3 = devices.TechSupport.task3statustechsupport_set.all().order_by('-created')
        posts4 = devices.TechSupport.task4statustechsupport_set.all().order_by('-created')
        posts5 = devices.TechSupport.task5statustechsupport_set.all().order_by('-created')
        posts6 = devices.TechSupport.task6statustechsupport_set.all().order_by('-created')
        posts7 = devices.TechSupport.task7statustechsupport_set.all().order_by('-created')
        posts8 = devices.TechSupport.task8statustechsupport_set.all().order_by('-created')
        posts9 = devices.TechSupport.task9statustechsupport_set.all().order_by('-created')
        posts10 = devices.TechSupport.task10statustechsupport_set.all().order_by('-created')
        posts11 = devices.TechSupport.task11statustechsupport_set.all().order_by('-created')
        posts12 = devices.TechSupport.task12statustechsupport_set.all().order_by('-created')
        posts13 = devices.TechSupport.task13statustechsupport_set.all().order_by('-created')
        posts14 = devices.TechSupport.task14statustechsupport_set.all().order_by('-created')
        posts15 = devices.TechSupport.task15statustechsupport_set.all().order_by('-created')
        posts16 = devices.TechSupport.task16statustechsupport_set.all().order_by('-created')
        posts17 = devices.TechSupport.task17statustechsupport_set.all().order_by('-created')
        posts18 = devices.TechSupport.task18statustechsupport_set.all().order_by('-created')
        posts19 = devices.TechSupport.task19statustechsupport_set.all().order_by('-created')
        posts20 = devices.TechSupport.task20statustechsupport_set.all().order_by('-created')

        args = {'devices':devices, 'form1':form1, 'form2':form2, 'form3':form3, 'form4':form4, 'form5':form5, 'form6':form6,
                'form7': form7, 'form8':form8, 'form9':form9, 'form10':form10, 'form11':form11, 'form12':form12, 'form13':form13,
                'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17, 'form18': form18, 'form19': form19,
                'form20': form20, 'posts1':posts1, 'posts2':posts2, 'posts3':posts3, 'posts4':posts4, 'posts5':posts5, 'posts6':posts6,
                'posts7': posts7, 'posts8':posts8, 'posts9':posts9, 'posts10':posts10, 'posts11':posts11, 'posts12':posts12, 'posts13':posts13,
                'posts14': posts14, 'posts15': posts15, 'posts16': posts16, 'posts17': posts17, 'posts18': posts18, 'posts19': posts19,
                'posts20': posts20, 'Task1_vc_dateform':Task1_vc_dateform, 'Task2_vc_dateform':Task2_vc_dateform,
                'Task3_vc_dateform':Task3_vc_dateform, 'Task4_vc_dateform':Task4_vc_dateform,
                'Task5_vc_dateform': Task5_vc_dateform, 'Task6_vc_dateform': Task6_vc_dateform,
                'Task7_vc_dateform': Task7_vc_dateform, 'Task8_vc_dateform': Task8_vc_dateform,
                'Task9_vc_dateform': Task9_vc_dateform, 'Task10_vc_dateform': Task10_vc_dateform,
                'Task11_vc_dateform': Task11_vc_dateform, 'Task12_vc_dateform': Task12_vc_dateform,
                'Task13_vc_dateform': Task13_vc_dateform, 'Task14_vc_dateform': Task14_vc_dateform,
                'Task15_vc_dateform': Task15_vc_dateform, 'Task16_vc_dateform': Task16_vc_dateform,
                'Task17_vc_dateform': Task17_vc_dateform, 'Task18_vc_dateform': Task18_vc_dateform,
                'Task19_vc_dateform': Task19_vc_dateform, 'Task20_vc_dateform': Task20_vc_dateform,
                'Task1_delta':Task1_delta, 'Task7_delta':Task7_delta, 'Task12_delta':Task12_delta, 'Task17_delta':Task17_delta,
                'Task2_delta': Task2_delta, 'Task8_delta': Task8_delta, 'Task13_delta': Task13_delta,
                'Task3_delta': Task3_delta, 'Task9_delta':Task9_delta, 'Task14_delta':Task14_delta, 'Task18_delta':Task18_delta,
                'Task4_delta':Task4_delta, 'Task10_delta':Task10_delta, 'Task15_delta':Task15_delta, 'Task19_delta':Task19_delta,
                'Task5_delta':Task5_delta, 'Task11_delta':Task11_delta, 'Task16_delta':Task16_delta, 'Task20_delta':Task20_delta,
                'Task6_delta':Task6_delta,
                }
        return render(request,self.template_name,args)

    def post(self, request, pk):

        form1 = Task1_ts_form(request.POST)
        form2 = Task2_ts_form(request.POST)
        form3 = Task3_ts_form(request.POST)
        form4 = Task4_ts_form(request.POST)
        form5 = Task5_ts_form(request.POST)
        form6 = Task6_ts_form(request.POST)
        form7 = Task7_ts_form(request.POST)
        form8 = Task8_ts_form(request.POST)
        form9 = Task9_ts_form(request.POST)
        form10 = Task10_ts_form(request.POST)
        form11 = Task11_ts_form(request.POST)
        form12 = Task12_ts_form(request.POST)
        form13 = Task13_ts_form(request.POST)
        form14 = Task14_ts_form(request.POST)
        form15 = Task15_ts_form(request.POST)
        form16 = Task16_ts_form(request.POST)
        form17 = Task17_ts_form(request.POST)
        form18 = Task18_ts_form(request.POST)
        form19 = Task19_ts_form(request.POST)
        form20 = Task20_ts_form(request.POST)
        devices = Device.objects.get(pk=pk)

        Task1_vc_dateform = Task1_ts_date_form(request.POST,instance=devices.TechSupport)
        Task2_vc_dateform = Task2_ts_date_form(request.POST,instance=devices.TechSupport)
        Task3_vc_dateform = Task3_ts_date_form(request.POST,instance=devices.TechSupport)
        Task4_vc_dateform = Task4_ts_date_form(request.POST,instance=devices.TechSupport)
        Task5_vc_dateform = Task5_ts_date_form(request.POST,instance=devices.TechSupport)
        Task6_vc_dateform = Task6_ts_date_form(request.POST,instance=devices.TechSupport)
        Task7_vc_dateform = Task7_ts_date_form(request.POST,instance=devices.TechSupport)
        Task8_vc_dateform = Task8_ts_date_form(request.POST,instance=devices.TechSupport)
        Task9_vc_dateform = Task9_ts_date_form(request.POST,instance=devices.TechSupport)
        Task10_vc_dateform = Task10_ts_date_form(request.POST,instance=devices.TechSupport)
        Task11_vc_dateform = Task11_ts_date_form(request.POST,instance=devices.TechSupport)
        Task12_vc_dateform = Task12_ts_date_form(request.POST,instance=devices.TechSupport)
        Task13_vc_dateform = Task13_ts_date_form(request.POST,instance=devices.TechSupport)
        Task14_vc_dateform = Task14_ts_date_form(request.POST,instance=devices.TechSupport)
        Task15_vc_dateform = Task15_ts_date_form(request.POST,instance=devices.TechSupport)
        Task16_vc_dateform = Task16_ts_date_form(request.POST,instance=devices.TechSupport)
        Task17_vc_dateform = Task17_ts_date_form(request.POST,instance=devices.TechSupport)
        Task18_vc_dateform = Task18_ts_date_form(request.POST,instance=devices.TechSupport)
        Task19_vc_dateform = Task19_ts_date_form(request.POST,instance=devices.TechSupport)
        Task20_vc_dateform = Task20_ts_date_form(request.POST,instance=devices.TechSupport)

        if 'Task1Submit' in request.POST:
            if form1.is_valid() and Task1_vc_dateform.is_valid():
                post = form1.save(commit=False)
                post.user = request.user
                post.TechSupport = devices.TechSupport
                Task1_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk + '/techsupport')
            else:
                return redirect('/login/summary/' + pk + '/techsupport')
        elif 'Task2Submit' in request.POST:
            if form2.is_valid() and Task2_vc_dateform.is_valid():
                post = form2.save(commit=False)
                post.user = request.user
                post.TechSupport = devices.TechSupport
                Task2_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/techsupport')
            else:
                return redirect('/login/summary/' + pk + '/techsupport')
        elif 'Task3Submit' in request.POST:
            if form3.is_valid() and Task3_vc_dateform.is_valid():
                post = form3.save(commit=False)
                post.user = request.user
                post.TechSupport = devices.TechSupport
                Task3_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/techsupport')
            else:
                return redirect('/login/summary/' + pk + '/techsupport')
        elif 'Task4Submit' in request.POST:
            if form4.is_valid() and Task4_vc_dateform.is_valid():
                post = form4.save(commit=False)
                post.user = request.user
                post.TechSupport = devices.TechSupport
                Task4_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/techsupport')
            else:
                return redirect('/login/summary/' + pk + '/techsupport')
        elif 'Task5Submit' in request.POST:
            if form5.is_valid() and Task5_vc_dateform.is_valid():
                post = form5.save(commit=False)
                post.user = request.user
                post.TechSupport = devices.TechSupport
                Task5_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/techsupport')
            else:
                return redirect('/login/summary/' + pk + '/techsupport')
        elif 'Task6Submit' in request.POST:
            if form6.is_valid() and Task6_vc_dateform.is_valid():
                post = form6.save(commit=False)
                post.user = request.user
                post.TechSupport = devices.TechSupport
                Task6_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/techsupport')
            else:
                return redirect('/login/summary/' + pk + '/techsupport')
        elif 'Task7Submit' in request.POST:
            if form7.is_valid() and Task7_vc_dateform.is_valid():
                post = form7.save(commit=False)
                post.user = request.user
                post.TechSupport = devices.TechSupport
                Task7_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/techsupport')
            else:
                return redirect('/login/summary/' + pk + '/techsupport')
        elif 'Task8Submit' in request.POST:
            if form8.is_valid() and Task8_vc_dateform.is_valid():
                post = form8.save(commit=False)
                post.user = request.user
                post.TechSupport = devices.TechSupport
                Task8_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/techsupport')
            else:
                return redirect('/login/summary/' + pk + '/techsupport')
        elif 'Task9Submit' in request.POST:
            if form9.is_valid() and Task9_vc_dateform.is_valid():
                post = form9.save(commit=False)
                post.user = request.user
                post.TechSupport = devices.TechSupport
                Task9_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/techsupport')
            else:
                return redirect('/login/summary/' + pk + '/techsupport')
        elif 'Task10Submit' in request.POST:
            if form10.is_valid() and Task10_vc_dateform.is_valid():
                post = form10.save(commit=False)
                post.user = request.user
                post.TechSupport = devices.TechSupport
                Task10_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/techsupport')
            else:
                return redirect('/login/summary/' + pk + '/techsupport')
        elif 'Task11Submit' in request.POST:
            if form11.is_valid() and Task11_vc_dateform.is_valid():
                post = form11.save(commit=False)
                post.user = request.user
                post.TechSupport = devices.TechSupport
                Task11_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/techsupport')
            else:
                return redirect('/login/summary/' + pk + '/techsupport')
        elif 'Task12Submit' in request.POST:
            if form12.is_valid() and Task12_vc_dateform.is_valid():
                post = form12.save(commit=False)
                post.user = request.user
                post.TechSupport = devices.TechSupport
                Task12_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/techsupport')
            else:
                return redirect('/login/summary/' + pk + '/techsupport')
        elif 'Task13Submit' in request.POST:
            if form13.is_valid() and Task13_vc_dateform.is_valid():
                post = form13.save(commit=False)
                post.user = request.user
                post.TechSupport = devices.TechSupport
                Task13_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/techsupport')
            else:
                return redirect('/login/summary/' + pk + '/techsupport')
        elif 'Task14Submit' in request.POST:
            if form14.is_valid() and Task14_vc_dateform.is_valid():
                post = form14.save(commit=False)
                post.user = request.user
                post.TechSupport = devices.TechSupport
                Task14_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/techsupport')
            else:
                return redirect('/login/summary/' + pk + '/techsupport')
        elif 'Task15Submit' in request.POST:
            if form15.is_valid() and Task15_vc_dateform.is_valid():
                post = form15.save(commit=False)
                post.user = request.user
                post.TechSupport = devices.TechSupport
                Task15_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/techsupport')
            else:
                return redirect('/login/summary/' + pk + '/techsupport')
        elif 'Task16Submit' in request.POST:
            if form16.is_valid() and Task16_vc_dateform.is_valid():
                post = form16.save(commit=False)
                post.user = request.user
                post.TechSupport = devices.TechSupport
                Task16_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/techsupport')
            else:
                return redirect('/login/summary/' + pk + '/techsupport')
        elif 'Task17Submit' in request.POST:
            if form17.is_valid() and Task17_vc_dateform.is_valid():
                post = form17.save(commit=False)
                post.user = request.user
                post.TechSupport = devices.TechSupport
                Task17_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/techsupport')
            else:
                return redirect('/login/summary/' + pk + '/techsupport')
        elif 'Task18Submit' in request.POST:
            if form18.is_valid() and Task18_vc_dateform.is_valid():
                post = form18.save(commit=False)
                post.user = request.user
                post.TechSupport = devices.TechSupport
                Task18_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/techsupport')
            else:
                return redirect('/login/summary/' + pk + '/techsupport')
        elif 'Task19Submit' in request.POST:
            if form19.is_valid() and Task19_vc_dateform.is_valid():
                post = form19.save(commit=False)
                post.user = request.user
                post.TechSupport = devices.TechSupport
                Task19_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/techsupport')
            else:
                return redirect('/login/summary/' + pk + '/techsupport')
        elif 'Task20Submit' in request.POST:
            if form20.is_valid() and Task20_vc_dateform.is_valid():
                post = form20.save(commit=False)
                post.user = request.user
                post.TechSupport = devices.TechSupport
                Task20_vc_dateform.save()
                post.save()
                return redirect('/login/summary/'+ pk+ '/techsupport')
            else:
                return redirect('/login/summary/' + pk + '/techsupport')


########################################################################################################################

class ServiceMarketingView(LoginRequiredMixin,TemplateView):
    template_name = 'login/device10.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        form1 = Task1_sm_form()
        form2 = Task2_sm_form()
        form3 = Task3_sm_form()
        form4 = Task4_sm_form()
        form5 = Task5_sm_form()
        form6 = Task6_sm_form()
        form7 = Task7_sm_form()
        form8 = Task8_sm_form()
        form9 = Task9_sm_form()
        form10 = Task10_sm_form()
        form11 = Task11_sm_form()
        form12 = Task12_sm_form()
        form13 = Task13_sm_form()
        form14 = Task14_sm_form()
        form15 = Task15_sm_form()
        form16 = Task16_sm_form()
        form17 = Task17_sm_form()
        form18 = Task18_sm_form()
        form19 = Task19_sm_form()
        form20 = Task20_sm_form()
        devices = Device.objects.get(pk=pk)
        Task1_vc_dateform = Task1_sm_date_form(instance=devices.ServiceMarketing)
        Task2_vc_dateform = Task2_sm_date_form(instance=devices.ServiceMarketing)
        Task3_vc_dateform = Task3_sm_date_form(instance=devices.ServiceMarketing)
        Task4_vc_dateform = Task4_sm_date_form(instance=devices.ServiceMarketing)
        Task5_vc_dateform = Task5_sm_date_form(instance=devices.ServiceMarketing)
        Task6_vc_dateform = Task6_sm_date_form(instance=devices.ServiceMarketing)
        Task7_vc_dateform = Task7_sm_date_form(instance=devices.ServiceMarketing)
        Task8_vc_dateform = Task8_sm_date_form(instance=devices.ServiceMarketing)
        Task9_vc_dateform = Task9_sm_date_form(instance=devices.ServiceMarketing)
        Task10_vc_dateform = Task10_sm_date_form(instance=devices.ServiceMarketing)
        Task11_vc_dateform = Task11_sm_date_form(instance=devices.ServiceMarketing)
        Task12_vc_dateform = Task12_sm_date_form(instance=devices.ServiceMarketing)
        Task13_vc_dateform = Task13_sm_date_form(instance=devices.ServiceMarketing)
        Task14_vc_dateform = Task14_sm_date_form(instance=devices.ServiceMarketing)
        Task15_vc_dateform = Task15_sm_date_form(instance=devices.ServiceMarketing)
        Task16_vc_dateform = Task16_sm_date_form(instance=devices.ServiceMarketing)
        Task17_vc_dateform = Task17_sm_date_form(instance=devices.ServiceMarketing)
        Task18_vc_dateform = Task18_sm_date_form(instance=devices.ServiceMarketing)
        Task19_vc_dateform = Task19_sm_date_form(instance=devices.ServiceMarketing)
        Task20_vc_dateform = Task20_sm_date_form(instance=devices.ServiceMarketing)

        # Calculating % completed
        y = 0
        if devices.ServiceMarketing.Task1_Name:
            y = y + 1
        if devices.ServiceMarketing.Task2_Name:
            y = y + 1
        if devices.ServiceMarketing.Task3_Name:
            y = y + 1
        if devices.ServiceMarketing.Task4_Name:
            y = y + 1
        if devices.ServiceMarketing.Task5_Name:
            y = y + 1
        if devices.ServiceMarketing.Task6_Name:
            y = y + 1
        if devices.ServiceMarketing.Task7_Name:
            y = y + 1
        if devices.ServiceMarketing.Task8_Name:
            y = y + 1
        if devices.ServiceMarketing.Task9_Name:
            y = y + 1
        if devices.ServiceMarketing.Task10_Name:
            y = y + 1
        if devices.ServiceMarketing.Task11_Name:
            y = y + 1
        if devices.ServiceMarketing.Task12_Name:
            y = y + 1
        if devices.ServiceMarketing.Task13_Name:
            y = y + 1
        if devices.ServiceMarketing.Task14_Name:
            y = y + 1
        if devices.ServiceMarketing.Task15_Name:
            y = y + 1
        if devices.ServiceMarketing.Task16_Name:
            y = y + 1
        if devices.ServiceMarketing.Task17_Name:
            y = y + 1
        if devices.ServiceMarketing.Task18_Name:
            y = y + 1
        if devices.ServiceMarketing.Task19_Name:
            y = y + 1
        if devices.ServiceMarketing.Task20_Name:
            y = y + 1

        x = 0
        if devices.ServiceMarketing.Task1_complete_date:
            x =x+1
            devices.ServiceMarketing.Task1_alert = False
            devices.ServiceMarketing.Task1_warning=False
            devices.ServiceMarketing.Status='On_Time'
        if devices.ServiceMarketing.Task2_complete_date:
            x = x + 1
            devices.ServiceMarketing.Task2_alert = False
            devices.ServiceMarketing.Task2_warning=False
            devices.ServiceMarketing.Status = 'On_Time'
        if devices.ServiceMarketing.Task3_complete_date:
            x = x + 1
            devices.ServiceMarketing.Task3_alert = False
            devices.ServiceMarketing.Task3_warning=False
            devices.ServiceMarketing.Status = 'On_Time'
        if devices.ServiceMarketing.Task4_complete_date:
            x = x + 1
            devices.ServiceMarketing.Task4_alert = False
            devices.ServiceMarketing.Task4_warning=False
            devices.ServiceMarketing.Status = 'On_Time'
        if devices.ServiceMarketing.Task5_complete_date:
            x = x + 1
            devices.ServiceMarketing.Task5_alert = False
            devices.ServiceMarketing.Task5_warning=False
            devices.ServiceMarketing.Status = 'On_Time'
        if devices.ServiceMarketing.Task6_complete_date:
            x = x + 1
            devices.ServiceMarketing.Task6_alert = False
            devices.ServiceMarketing.Task6_warning=False
            devices.ServiceMarketing.Status = 'On_Time'
        if devices.ServiceMarketing.Task7_complete_date:
            x =x+1
            devices.ServiceMarketing.Task7_alert = False
            devices.ServiceMarketing.Task7_warning=False
            devices.ServiceMarketing.Status = 'On_Time'
        if devices.ServiceMarketing.Task8_complete_date:
            x =x+1
            devices.ServiceMarketing.Task8_alert = False
            devices.ServiceMarketing.Task8_warning=False
            devices.ServiceMarketing.Status = 'On_Time'
        if devices.ServiceMarketing.Task9_complete_date:
            x =x+1
            devices.ServiceMarketing.Task9_alert = False
            devices.ServiceMarketing.Task9_warning=False
            devices.ServiceMarketing.Status = 'On_Time'
        if devices.ServiceMarketing.Task10_complete_date:
            x =x+1
            devices.ServiceMarketing.Task10_alert = False
            devices.ServiceMarketing.Task10_warning=False
            devices.ServiceMarketing.Status = 'On_Time'
        if devices.ServiceMarketing.Task11_complete_date:
            x =x+1
            devices.ServiceMarketing.Task11_alert = False
            devices.ServiceMarketing.Task11_warning=False
            devices.ServiceMarketing.Status = 'On_Time'
        if devices.ServiceMarketing.Task12_complete_date:
            x = x + 1
            devices.ServiceMarketing.Task12_alert = False
            devices.ServiceMarketing.Task12_warning=False
            devices.ServiceMarketing.Status = 'On_Time'
        if devices.ServiceMarketing.Task13_complete_date:
            x = x + 1
            devices.ServiceMarketing.Task13_alert = False
            devices.ServiceMarketing.Task13_warning=False
            devices.ServiceMarketing.Status = 'On_Time'
        if devices.ServiceMarketing.Task14_complete_date:
            x = x + 1
            devices.ServiceMarketing.Task14_alert = False
            devices.ServiceMarketing.Task14_warning=False
            devices.ServiceMarketing.Status = 'On_Time'
        if devices.ServiceMarketing.Task15_complete_date:
            x = x + 1
            devices.ServiceMarketing.Task15_alert = False
            devices.ServiceMarketing.Task15_warning=False
            devices.ServiceMarketing.Status = 'On_Time'
        if devices.ServiceMarketing.Task16_complete_date:
            x = x + 1
            devices.ServiceMarketing.Task16_alert = False
            devices.ServiceMarketing.Task16_warning=False
            devices.ServiceMarketing.Status = 'On_Time'
        if devices.ServiceMarketing.Task17_complete_date:
            x =x+1
            devices.ServiceMarketing.Task17_alert = False
            devices.ServiceMarketing.Task17_warning=False
            devices.ServiceMarketing.Status = 'On_Time'
        if devices.ServiceMarketing.Task18_complete_date:
            x =x+1
            devices.ServiceMarketing.Task18_alert = False
            devices.ServiceMarketing.Task18_warning=False
            devices.ServiceMarketing.Status = 'On_Time'
        if devices.ServiceMarketing.Task19_complete_date:
            x =x+1
            devices.ServiceMarketing.Task19_alert = False
            devices.ServiceMarketing.Task19_warning=False
            devices.ServiceMarketing.Status = 'On_Time'
        if devices.ServiceMarketing.Task20_complete_date:
            x =x+1
            devices.ServiceMarketing.Task20_alert = False
            devices.ServiceMarketing.Task20_warning=False
            devices.ServiceMarketing.Status = 'On_Time'
        percent = x/y * 100
        print (percent)

        #alerting logic
        today = datetime.date.today()
        if devices.ServiceMarketing.Task1_End_Date:
            Task1_delta =  devices.ServiceMarketing.Task1_End_Date - today
        else:
            Task1_delta = None
        if devices.ServiceMarketing.Task2_End_Date:
            Task2_delta = devices.ServiceMarketing.Task2_End_Date - today
        else:
            Task2_delta = None
        if devices.ServiceMarketing.Task3_End_Date:
            Task3_delta = devices.ServiceMarketing.Task3_End_Date - today
        else:
            Task3_delta = None
        if devices.ServiceMarketing.Task4_End_Date:
            Task4_delta = devices.ServiceMarketing.Task4_End_Date - today
        else:
            Task4_delta = None
        if devices.ServiceMarketing.Task5_End_Date:
            Task5_delta = devices.ServiceMarketing.Task5_End_Date - today
        else:
            Task5_delta = None
        if devices.ServiceMarketing.Task6_End_Date:
            Task6_delta = devices.ServiceMarketing.Task6_End_Date - today
        else:
            Task6_delta = None
        if devices.ServiceMarketing.Task7_End_Date:
            Task7_delta = devices.ServiceMarketing.Task7_End_Date - today
        else:
            Task7_delta = None
        if devices.ServiceMarketing.Task8_End_Date:
            Task8_delta = devices.ServiceMarketing.Task8_End_Date - today
        else:
            Task8_delta = None
        if devices.ServiceMarketing.Task9_End_Date:
            Task9_delta = devices.ServiceMarketing.Task9_End_Date - today
        else:
            Task9_delta = None
        if devices.ServiceMarketing.Task10_End_Date:
            Task10_delta =  devices.ServiceMarketing.Task10_End_Date - today
        else:
            Task10_delta = None
        if devices.ServiceMarketing.Task11_End_Date:
            Task11_delta =  devices.ServiceMarketing.Task11_End_Date - today
        else:
            Task11_delta = None
        if devices.ServiceMarketing.Task12_End_Date:
            Task12_delta = devices.ServiceMarketing.Task12_End_Date - today
        else:
            Task12_delta = None
        if devices.ServiceMarketing.Task13_End_Date:
            Task13_delta = devices.ServiceMarketing.Task13_End_Date - today
        else:
            Task13_delta = None
        if devices.ServiceMarketing.Task14_End_Date:
            Task14_delta = devices.ServiceMarketing.Task14_End_Date - today
        else:
            Task14_delta = None
        if devices.ServiceMarketing.Task15_End_Date:
            Task15_delta = devices.ServiceMarketing.Task15_End_Date - today
        else:
            Task15_delta = None
        if devices.ServiceMarketing.Task16_End_Date:
            Task16_delta = devices.ServiceMarketing.Task16_End_Date - today
        else:
            Task16_delta = None
        if devices.ServiceMarketing.Task17_End_Date:
            Task17_delta = devices.ServiceMarketing.Task17_End_Date - today
        else:
            Task17_delta = None
        if devices.ServiceMarketing.Task18_End_Date:
            Task18_delta = devices.ServiceMarketing.Task18_End_Date - today
        else:
            Task18_delta = None
        if devices.ServiceMarketing.Task19_End_Date:
            Task19_delta = devices.ServiceMarketing.Task19_End_Date - today
        else:
            Task19_delta = None
        if devices.ServiceMarketing.Task20_End_Date:
            Task20_delta = devices.ServiceMarketing.Task20_End_Date - today
        else:
            Task20_delta = None

        if Task1_delta and Task1_delta < timedelta(devices.ServiceMarketing.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not devices.ServiceMarketing.Task1_complete_date:
            devices.ServiceMarketing.Task1_warning = True
            devices.ServiceMarketing.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(devices.ServiceMarketing.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not devices.ServiceMarketing.Task2_complete_date:
            devices.ServiceMarketing.Task2_warning = True
            devices.ServiceMarketing.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(devices.ServiceMarketing.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not devices.ServiceMarketing.Task3_complete_date:
            devices.ServiceMarketing.Task3_warning = True
            devices.ServiceMarketing.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(devices.ServiceMarketing.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not devices.ServiceMarketing.Task4_complete_date:
            devices.ServiceMarketing.Task4_warning = True
            devices.ServiceMarketing.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(devices.ServiceMarketing.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not devices.ServiceMarketing.Task5_complete_date:
            devices.ServiceMarketing.Task5_warning = True
            devices.ServiceMarketing.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(devices.ServiceMarketing.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not devices.ServiceMarketing.Task6_complete_date:
            devices.ServiceMarketing.Task6_warning = True
            devices.ServiceMarketing.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(devices.ServiceMarketing.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not devices.ServiceMarketing.Task7_complete_date:
            devices.ServiceMarketing.Task7_warning = True
            devices.ServiceMarketing.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(devices.ServiceMarketing.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not devices.ServiceMarketing.Task8_complete_date:
            devices.ServiceMarketing.Task8_warning = True
            devices.ServiceMarketing.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(devices.ServiceMarketing.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not devices.ServiceMarketing.Task9_complete_date:
            devices.ServiceMarketing.Task9_warning = True
            devices.ServiceMarketing.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(devices.ServiceMarketing.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not devices.ServiceMarketing.Task10_complete_date:
            devices.ServiceMarketing.Task10_warning = True
            devices.ServiceMarketing.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(devices.ServiceMarketing.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not devices.ServiceMarketing.Task11_complete_date:
            devices.ServiceMarketing.Task11_warning = True
            devices.ServiceMarketing.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(devices.ServiceMarketing.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not devices.ServiceMarketing.Task12_complete_date:
            devices.ServiceMarketing.Task12_warning = True
            devices.ServiceMarketing.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(devices.ServiceMarketing.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not devices.ServiceMarketing.Task13_complete_date:
            devices.ServiceMarketing.Task13_warning = True
            devices.ServiceMarketing.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(devices.ServiceMarketing.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not devices.ServiceMarketing.Task14_complete_date:
            devices.ServiceMarketing.Task14_warning = True
            devices.ServiceMarketing.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(devices.ServiceMarketing.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not devices.ServiceMarketing.Task15_complete_date:
            devices.ServiceMarketing.Task15_warning = True
            devices.ServiceMarketing.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(devices.ServiceMarketing.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not devices.ServiceMarketing.Task16_complete_date:
            devices.ServiceMarketing.Task16_warning = True
            devices.ServiceMarketing.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(devices.ServiceMarketing.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not devices.ServiceMarketing.Task17_complete_date:
            devices.ServiceMarketing.Task17_warning = True
            devices.ServiceMarketing.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(devices.ServiceMarketing.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not devices.ServiceMarketing.Task18_complete_date:
            devices.ServiceMarketing.Task18_warning = True
            devices.ServiceMarketing.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(devices.ServiceMarketing.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not devices.ServiceMarketing.Task19_complete_date:
            devices.ServiceMarketing.Task19_warning = True
            devices.ServiceMarketing.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(devices.ServiceMarketing.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not devices.ServiceMarketing.Task20_complete_date:
            devices.ServiceMarketing.Task20_warning = True
            devices.ServiceMarketing.Status = 'At Risk'

        if devices.ServiceMarketing.Task1_End_Date and Task1_delta < timedelta(0) and not devices.ServiceMarketing.Task1_complete_date:
            devices.ServiceMarketing.Task1_alert = True
            devices.ServiceMarketing.Status = 'Delayed'
        if devices.ServiceMarketing.Task2_End_Date and Task2_delta < timedelta(0) and not devices.ServiceMarketing.Task2_complete_date:
            devices.ServiceMarketing.Task2_alert = True
            devices.ServiceMarketing.Status = 'Delayed'
        if devices.ServiceMarketing.Task3_End_Date and Task3_delta < timedelta(0) and not devices.ServiceMarketing.Task3_complete_date:
            devices.ServiceMarketing.Task3_alert = True
            devices.ServiceMarketing.Status = 'Delayed'
        if devices.ServiceMarketing.Task4_End_Date and Task4_delta < timedelta(0) and not devices.ServiceMarketing.Task4_complete_date:
            devices.ServiceMarketing.Task4_alert = True
            devices.ServiceMarketing.Status = 'Delayed'
        if devices.ServiceMarketing.Task5_End_Date and Task5_delta < timedelta(0) and not devices.ServiceMarketing.Task5_complete_date:
            devices.ServiceMarketing.Task5_alert = True
            devices.ServiceMarketing.Status = 'Delayed'
        if devices.ServiceMarketing.Task6_End_Date and Task6_delta < timedelta(0) and not devices.ServiceMarketing.Task6_complete_date:
            devices.ServiceMarketing.Task6_alert = True
            devices.ServiceMarketing.Status = 'Delayed'
        if devices.ServiceMarketing.Task7_End_Date and Task7_delta < timedelta(0) and not devices.ServiceMarketing.Task7_complete_date:
            devices.ServiceMarketing.Task7_alert = True
            devices.ServiceMarketing.Status = 'Delayed'
        if devices.ServiceMarketing.Task8_End_Date and Task8_delta < timedelta(0)and not devices.ServiceMarketing.Task8_complete_date:
            devices.ServiceMarketing.Task8_alert = True
            devices.ServiceMarketing.Status = 'Delayed'
        if devices.ServiceMarketing.Task9_End_Date and Task9_delta < timedelta(0)and not devices.ServiceMarketing.Task9_complete_date:
            devices.ServiceMarketing.Task9_alert = True
            devices.ServiceMarketing.Status = 'Delayed'
        if devices.ServiceMarketing.Task10_End_Date and Task10_delta < timedelta(0) and not devices.ServiceMarketing.Task10_complete_date:
            devices.ServiceMarketing.Task10_alert = True
            devices.ServiceMarketing.Status = 'Delayed'
        if devices.ServiceMarketing.Task11_End_Date and Task11_delta < timedelta(0) and not devices.ServiceMarketing.Task11_complete_date:
            devices.ServiceMarketing.Task11_alert = True
            devices.ServiceMarketing.Status = 'Delayed'
        if devices.ServiceMarketing.Task12_End_Date and Task12_delta < timedelta(0) and not devices.ServiceMarketing.Task12_complete_date:
            devices.ServiceMarketing.Task12_alert = True
            devices.ServiceMarketing.Status = 'Delayed'
        if devices.ServiceMarketing.Task13_End_Date and Task13_delta < timedelta(0) and not devices.ServiceMarketing.Task13_complete_date:
            devices.ServiceMarketing.Task13_alert = True
            devices.ServiceMarketing.Status = 'Delayed'
        if devices.ServiceMarketing.Task14_End_Date and Task14_delta < timedelta(0) and not devices.ServiceMarketing.Task14_complete_date:
            devices.ServiceMarketing.Task14_alert = True
            devices.ServiceMarketing.Status = 'Delayed'
        if devices.ServiceMarketing.Task15_End_Date and Task15_delta < timedelta(0) and not devices.ServiceMarketing.Task15_complete_date:
            devices.ServiceMarketing.Task15_alert = True
            devices.ServiceMarketing.Status = 'Delayed'
        if devices.ServiceMarketing.Task16_End_Date and Task16_delta < timedelta(0) and not devices.ServiceMarketing.Task16_complete_date:
            devices.ServiceMarketing.Task16_alert = True
            devices.ServiceMarketing.Status = 'Delayed'
        if devices.ServiceMarketing.Task17_End_Date and Task17_delta < timedelta(0)and not devices.ServiceMarketing.Task17_complete_date:
            devices.ServiceMarketing.Task17_alert = True
            devices.ServiceMarketing.Status = 'Delayed'
        if devices.ServiceMarketing.Task18_End_Date and Task18_delta < timedelta(0)and not devices.ServiceMarketing.Task18_complete_date:
            devices.ServiceMarketing.Task18_alert = True
            devices.ServiceMarketing.Status = 'Delayed'
        if devices.ServiceMarketing.Task19_End_Date and Task19_delta < timedelta(0)and not devices.ServiceMarketing.Task19_complete_date:
            devices.ServiceMarketing.Task19_alert = True
            devices.ServiceMarketing.Status = 'Delayed'
        if devices.ServiceMarketing.Task20_End_Date and Task20_delta < timedelta(0)and not devices.ServiceMarketing.Task20_complete_date:
            devices.ServiceMarketing.Task20_alert = True
            devices.ServiceMarketing.Status = 'Delayed'

        devices.ServiceMarketing.completed = int(percent)
        devices.ServiceMarketing.save()
        posts1 = devices.ServiceMarketing.task1statusservicemarketing_set.all().order_by('-created')
        posts2 = devices.ServiceMarketing.task2statusservicemarketing_set.all().order_by('-created')
        posts3 = devices.ServiceMarketing.task3statusservicemarketing_set.all().order_by('-created')
        posts4 = devices.ServiceMarketing.task4statusservicemarketing_set.all().order_by('-created')
        posts5 = devices.ServiceMarketing.task5statusservicemarketing_set.all().order_by('-created')
        posts6 = devices.ServiceMarketing.task6statusservicemarketing_set.all().order_by('-created')
        posts7 = devices.ServiceMarketing.task7statusservicemarketing_set.all().order_by('-created')
        posts8 = devices.ServiceMarketing.task8statusservicemarketing_set.all().order_by('-created')
        posts9 = devices.ServiceMarketing.task9statusservicemarketing_set.all().order_by('-created')
        posts10 = devices.ServiceMarketing.task10statusservicemarketing_set.all().order_by('-created')
        posts11 = devices.ServiceMarketing.task11statusservicemarketing_set.all().order_by('-created')
        posts12 = devices.ServiceMarketing.task12statusservicemarketing_set.all().order_by('-created')
        posts13 = devices.ServiceMarketing.task13statusservicemarketing_set.all().order_by('-created')
        posts14 = devices.ServiceMarketing.task14statusservicemarketing_set.all().order_by('-created')
        posts15 = devices.ServiceMarketing.task15statusservicemarketing_set.all().order_by('-created')
        posts16 = devices.ServiceMarketing.task16statusservicemarketing_set.all().order_by('-created')
        posts17 = devices.ServiceMarketing.task17statusservicemarketing_set.all().order_by('-created')
        posts18 = devices.ServiceMarketing.task18statusservicemarketing_set.all().order_by('-created')
        posts19 = devices.ServiceMarketing.task19statusservicemarketing_set.all().order_by('-created')
        posts20 = devices.ServiceMarketing.task20statusservicemarketing_set.all().order_by('-created')

        args = {'devices': devices, 'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5,
                'form6': form6,
                'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12,
                'form13': form13,
                'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17, 'form18': form18,
                'form19': form19,
                'form20': form20, 'posts1': posts1, 'posts2': posts2, 'posts3': posts3, 'posts4': posts4,
                'posts5': posts5, 'posts6': posts6,
                'posts7': posts7, 'posts8': posts8, 'posts9': posts9, 'posts10': posts10, 'posts11': posts11,
                'posts12': posts12, 'posts13': posts13,
                'posts14': posts14, 'posts15': posts15, 'posts16': posts16, 'posts17': posts17, 'posts18': posts18,
                'posts19': posts19,
                'posts20': posts20, 'Task1_vc_dateform': Task1_vc_dateform, 'Task2_vc_dateform': Task2_vc_dateform,
                'Task3_vc_dateform': Task3_vc_dateform, 'Task4_vc_dateform': Task4_vc_dateform,
                'Task5_vc_dateform': Task5_vc_dateform, 'Task6_vc_dateform': Task6_vc_dateform,
                'Task7_vc_dateform': Task7_vc_dateform, 'Task8_vc_dateform': Task8_vc_dateform,
                'Task9_vc_dateform': Task9_vc_dateform, 'Task10_vc_dateform': Task10_vc_dateform,
                'Task11_vc_dateform': Task11_vc_dateform, 'Task12_vc_dateform': Task12_vc_dateform,
                'Task13_vc_dateform': Task13_vc_dateform, 'Task14_vc_dateform': Task14_vc_dateform,
                'Task15_vc_dateform': Task15_vc_dateform, 'Task16_vc_dateform': Task16_vc_dateform,
                'Task17_vc_dateform': Task17_vc_dateform, 'Task18_vc_dateform': Task18_vc_dateform,
                'Task19_vc_dateform': Task19_vc_dateform, 'Task20_vc_dateform': Task20_vc_dateform,
                'Task1_delta': Task1_delta, 'Task7_delta': Task7_delta, 'Task12_delta': Task12_delta,
                'Task17_delta': Task17_delta,
                'Task2_delta': Task2_delta, 'Task8_delta': Task8_delta, 'Task13_delta': Task13_delta,
                'Task3_delta': Task3_delta, 'Task9_delta': Task9_delta, 'Task14_delta': Task14_delta,
                'Task18_delta': Task18_delta,
                'Task4_delta': Task4_delta, 'Task10_delta': Task10_delta, 'Task15_delta': Task15_delta,
                'Task19_delta': Task19_delta,
                'Task5_delta': Task5_delta, 'Task11_delta': Task11_delta, 'Task16_delta': Task16_delta,
                'Task20_delta': Task20_delta,
                'Task6_delta': Task6_delta,
                }
        return render(request, self.template_name, args)

    def post(self, request, pk):

        form1 = Task1_sm_form(request.POST)
        form2 = Task2_sm_form(request.POST)
        form3 = Task3_sm_form(request.POST)
        form4 = Task4_sm_form(request.POST)
        form5 = Task5_sm_form(request.POST)
        form6 = Task6_sm_form(request.POST)
        form7 = Task7_sm_form(request.POST)
        form8 = Task8_sm_form(request.POST)
        form9 = Task9_sm_form(request.POST)
        form10 = Task10_sm_form(request.POST)
        form11 = Task11_sm_form(request.POST)
        form12 = Task12_sm_form(request.POST)
        form13 = Task13_sm_form(request.POST)
        form14 = Task14_sm_form(request.POST)
        form15 = Task15_sm_form(request.POST)
        form16 = Task16_sm_form(request.POST)
        form17 = Task17_sm_form(request.POST)
        form18 = Task18_sm_form(request.POST)
        form19 = Task19_sm_form(request.POST)
        form20 = Task20_sm_form(request.POST)
        devices = Device.objects.get(pk=pk)

        Task1_vc_dateform = Task1_sm_date_form(request.POST, instance=devices.ServiceMarketing)
        Task2_vc_dateform = Task2_sm_date_form(request.POST, instance=devices.ServiceMarketing)
        Task3_vc_dateform = Task3_sm_date_form(request.POST, instance=devices.ServiceMarketing)
        Task4_vc_dateform = Task4_sm_date_form(request.POST, instance=devices.ServiceMarketing)
        Task5_vc_dateform = Task5_sm_date_form(request.POST, instance=devices.ServiceMarketing)
        Task6_vc_dateform = Task6_sm_date_form(request.POST, instance=devices.ServiceMarketing)
        Task7_vc_dateform = Task7_sm_date_form(request.POST, instance=devices.ServiceMarketing)
        Task8_vc_dateform = Task8_sm_date_form(request.POST, instance=devices.ServiceMarketing)
        Task9_vc_dateform = Task9_sm_date_form(request.POST, instance=devices.ServiceMarketing)
        Task10_vc_dateform = Task10_sm_date_form(request.POST, instance=devices.ServiceMarketing)
        Task11_vc_dateform = Task11_sm_date_form(request.POST, instance=devices.ServiceMarketing)
        Task12_vc_dateform = Task12_sm_date_form(request.POST, instance=devices.ServiceMarketing)
        Task13_vc_dateform = Task13_sm_date_form(request.POST, instance=devices.ServiceMarketing)
        Task14_vc_dateform = Task14_sm_date_form(request.POST, instance=devices.ServiceMarketing)
        Task15_vc_dateform = Task15_sm_date_form(request.POST, instance=devices.ServiceMarketing)
        Task16_vc_dateform = Task16_sm_date_form(request.POST, instance=devices.ServiceMarketing)
        Task17_vc_dateform = Task17_sm_date_form(request.POST, instance=devices.ServiceMarketing)
        Task18_vc_dateform = Task18_sm_date_form(request.POST, instance=devices.ServiceMarketing)
        Task19_vc_dateform = Task19_sm_date_form(request.POST, instance=devices.ServiceMarketing)
        Task20_vc_dateform = Task20_sm_date_form(request.POST, instance=devices.ServiceMarketing)

        if 'Task1Submit' in request.POST:
            if form1.is_valid() and Task1_vc_dateform.is_valid():
                post = form1.save(commit=False)
                post.user = request.user
                post.ServiceMarketing = devices.ServiceMarketing
                Task1_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicemarketing')
            else:
                return redirect('/login/summary/' + pk + '/servicemarketing')
        elif 'Task2Submit' in request.POST:
            if form2.is_valid() and Task2_vc_dateform.is_valid():
                post = form2.save(commit=False)
                post.user = request.user
                post.ServiceMarketing = devices.ServiceMarketing
                Task2_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicemarketing')
            else:
                return redirect('/login/summary/' + pk + '/servicemarketing')
        elif 'Task3Submit' in request.POST:
            if form3.is_valid() and Task3_vc_dateform.is_valid():
                post = form3.save(commit=False)
                post.user = request.user
                post.ServiceMarketing = devices.ServiceMarketing
                Task3_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicemarketing')
            else:
                return redirect('/login/summary/' + pk + '/servicemarketing')
        elif 'Task4Submit' in request.POST:
            if form4.is_valid() and Task4_vc_dateform.is_valid():
                post = form4.save(commit=False)
                post.user = request.user
                post.ServiceMarketing = devices.ServiceMarketing
                Task4_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicemarketing')
            else:
                return redirect('/login/summary/' + pk + '/servicemarketing')
        elif 'Task5Submit' in request.POST:
            if form5.is_valid() and Task5_vc_dateform.is_valid():
                post = form5.save(commit=False)
                post.user = request.user
                post.ServiceMarketing = devices.ServiceMarketing
                Task5_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicemarketing')
            else:
                return redirect('/login/summary/' + pk + '/servicemarketing')
        elif 'Task6Submit' in request.POST:
            if form6.is_valid() and Task6_vc_dateform.is_valid():
                post = form6.save(commit=False)
                post.user = request.user
                post.ServiceMarketing = devices.ServiceMarketing
                Task6_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicemarketing')
            else:
                return redirect('/login/summary/' + pk + '/servicemarketing')
        elif 'Task7Submit' in request.POST:
            if form7.is_valid() and Task7_vc_dateform.is_valid():
                post = form7.save(commit=False)
                post.user = request.user
                post.ServiceMarketing = devices.ServiceMarketing
                Task7_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicemarketing')
            else:
                return redirect('/login/summary/' + pk + '/servicemarketing')
        elif 'Task8Submit' in request.POST:
            if form8.is_valid() and Task8_vc_dateform.is_valid():
                post = form8.save(commit=False)
                post.user = request.user
                post.ServiceMarketing = devices.ServiceMarketing
                Task8_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicemarketing')
            else:
                return redirect('/login/summary/' + pk + '/servicemarketing')
        elif 'Task9Submit' in request.POST:
            if form9.is_valid() and Task9_vc_dateform.is_valid():
                post = form9.save(commit=False)
                post.user = request.user
                post.ServiceMarketing = devices.ServiceMarketing
                Task9_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicemarketing')
            else:
                return redirect('/login/summary/' + pk + '/servicemarketing')
        elif 'Task10Submit' in request.POST:
            if form10.is_valid() and Task10_vc_dateform.is_valid():
                post = form10.save(commit=False)
                post.user = request.user
                post.ServiceMarketing = devices.ServiceMarketing
                Task10_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicemarketing')
            else:
                return redirect('/login/summary/' + pk + '/servicemarketing')
        elif 'Task11Submit' in request.POST:
            if form11.is_valid() and Task11_vc_dateform.is_valid():
                post = form11.save(commit=False)
                post.user = request.user
                post.ServiceMarketing = devices.ServiceMarketing
                Task11_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicemarketing')
            else:
                return redirect('/login/summary/' + pk + '/servicemarketing')
        elif 'Task12Submit' in request.POST:
            if form12.is_valid() and Task12_vc_dateform.is_valid():
                post = form12.save(commit=False)
                post.user = request.user
                post.ServiceMarketing = devices.ServiceMarketing
                Task12_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicemarketing')
            else:
                return redirect('/login/summary/' + pk + '/servicemarketing')
        elif 'Task13Submit' in request.POST:
            if form13.is_valid() and Task13_vc_dateform.is_valid():
                post = form13.save(commit=False)
                post.user = request.user
                post.ServiceMarketing = devices.ServiceMarketing
                Task13_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicemarketing')
            else:
                return redirect('/login/summary/' + pk + '/servicemarketing')
        elif 'Task14Submit' in request.POST:
            if form14.is_valid() and Task14_vc_dateform.is_valid():
                post = form14.save(commit=False)
                post.user = request.user
                post.ServiceMarketing = devices.ServiceMarketing
                Task14_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicemarketing')
            else:
                return redirect('/login/summary/' + pk + '/servicemarketing')
        elif 'Task15Submit' in request.POST:
            if form15.is_valid() and Task15_vc_dateform.is_valid():
                post = form15.save(commit=False)
                post.user = request.user
                post.ServiceMarketing = devices.ServiceMarketing
                Task15_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicemarketing')
            else:
                return redirect('/login/summary/' + pk + '/servicemarketing')
        elif 'Task16Submit' in request.POST:
            if form16.is_valid() and Task16_vc_dateform.is_valid():
                post = form16.save(commit=False)
                post.user = request.user
                post.ServiceMarketing = devices.ServiceMarketing
                Task16_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicemarketing')
            else:
                return redirect('/login/summary/' + pk + '/servicemarketing')
        elif 'Task17Submit' in request.POST:
            if form17.is_valid() and Task17_vc_dateform.is_valid():
                post = form17.save(commit=False)
                post.user = request.user
                post.ServiceMarketing = devices.ServiceMarketing
                Task17_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicemarketing')
            else:
                return redirect('/login/summary/' + pk + '/servicemarketing')
        elif 'Task18Submit' in request.POST:
            if form18.is_valid() and Task18_vc_dateform.is_valid():
                post = form18.save(commit=False)
                post.user = request.user
                post.ServiceMarketing = devices.ServiceMarketing
                Task18_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicemarketing')
            else:
                return redirect('/login/summary/' + pk + '/servicemarketing')
        elif 'Task19Submit' in request.POST:
            if form19.is_valid() and Task19_vc_dateform.is_valid():
                post = form19.save(commit=False)
                post.user = request.user
                post.ServiceMarketing = devices.ServiceMarketing
                Task19_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicemarketing')
            else:
                return redirect('/login/summary/' + pk + '/servicemarketing')
        elif 'Task20Submit' in request.POST:
            if form20.is_valid() and Task20_vc_dateform.is_valid():
                post = form20.save(commit=False)
                post.user = request.user
                post.ServiceMarketing = devices.ServiceMarketing
                Task20_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicemarketing')
            else:
                return redirect('/login/summary/' + pk + '/servicemarketing')


########################################################################################################################

class ServiceTrainingView(LoginRequiredMixin,TemplateView):
    template_name = 'login/device11.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        form1 = Task1_st_form()
        form2 = Task2_st_form()
        form3 = Task3_st_form()
        form4 = Task4_st_form()
        form5 = Task5_st_form()
        form6 = Task6_st_form()
        form7 = Task7_st_form()
        form8 = Task8_st_form()
        form9 = Task9_st_form()
        form10 = Task10_st_form()
        form11 = Task11_st_form()
        form12 = Task12_st_form()
        form13 = Task13_st_form()
        form14 = Task14_st_form()
        form15 = Task15_st_form()
        form16 = Task16_st_form()
        form17 = Task17_st_form()
        form18 = Task18_st_form()
        form19 = Task19_st_form()
        form20 = Task20_st_form()
        devices = Device.objects.get(pk=pk)
        Task1_vc_dateform = Task1_st_date_form(instance=devices.ServiceTraining)
        Task2_vc_dateform = Task2_st_date_form(instance=devices.ServiceTraining)
        Task3_vc_dateform = Task3_st_date_form(instance=devices.ServiceTraining)
        Task4_vc_dateform = Task4_st_date_form(instance=devices.ServiceTraining)
        Task5_vc_dateform = Task5_st_date_form(instance=devices.ServiceTraining)
        Task6_vc_dateform = Task6_st_date_form(instance=devices.ServiceTraining)
        Task7_vc_dateform = Task7_st_date_form(instance=devices.ServiceTraining)
        Task8_vc_dateform = Task8_st_date_form(instance=devices.ServiceTraining)
        Task9_vc_dateform = Task9_st_date_form(instance=devices.ServiceTraining)
        Task10_vc_dateform = Task10_st_date_form(instance=devices.ServiceTraining)
        Task11_vc_dateform = Task11_st_date_form(instance=devices.ServiceTraining)
        Task12_vc_dateform = Task12_st_date_form(instance=devices.ServiceTraining)
        Task13_vc_dateform = Task13_st_date_form(instance=devices.ServiceTraining)
        Task14_vc_dateform = Task14_st_date_form(instance=devices.ServiceTraining)
        Task15_vc_dateform = Task15_st_date_form(instance=devices.ServiceTraining)
        Task16_vc_dateform = Task16_st_date_form(instance=devices.ServiceTraining)
        Task17_vc_dateform = Task17_st_date_form(instance=devices.ServiceTraining)
        Task18_vc_dateform = Task18_st_date_form(instance=devices.ServiceTraining)
        Task19_vc_dateform = Task19_st_date_form(instance=devices.ServiceTraining)
        Task20_vc_dateform = Task20_st_date_form(instance=devices.ServiceTraining)

        # Calculating % completed
        y = 0
        if devices.ServiceTraining.Task1_Name:
            y = y + 1
        if devices.ServiceTraining.Task2_Name:
            y = y + 1
        if devices.ServiceTraining.Task3_Name:
            y = y + 1
        if devices.ServiceTraining.Task4_Name:
            y = y + 1
        if devices.ServiceTraining.Task5_Name:
            y = y + 1
        if devices.ServiceTraining.Task6_Name:
            y = y + 1
        if devices.ServiceTraining.Task7_Name:
            y = y + 1
        if devices.ServiceTraining.Task8_Name:
            y = y + 1
        if devices.ServiceTraining.Task9_Name:
            y = y + 1
        if devices.ServiceTraining.Task10_Name:
            y = y + 1
        if devices.ServiceTraining.Task11_Name:
            y = y + 1
        if devices.ServiceTraining.Task12_Name:
            y = y + 1
        if devices.ServiceTraining.Task13_Name:
            y = y + 1
        if devices.ServiceTraining.Task14_Name:
            y = y + 1
        if devices.ServiceTraining.Task15_Name:
            y = y + 1
        if devices.ServiceTraining.Task16_Name:
            y = y + 1
        if devices.ServiceTraining.Task17_Name:
            y = y + 1
        if devices.ServiceTraining.Task18_Name:
            y = y + 1
        if devices.ServiceTraining.Task19_Name:
            y = y + 1
        if devices.ServiceTraining.Task20_Name:
            y = y + 1


        x = 0
        if devices.ServiceTraining.Task1_complete_date:
            x =x+1
            devices.ServiceTraining.Task1_alert = False
            devices.ServiceTraining.Task1_warning=False
            devices.ServiceTraining.Status='On_Time'
        if devices.ServiceTraining.Task2_complete_date:
            x = x + 1
            devices.ServiceTraining.Task2_alert = False
            devices.ServiceTraining.Task2_warning=False
            devices.ServiceTraining.Status = 'On_Time'
        if devices.ServiceTraining.Task3_complete_date:
            x = x + 1
            devices.ServiceTraining.Task3_alert = False
            devices.ServiceTraining.Task3_warning=False
            devices.ServiceTraining.Status = 'On_Time'
        if devices.ServiceTraining.Task4_complete_date:
            x = x + 1
            devices.ServiceTraining.Task4_alert = False
            devices.ServiceTraining.Task4_warning=False
            devices.ServiceTraining.Status = 'On_Time'
        if devices.ServiceTraining.Task5_complete_date:
            x = x + 1
            devices.ServiceTraining.Task5_alert = False
            devices.ServiceTraining.Task5_warning=False
            devices.ServiceTraining.Status = 'On_Time'
        if devices.ServiceTraining.Task6_complete_date:
            x = x + 1
            devices.ServiceTraining.Task6_alert = False
            devices.ServiceTraining.Task6_warning=False
            devices.ServiceTraining.Status = 'On_Time'
        if devices.ServiceTraining.Task7_complete_date:
            x =x+1
            devices.ServiceTraining.Task7_alert = False
            devices.ServiceTraining.Task7_warning=False
            devices.ServiceTraining.Status = 'On_Time'
        if devices.ServiceTraining.Task8_complete_date:
            x =x+1
            devices.ServiceTraining.Task8_alert = False
            devices.ServiceTraining.Task8_warning=False
            devices.ServiceTraining.Status = 'On_Time'
        if devices.ServiceTraining.Task9_complete_date:
            x =x+1
            devices.ServiceTraining.Task9_alert = False
            devices.ServiceTraining.Task9_warning=False
            devices.ServiceTraining.Status = 'On_Time'
        if devices.ServiceTraining.Task10_complete_date:
            x =x+1
            devices.ServiceTraining.Task10_alert = False
            devices.ServiceTraining.Task10_warning=False
            devices.ServiceTraining.Status = 'On_Time'
        if devices.ServiceTraining.Task11_complete_date:
            x =x+1
            devices.ServiceTraining.Task11_alert = False
            devices.ServiceTraining.Task11_warning=False
            devices.ServiceTraining.Status = 'On_Time'
        if devices.ServiceTraining.Task12_complete_date:
            x = x + 1
            devices.ServiceTraining.Task12_alert = False
            devices.ServiceTraining.Task12_warning=False
            devices.ServiceTraining.Status = 'On_Time'
        if devices.ServiceTraining.Task13_complete_date:
            x = x + 1
            devices.ServiceTraining.Task13_alert = False
            devices.ServiceTraining.Task13_warning=False
            devices.ServiceTraining.Status = 'On_Time'
        if devices.ServiceTraining.Task14_complete_date:
            x = x + 1
            devices.ServiceTraining.Task14_alert = False
            devices.ServiceTraining.Task14_warning=False
            devices.ServiceTraining.Status = 'On_Time'
        if devices.ServiceTraining.Task15_complete_date:
            x = x + 1
            devices.ServiceTraining.Task15_alert = False
            devices.ServiceTraining.Task15_warning=False
            devices.ServiceTraining.Status = 'On_Time'
        if devices.ServiceTraining.Task16_complete_date:
            x = x + 1
            devices.ServiceTraining.Task16_alert = False
            devices.ServiceTraining.Task16_warning=False
            devices.ServiceTraining.Status = 'On_Time'
        if devices.ServiceTraining.Task17_complete_date:
            x =x+1
            devices.ServiceTraining.Task17_alert = False
            devices.ServiceTraining.Task17_warning=False
            devices.ServiceTraining.Status = 'On_Time'
        if devices.ServiceTraining.Task18_complete_date:
            x =x+1
            devices.ServiceTraining.Task18_alert = False
            devices.ServiceTraining.Task18_warning=False
            devices.ServiceTraining.Status = 'On_Time'
        if devices.ServiceTraining.Task19_complete_date:
            x =x+1
            devices.ServiceTraining.Task19_alert = False
            devices.ServiceTraining.Task19_warning=False
            devices.ServiceTraining.Status = 'On_Time'
        if devices.ServiceTraining.Task20_complete_date:
            x =x+1
            devices.ServiceTraining.Task20_alert = False
            devices.ServiceTraining.Task20_warning=False
            devices.ServiceTraining.Status = 'On_Time'
        percent = x/y * 100
        print (percent)

        #alerting logic
        today = datetime.date.today()
        if devices.ServiceTraining.Task1_End_Date:
            Task1_delta =  devices.ServiceTraining.Task1_End_Date - today
        else:
            Task1_delta = None
        if devices.ServiceTraining.Task2_End_Date:
            Task2_delta = devices.ServiceTraining.Task2_End_Date - today
        else:
            Task2_delta = None
        if devices.ServiceTraining.Task3_End_Date:
            Task3_delta = devices.ServiceTraining.Task3_End_Date - today
        else:
            Task3_delta = None
        if devices.ServiceTraining.Task4_End_Date:
            Task4_delta = devices.ServiceTraining.Task4_End_Date - today
        else:
            Task4_delta = None
        if devices.ServiceTraining.Task5_End_Date:
            Task5_delta = devices.ServiceTraining.Task5_End_Date - today
        else:
            Task5_delta = None
        if devices.ServiceTraining.Task6_End_Date:
            Task6_delta = devices.ServiceTraining.Task6_End_Date - today
        else:
            Task6_delta = None
        if devices.ServiceTraining.Task7_End_Date:
            Task7_delta = devices.ServiceTraining.Task7_End_Date - today
        else:
            Task7_delta = None
        if devices.ServiceTraining.Task8_End_Date:
            Task8_delta = devices.ServiceTraining.Task8_End_Date - today
        else:
            Task8_delta = None
        if devices.ServiceTraining.Task9_End_Date:
            Task9_delta = devices.ServiceTraining.Task9_End_Date - today
        else:
            Task9_delta = None
        if devices.ServiceTraining.Task10_End_Date:
            Task10_delta =  devices.ServiceTraining.Task10_End_Date - today
        else:
            Task10_delta = None
        if devices.ServiceTraining.Task11_End_Date:
            Task11_delta =  devices.ServiceTraining.Task11_End_Date - today
        else:
            Task11_delta = None
        if devices.ServiceTraining.Task12_End_Date:
            Task12_delta = devices.ServiceTraining.Task12_End_Date - today
        else:
            Task12_delta = None
        if devices.ServiceTraining.Task13_End_Date:
            Task13_delta = devices.ServiceTraining.Task13_End_Date - today
        else:
            Task13_delta = None
        if devices.ServiceTraining.Task14_End_Date:
            Task14_delta = devices.ServiceTraining.Task14_End_Date - today
        else:
            Task14_delta = None
        if devices.ServiceTraining.Task15_End_Date:
            Task15_delta = devices.ServiceTraining.Task15_End_Date - today
        else:
            Task15_delta = None
        if devices.ServiceTraining.Task16_End_Date:
            Task16_delta = devices.ServiceTraining.Task16_End_Date - today
        else:
            Task16_delta = None
        if devices.ServiceTraining.Task17_End_Date:
            Task17_delta = devices.ServiceTraining.Task17_End_Date - today
        else:
            Task17_delta = None
        if devices.ServiceTraining.Task18_End_Date:
            Task18_delta = devices.ServiceTraining.Task18_End_Date - today
        else:
            Task18_delta = None
        if devices.ServiceTraining.Task19_End_Date:
            Task19_delta = devices.ServiceTraining.Task19_End_Date - today
        else:
            Task19_delta = None
        if devices.ServiceTraining.Task20_End_Date:
            Task20_delta = devices.ServiceTraining.Task20_End_Date - today
        else:
            Task20_delta = None


        if Task1_delta and Task1_delta < timedelta(devices.ServiceTraining.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not devices.ServiceTraining.Task1_complete_date:
            devices.ServiceTraining.Task1_warning = True
            devices.ServiceTraining.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(devices.ServiceTraining.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not devices.ServiceTraining.Task2_complete_date:
            devices.ServiceTraining.Task2_warning = True
            devices.ServiceTraining.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(devices.ServiceTraining.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not devices.ServiceTraining.Task3_complete_date:
            devices.ServiceTraining.Task3_warning = True
            devices.ServiceTraining.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(devices.ServiceTraining.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not devices.ServiceTraining.Task4_complete_date:
            devices.ServiceTraining.Task4_warning = True
            devices.ServiceTraining.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(devices.ServiceTraining.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not devices.ServiceTraining.Task5_complete_date:
            devices.ServiceTraining.Task5_warning = True
            devices.ServiceTraining.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(devices.ServiceTraining.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not devices.ServiceTraining.Task6_complete_date:
            devices.ServiceTraining.Task6_warning = True
            devices.ServiceTraining.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(devices.ServiceTraining.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not devices.ServiceTraining.Task7_complete_date:
            devices.ServiceTraining.Task7_warning = True
            devices.ServiceTraining.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(devices.ServiceTraining.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not devices.ServiceTraining.Task8_complete_date:
            devices.ServiceTraining.Task8_warning = True
            devices.ServiceTraining.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(devices.ServiceTraining.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not devices.ServiceTraining.Task9_complete_date:
            devices.ServiceTraining.Task9_warning = True
            devices.ServiceTraining.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(devices.ServiceTraining.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not devices.ServiceTraining.Task10_complete_date:
            devices.ServiceTraining.Task10_warning = True
            devices.ServiceTraining.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(devices.ServiceTraining.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not devices.ServiceTraining.Task11_complete_date:
            devices.ServiceTraining.Task11_warning = True
            devices.ServiceTraining.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(devices.ServiceTraining.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not devices.ServiceTraining.Task12_complete_date:
            devices.ServiceTraining.Task12_warning = True
            devices.ServiceTraining.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(devices.ServiceTraining.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not devices.ServiceTraining.Task13_complete_date:
            devices.ServiceTraining.Task13_warning = True
            devices.ServiceTraining.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(devices.ServiceTraining.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not devices.ServiceTraining.Task14_complete_date:
            devices.ServiceTraining.Task14_warning = True
            devices.ServiceTraining.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(devices.ServiceTraining.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not devices.ServiceTraining.Task15_complete_date:
            devices.ServiceTraining.Task15_warning = True
            devices.ServiceTraining.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(devices.ServiceTraining.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not devices.ServiceTraining.Task16_complete_date:
            devices.ServiceTraining.Task16_warning = True
            devices.ServiceTraining.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(devices.ServiceTraining.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not devices.ServiceTraining.Task17_complete_date:
            devices.ServiceTraining.Task17_warning = True
            devices.ServiceTraining.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(devices.ServiceTraining.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not devices.ServiceTraining.Task18_complete_date:
            devices.ServiceTraining.Task18_warning = True
            devices.ServiceTraining.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(devices.ServiceTraining.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not devices.ServiceTraining.Task19_complete_date:
            devices.ServiceTraining.Task19_warning = True
            devices.ServiceTraining.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(devices.ServiceTraining.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not devices.ServiceTraining.Task20_complete_date:
            devices.ServiceTraining.Task20_warning = True
            devices.ServiceTraining.Status = 'At Risk'

        if devices.ServiceTraining.Task1_End_Date and Task1_delta < timedelta(0) and not devices.ServiceTraining.Task1_complete_date:
            devices.ServiceTraining.Task1_alert = True
            devices.ServiceTraining.Status = 'Delayed'
        if devices.ServiceTraining.Task2_End_Date and Task2_delta < timedelta(0) and not devices.ServiceTraining.Task2_complete_date:
            devices.ServiceTraining.Task2_alert = True
            devices.ServiceTraining.Status = 'Delayed'
        if devices.ServiceTraining.Task3_End_Date and Task3_delta < timedelta(0) and not devices.ServiceTraining.Task3_complete_date:
            devices.ServiceTraining.Task3_alert = True
            devices.ServiceTraining.Status = 'Delayed'
        if devices.ServiceTraining.Task4_End_Date and Task4_delta < timedelta(0) and not devices.ServiceTraining.Task4_complete_date:
            devices.ServiceTraining.Task4_alert = True
            devices.ServiceTraining.Status = 'Delayed'
        if devices.ServiceTraining.Task5_End_Date and Task5_delta < timedelta(0) and not devices.ServiceTraining.Task5_complete_date:
            devices.ServiceTraining.Task5_alert = True
            devices.ServiceTraining.Status = 'Delayed'
        if devices.ServiceTraining.Task6_End_Date and Task6_delta < timedelta(0) and not devices.ServiceTraining.Task6_complete_date:
            devices.ServiceTraining.Task6_alert = True
            devices.ServiceTraining.Status = 'Delayed'
        if devices.ServiceTraining.Task7_End_Date and Task7_delta < timedelta(0) and not devices.ServiceTraining.Task7_complete_date:
            devices.ServiceTraining.Task7_alert = True
            devices.ServiceTraining.Status = 'Delayed'
        if devices.ServiceTraining.Task8_End_Date and Task8_delta < timedelta(0)and not devices.ServiceTraining.Task8_complete_date:
            devices.ServiceTraining.Task8_alert = True
            devices.ServiceTraining.Status = 'Delayed'
        if devices.ServiceTraining.Task9_End_Date and Task9_delta < timedelta(0)and not devices.ServiceTraining.Task9_complete_date:
            devices.ServiceTraining.Task9_alert = True
            devices.ServiceTraining.Status = 'Delayed'
        if devices.ServiceTraining.Task10_End_Date and Task10_delta < timedelta(0) and not devices.ServiceTraining.Task10_complete_date:
            devices.ServiceTraining.Task10_alert = True
            devices.ServiceTraining.Status = 'Delayed'
        if devices.ServiceTraining.Task11_End_Date and Task11_delta < timedelta(0) and not devices.ServiceTraining.Task11_complete_date:
            devices.ServiceTraining.Task11_alert = True
            devices.ServiceTraining.Status = 'Delayed'
        if devices.ServiceTraining.Task12_End_Date and Task12_delta < timedelta(0) and not devices.ServiceTraining.Task12_complete_date:
            devices.ServiceTraining.Task12_alert = True
            devices.ServiceTraining.Status = 'Delayed'
        if devices.ServiceTraining.Task13_End_Date and Task13_delta < timedelta(0) and not devices.ServiceTraining.Task13_complete_date:
            devices.ServiceTraining.Task13_alert = True
            devices.ServiceTraining.Status = 'Delayed'
        if devices.ServiceTraining.Task14_End_Date and Task14_delta < timedelta(0) and not devices.ServiceTraining.Task14_complete_date:
            devices.ServiceTraining.Task14_alert = True
            devices.ServiceTraining.Status = 'Delayed'
        if devices.ServiceTraining.Task15_End_Date and Task15_delta < timedelta(0) and not devices.ServiceTraining.Task15_complete_date:
            devices.ServiceTraining.Task15_alert = True
            devices.ServiceTraining.Status = 'Delayed'
        if devices.ServiceTraining.Task16_End_Date and Task16_delta < timedelta(0) and not devices.ServiceTraining.Task16_complete_date:
            devices.ServiceTraining.Task16_alert = True
            devices.ServiceTraining.Status = 'Delayed'
        if devices.ServiceTraining.Task17_End_Date and Task17_delta < timedelta(0)and not devices.ServiceTraining.Task17_complete_date:
            devices.ServiceTraining.Task17_alert = True
            devices.ServiceTraining.Status = 'Delayed'
        if devices.ServiceTraining.Task18_End_Date and Task18_delta < timedelta(0)and not devices.ServiceTraining.Task18_complete_date:
            devices.ServiceTraining.Task18_alert = True
            devices.ServiceTraining.Status = 'Delayed'
        if devices.ServiceTraining.Task19_End_Date and Task19_delta < timedelta(0)and not devices.ServiceTraining.Task19_complete_date:
            devices.ServiceTraining.Task19_alert = True
            devices.ServiceTraining.Status = 'Delayed'
        if devices.ServiceTraining.Task20_End_Date and Task20_delta < timedelta(0)and not devices.ServiceTraining.Task20_complete_date:
            devices.ServiceTraining.Task20_alert = True
            devices.ServiceTraining.Status = 'Delayed'

        devices.ServiceTraining.completed = int(percent)
        devices.ServiceTraining.save()
        posts1 = devices.ServiceTraining.task1statusservicetraining_set.all().order_by('-created')
        posts2 = devices.ServiceTraining.task2statusservicetraining_set.all().order_by('-created')
        posts3 = devices.ServiceTraining.task3statusservicetraining_set.all().order_by('-created')
        posts4 = devices.ServiceTraining.task4statusservicetraining_set.all().order_by('-created')
        posts5 = devices.ServiceTraining.task5statusservicetraining_set.all().order_by('-created')
        posts6 = devices.ServiceTraining.task6statusservicetraining_set.all().order_by('-created')
        posts7 = devices.ServiceTraining.task7statusservicetraining_set.all().order_by('-created')
        posts8 = devices.ServiceTraining.task8statusservicetraining_set.all().order_by('-created')
        posts9 = devices.ServiceTraining.task9statusservicetraining_set.all().order_by('-created')
        posts10 = devices.ServiceTraining.task10statusservicetraining_set.all().order_by('-created')
        posts11 = devices.ServiceTraining.task11statusservicetraining_set.all().order_by('-created')
        posts12 = devices.ServiceTraining.task12statusservicetraining_set.all().order_by('-created')
        posts13 = devices.ServiceTraining.task13statusservicetraining_set.all().order_by('-created')
        posts14 = devices.ServiceTraining.task14statusservicetraining_set.all().order_by('-created')
        posts15 = devices.ServiceTraining.task15statusservicetraining_set.all().order_by('-created')
        posts16 = devices.ServiceTraining.task16statusservicetraining_set.all().order_by('-created')
        posts17 = devices.ServiceTraining.task17statusservicetraining_set.all().order_by('-created')
        posts18 = devices.ServiceTraining.task18statusservicetraining_set.all().order_by('-created')
        posts19 = devices.ServiceTraining.task19statusservicetraining_set.all().order_by('-created')
        posts20 = devices.ServiceTraining.task20statusservicetraining_set.all().order_by('-created')

        args = {'devices': devices, 'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5,
                'form6': form6,
                'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12,
                'form13': form13,
                'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17, 'form18': form18,
                'form19': form19,
                'form20': form20, 'posts1': posts1, 'posts2': posts2, 'posts3': posts3, 'posts4': posts4,
                'posts5': posts5, 'posts6': posts6,
                'posts7': posts7, 'posts8': posts8, 'posts9': posts9, 'posts10': posts10, 'posts11': posts11,
                'posts12': posts12, 'posts13': posts13,
                'posts14': posts14, 'posts15': posts15, 'posts16': posts16, 'posts17': posts17, 'posts18': posts18,
                'posts19': posts19,
                'posts20': posts20, 'Task1_vc_dateform': Task1_vc_dateform, 'Task2_vc_dateform': Task2_vc_dateform,
                'Task3_vc_dateform': Task3_vc_dateform, 'Task4_vc_dateform': Task4_vc_dateform,
                'Task5_vc_dateform': Task5_vc_dateform, 'Task6_vc_dateform': Task6_vc_dateform,
                'Task7_vc_dateform': Task7_vc_dateform, 'Task8_vc_dateform': Task8_vc_dateform,
                'Task9_vc_dateform': Task9_vc_dateform, 'Task10_vc_dateform': Task10_vc_dateform,
                'Task11_vc_dateform': Task11_vc_dateform, 'Task12_vc_dateform': Task12_vc_dateform,
                'Task13_vc_dateform': Task13_vc_dateform, 'Task14_vc_dateform': Task14_vc_dateform,
                'Task15_vc_dateform': Task15_vc_dateform, 'Task16_vc_dateform': Task16_vc_dateform,
                'Task17_vc_dateform': Task17_vc_dateform, 'Task18_vc_dateform': Task18_vc_dateform,
                'Task19_vc_dateform': Task19_vc_dateform, 'Task20_vc_dateform': Task20_vc_dateform,
                'Task1_delta': Task1_delta, 'Task7_delta': Task7_delta, 'Task12_delta': Task12_delta,
                'Task17_delta': Task17_delta,
                'Task2_delta': Task2_delta, 'Task8_delta': Task8_delta, 'Task13_delta': Task13_delta,
                'Task3_delta': Task3_delta, 'Task9_delta': Task9_delta, 'Task14_delta': Task14_delta,
                'Task18_delta': Task18_delta,
                'Task4_delta': Task4_delta, 'Task10_delta': Task10_delta, 'Task15_delta': Task15_delta,
                'Task19_delta': Task19_delta,
                'Task5_delta': Task5_delta, 'Task11_delta': Task11_delta, 'Task16_delta': Task16_delta,
                'Task20_delta': Task20_delta,
                'Task6_delta': Task6_delta,
                }
        return render(request, self.template_name, args)

    def post(self, request, pk):

        form1 = Task1_st_form(request.POST)
        form2 = Task2_st_form(request.POST)
        form3 = Task3_st_form(request.POST)
        form4 = Task4_st_form(request.POST)
        form5 = Task5_st_form(request.POST)
        form6 = Task6_st_form(request.POST)
        form7 = Task7_st_form(request.POST)
        form8 = Task8_st_form(request.POST)
        form9 = Task9_st_form(request.POST)
        form10 = Task10_st_form(request.POST)
        form11 = Task11_st_form(request.POST)
        form12 = Task12_st_form(request.POST)
        form13 = Task13_st_form(request.POST)
        form14 = Task14_st_form(request.POST)
        form15 = Task15_st_form(request.POST)
        form16 = Task16_st_form(request.POST)
        form17 = Task17_st_form(request.POST)
        form18 = Task18_st_form(request.POST)
        form19 = Task19_st_form(request.POST)
        form20 = Task20_st_form(request.POST)
        devices = Device.objects.get(pk=pk)

        Task1_vc_dateform = Task1_st_date_form(request.POST, instance=devices.ServiceTraining)
        Task2_vc_dateform = Task2_st_date_form(request.POST, instance=devices.ServiceTraining)
        Task3_vc_dateform = Task3_st_date_form(request.POST, instance=devices.ServiceTraining)
        Task4_vc_dateform = Task4_st_date_form(request.POST, instance=devices.ServiceTraining)
        Task5_vc_dateform = Task5_st_date_form(request.POST, instance=devices.ServiceTraining)
        Task6_vc_dateform = Task6_st_date_form(request.POST, instance=devices.ServiceTraining)
        Task7_vc_dateform = Task7_st_date_form(request.POST, instance=devices.ServiceTraining)
        Task8_vc_dateform = Task8_st_date_form(request.POST, instance=devices.ServiceTraining)
        Task9_vc_dateform = Task9_st_date_form(request.POST, instance=devices.ServiceTraining)
        Task10_vc_dateform = Task10_st_date_form(request.POST, instance=devices.ServiceTraining)
        Task11_vc_dateform = Task11_st_date_form(request.POST, instance=devices.ServiceTraining)
        Task12_vc_dateform = Task12_st_date_form(request.POST, instance=devices.ServiceTraining)
        Task13_vc_dateform = Task13_st_date_form(request.POST, instance=devices.ServiceTraining)
        Task14_vc_dateform = Task14_st_date_form(request.POST, instance=devices.ServiceTraining)
        Task15_vc_dateform = Task15_st_date_form(request.POST, instance=devices.ServiceTraining)
        Task16_vc_dateform = Task16_st_date_form(request.POST, instance=devices.ServiceTraining)
        Task17_vc_dateform = Task17_st_date_form(request.POST, instance=devices.ServiceTraining)
        Task18_vc_dateform = Task18_st_date_form(request.POST, instance=devices.ServiceTraining)
        Task19_vc_dateform = Task19_st_date_form(request.POST, instance=devices.ServiceTraining)
        Task20_vc_dateform = Task20_st_date_form(request.POST, instance=devices.ServiceTraining)

        if 'Task1Submit' in request.POST:
            if form1.is_valid() and Task1_vc_dateform.is_valid():
                post = form1.save(commit=False)
                post.user = request.user
                post.ServiceTraining = devices.ServiceTraining
                Task1_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicetraining')
            else:
                return redirect('/login/summary/' + pk + '/servicetraining')
        elif 'Task2Submit' in request.POST:
            if form2.is_valid() and Task2_vc_dateform.is_valid():
                post = form2.save(commit=False)
                post.user = request.user
                post.ServiceTraining = devices.ServiceTraining
                Task2_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicetraining')
            else:
                return redirect('/login/summary/' + pk + '/servicetraining')
        elif 'Task3Submit' in request.POST:
            if form3.is_valid() and Task3_vc_dateform.is_valid():
                post = form3.save(commit=False)
                post.user = request.user
                post.ServiceTraining = devices.ServiceTraining
                Task3_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicetraining')
            else:
                return redirect('/login/summary/' + pk + '/servicetraining')
        elif 'Task4Submit' in request.POST:
            if form4.is_valid() and Task4_vc_dateform.is_valid():
                post = form4.save(commit=False)
                post.user = request.user
                post.ServiceTraining = devices.ServiceTraining
                Task4_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicetraining')
            else:
                return redirect('/login/summary/' + pk + '/servicetraining')
        elif 'Task5Submit' in request.POST:
            if form5.is_valid() and Task5_vc_dateform.is_valid():
                post = form5.save(commit=False)
                post.user = request.user
                post.ServiceTraining = devices.ServiceTraining
                Task5_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicetraining')
            else:
                return redirect('/login/summary/' + pk + '/servicetraining')
        elif 'Task6Submit' in request.POST:
            if form6.is_valid() and Task6_vc_dateform.is_valid():
                post = form6.save(commit=False)
                post.user = request.user
                post.ServiceTraining = devices.ServiceTraining
                Task6_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicetraining')
            else:
                return redirect('/login/summary/' + pk + '/servicetraining')
        elif 'Task7Submit' in request.POST:
            if form7.is_valid() and Task7_vc_dateform.is_valid():
                post = form7.save(commit=False)
                post.user = request.user
                post.ServiceTraining = devices.ServiceTraining
                Task7_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicetraining')
            else:
                return redirect('/login/summary/' + pk + '/servicetraining')
        elif 'Task8Submit' in request.POST:
            if form8.is_valid() and Task8_vc_dateform.is_valid():
                post = form8.save(commit=False)
                post.user = request.user
                post.ServiceTraining = devices.ServiceTraining
                Task8_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicetraining')
            else:
                return redirect('/login/summary/' + pk + '/servicetraining')
        elif 'Task9Submit' in request.POST:
            if form9.is_valid() and Task9_vc_dateform.is_valid():
                post = form9.save(commit=False)
                post.user = request.user
                post.ServiceTraining = devices.ServiceTraining
                Task9_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicetraining')
            else:
                return redirect('/login/summary/' + pk + '/servicetraining')
        elif 'Task10Submit' in request.POST:
            if form10.is_valid() and Task10_vc_dateform.is_valid():
                post = form10.save(commit=False)
                post.user = request.user
                post.ServiceTraining = devices.ServiceTraining
                Task10_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicetraining')
            else:
                return redirect('/login/summary/' + pk + '/servicetraining')
        elif 'Task11Submit' in request.POST:
            if form11.is_valid() and Task11_vc_dateform.is_valid():
                post = form11.save(commit=False)
                post.user = request.user
                post.ServiceTraining = devices.ServiceTraining
                Task11_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicetraining')
            else:
                return redirect('/login/summary/' + pk + '/servicetraining')
        elif 'Task12Submit' in request.POST:
            if form12.is_valid() and Task12_vc_dateform.is_valid():
                post = form12.save(commit=False)
                post.user = request.user
                post.ServiceTraining = devices.ServiceTraining
                Task12_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicetraining')
            else:
                return redirect('/login/summary/' + pk + '/servicetraining')
        elif 'Task13Submit' in request.POST:
            if form13.is_valid() and Task13_vc_dateform.is_valid():
                post = form13.save(commit=False)
                post.user = request.user
                post.ServiceTraining = devices.ServiceTraining
                Task13_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicetraining')
            else:
                return redirect('/login/summary/' + pk + '/servicetraining')
        elif 'Task14Submit' in request.POST:
            if form14.is_valid() and Task14_vc_dateform.is_valid():
                post = form14.save(commit=False)
                post.user = request.user
                post.ServiceTraining = devices.ServiceTraining
                Task14_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicetraining')
            else:
                return redirect('/login/summary/' + pk + '/servicetraining')
        elif 'Task15Submit' in request.POST:
            if form15.is_valid() and Task15_vc_dateform.is_valid():
                post = form15.save(commit=False)
                post.user = request.user
                post.ServiceTraining = devices.ServiceTraining
                Task15_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicetraining')
            else:
                return redirect('/login/summary/' + pk + '/servicetraining')
        elif 'Task16Submit' in request.POST:
            if form16.is_valid() and Task16_vc_dateform.is_valid():
                post = form16.save(commit=False)
                post.user = request.user
                post.ServiceTraining = devices.ServiceTraining
                Task16_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicetraining')
            else:
                return redirect('/login/summary/' + pk + '/servicetraining')
        elif 'Task17Submit' in request.POST:
            if form17.is_valid() and Task17_vc_dateform.is_valid():
                post = form17.save(commit=False)
                post.user = request.user
                post.ServiceTraining = devices.ServiceTraining
                Task17_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicetraining')
            else:
                return redirect('/login/summary/' + pk + '/servicetraining')
        elif 'Task18Submit' in request.POST:
            if form18.is_valid() and Task18_vc_dateform.is_valid():
                post = form18.save(commit=False)
                post.user = request.user
                post.ServiceTraining = devices.ServiceTraining
                Task18_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicetraining')
            else:
                return redirect('/login/summary/' + pk + '/servicetraining')
        elif 'Task19Submit' in request.POST:
            if form19.is_valid() and Task19_vc_dateform.is_valid():
                post = form19.save(commit=False)
                post.user = request.user
                post.ServiceTraining = devices.ServiceTraining
                Task19_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicetraining')
            else:
                return redirect('/login/summary/' + pk + '/servicetraining')
        elif 'Task20Submit' in request.POST:
            if form20.is_valid() and Task20_vc_dateform.is_valid():
                post = form20.save(commit=False)
                post.user = request.user
                post.ServiceTraining = devices.ServiceTraining
                Task20_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/servicetraining')
            else:
                return redirect('/login/summary/' + pk + '/servicetraining')

########################################################################################################################

class PartsView(LoginRequiredMixin,TemplateView):
    template_name = 'login/device12.html'
    login_url = '/login/auth/'

    def get(self, request, pk):
        form1 = Task1_p_form()
        form2 = Task2_p_form()
        form3 = Task3_p_form()
        form4 = Task4_p_form()
        form5 = Task5_p_form()
        form6 = Task6_p_form()
        form7 = Task7_p_form()
        form8 = Task8_p_form()
        form9 = Task9_p_form()
        form10 = Task10_p_form()
        form11 = Task11_p_form()
        form12 = Task12_p_form()
        form13 = Task13_p_form()
        form14 = Task14_p_form()
        form15 = Task15_p_form()
        form16 = Task16_p_form()
        form17 = Task17_p_form()
        form18 = Task18_p_form()
        form19 = Task19_p_form()
        form20 = Task20_p_form()
        devices = Device.objects.get(pk=pk)
        Task1_vc_dateform = Task1_p_date_form(instance=devices.Parts)
        Task2_vc_dateform = Task2_p_date_form(instance=devices.Parts)
        Task3_vc_dateform = Task3_p_date_form(instance=devices.Parts)
        Task4_vc_dateform = Task4_p_date_form(instance=devices.Parts)
        Task5_vc_dateform = Task5_p_date_form(instance=devices.Parts)
        Task6_vc_dateform = Task6_p_date_form(instance=devices.Parts)
        Task7_vc_dateform = Task7_p_date_form(instance=devices.Parts)
        Task8_vc_dateform = Task8_p_date_form(instance=devices.Parts)
        Task9_vc_dateform = Task9_p_date_form(instance=devices.Parts)
        Task10_vc_dateform = Task10_p_date_form(instance=devices.Parts)
        Task11_vc_dateform = Task11_p_date_form(instance=devices.Parts)
        Task12_vc_dateform = Task12_p_date_form(instance=devices.Parts)
        Task13_vc_dateform = Task13_p_date_form(instance=devices.Parts)
        Task14_vc_dateform = Task14_p_date_form(instance=devices.Parts)
        Task15_vc_dateform = Task15_p_date_form(instance=devices.Parts)
        Task16_vc_dateform = Task16_p_date_form(instance=devices.Parts)
        Task17_vc_dateform = Task17_p_date_form(instance=devices.Parts)
        Task18_vc_dateform = Task18_p_date_form(instance=devices.Parts)
        Task19_vc_dateform = Task19_p_date_form(instance=devices.Parts)
        Task20_vc_dateform = Task20_p_date_form(instance=devices.Parts)

        # Calculating % completed
        y = 0
        if devices.Parts.Task1_Name:
            y = y + 1
        if devices.Parts.Task2_Name:
            y = y + 1
        if devices.Parts.Task3_Name:
            y = y + 1
        if devices.Parts.Task4_Name:
            y = y + 1
        if devices.Parts.Task5_Name:
            y = y + 1
        if devices.Parts.Task6_Name:
            y = y + 1
        if devices.Parts.Task7_Name:
            y = y + 1
        if devices.Parts.Task8_Name:
            y = y + 1
        if devices.Parts.Task9_Name:
            y = y + 1
        if devices.Parts.Task10_Name:
            y = y + 1
        if devices.Parts.Task11_Name:
            y = y + 1
        if devices.Parts.Task12_Name:
            y = y + 1
        if devices.Parts.Task13_Name:
            y = y + 1
        if devices.Parts.Task14_Name:
            y = y + 1
        if devices.Parts.Task15_Name:
            y = y + 1
        if devices.Parts.Task16_Name:
            y = y + 1
        if devices.Parts.Task17_Name:
            y = y + 1
        if devices.Parts.Task18_Name:
            y = y + 1
        if devices.Parts.Task19_Name:
            y = y + 1
        if devices.Parts.Task20_Name:
            y = y + 1


        x = 0
        if devices.Parts.Task1_complete_date:
            x =x+1
            devices.Parts.Task1_alert = False
            devices.Parts.Task1_warning=False
            devices.Parts.Status='On_Time'
        if devices.Parts.Task2_complete_date:
            x = x + 1
            devices.Parts.Task2_alert = False
            devices.Parts.Task2_warning=False
            devices.Parts.Status = 'On_Time'
        if devices.Parts.Task3_complete_date:
            x = x + 1
            devices.Parts.Task3_alert = False
            devices.Parts.Task3_warning=False
            devices.Parts.Status = 'On_Time'
        if devices.Parts.Task4_complete_date:
            x = x + 1
            devices.Parts.Task4_alert = False
            devices.Parts.Task4_warning=False
            devices.Parts.Status = 'On_Time'
        if devices.Parts.Task5_complete_date:
            x = x + 1
            devices.Parts.Task5_alert = False
            devices.Parts.Task5_warning=False
            devices.Parts.Status = 'On_Time'
        if devices.Parts.Task6_complete_date:
            x = x + 1
            devices.Parts.Task6_alert = False
            devices.Parts.Task6_warning=False
            devices.Parts.Status = 'On_Time'
        if devices.Parts.Task7_complete_date:
            x =x+1
            devices.Parts.Task7_alert = False
            devices.Parts.Task7_warning=False
            devices.Parts.Status = 'On_Time'
        if devices.Parts.Task8_complete_date:
            x =x+1
            devices.Parts.Task8_alert = False
            devices.Parts.Task8_warning=False
            devices.Parts.Status = 'On_Time'
        if devices.Parts.Task9_complete_date:
            x =x+1
            devices.Parts.Task9_alert = False
            devices.Parts.Task9_warning=False
            devices.Parts.Status = 'On_Time'
        if devices.Parts.Task10_complete_date:
            x =x+1
            devices.Parts.Task10_alert = False
            devices.Parts.Task10_warning=False
            devices.Parts.Status = 'On_Time'
        if devices.Parts.Task11_complete_date:
            x =x+1
            devices.Parts.Task11_alert = False
            devices.Parts.Task11_warning=False
            devices.Parts.Status = 'On_Time'
        if devices.Parts.Task12_complete_date:
            x = x + 1
            devices.Parts.Task12_alert = False
            devices.Parts.Task12_warning=False
            devices.Parts.Status = 'On_Time'
        if devices.Parts.Task13_complete_date:
            x = x + 1
            devices.Parts.Task13_alert = False
            devices.Parts.Task13_warning=False
            devices.Parts.Status = 'On_Time'
        if devices.Parts.Task14_complete_date:
            x = x + 1
            devices.Parts.Task14_alert = False
            devices.Parts.Task14_warning=False
            devices.Parts.Status = 'On_Time'
        if devices.Parts.Task15_complete_date:
            x = x + 1
            devices.Parts.Task15_alert = False
            devices.Parts.Task15_warning=False
            devices.Parts.Status = 'On_Time'
        if devices.Parts.Task16_complete_date:
            x = x + 1
            devices.Parts.Task16_alert = False
            devices.Parts.Task16_warning=False
            devices.Parts.Status = 'On_Time'
        if devices.Parts.Task17_complete_date:
            x =x+1
            devices.Parts.Task17_alert = False
            devices.Parts.Task17_warning=False
            devices.Parts.Status = 'On_Time'
        if devices.Parts.Task18_complete_date:
            x =x+1
            devices.Parts.Task18_alert = False
            devices.Parts.Task18_warning=False
            devices.Parts.Status = 'On_Time'
        if devices.Parts.Task19_complete_date:
            x =x+1
            devices.Parts.Task19_alert = False
            devices.Parts.Task19_warning=False
            devices.Parts.Status = 'On_Time'
        if devices.Parts.Task20_complete_date:
            x =x+1
            devices.Parts.Task20_alert = False
            devices.Parts.Task20_warning=False
            devices.Parts.Status = 'On_Time'
        percent = x/y * 100
        print (percent)

        #alerting logic
        today = datetime.date.today()
        if devices.Parts.Task1_End_Date:
            Task1_delta =  devices.Parts.Task1_End_Date - today
        else:
            Task1_delta = None
        if devices.Parts.Task2_End_Date:
            Task2_delta = devices.Parts.Task2_End_Date - today
        else:
            Task2_delta = None
        if devices.Parts.Task3_End_Date:
            Task3_delta = devices.Parts.Task3_End_Date - today
        else:
            Task3_delta = None
        if devices.Parts.Task4_End_Date:
            Task4_delta = devices.Parts.Task4_End_Date - today
        else:
            Task4_delta = None
        if devices.Parts.Task5_End_Date:
            Task5_delta = devices.Parts.Task5_End_Date - today
        else:
            Task5_delta = None
        if devices.Parts.Task6_End_Date:
            Task6_delta = devices.Parts.Task6_End_Date - today
        else:
            Task6_delta = None
        if devices.Parts.Task7_End_Date:
            Task7_delta = devices.Parts.Task7_End_Date - today
        else:
            Task7_delta = None
        if devices.Parts.Task8_End_Date:
            Task8_delta = devices.Parts.Task8_End_Date - today
        else:
            Task8_delta = None
        if devices.Parts.Task9_End_Date:
            Task9_delta = devices.Parts.Task9_End_Date - today
        else:
            Task9_delta = None
        if devices.Parts.Task10_End_Date:
            Task10_delta =  devices.Parts.Task10_End_Date - today
        else:
            Task10_delta = None
        if devices.Parts.Task11_End_Date:
            Task11_delta =  devices.Parts.Task11_End_Date - today
        else:
            Task11_delta = None
        if devices.Parts.Task12_End_Date:
            Task12_delta = devices.Parts.Task12_End_Date - today
        else:
            Task12_delta = None
        if devices.Parts.Task13_End_Date:
            Task13_delta = devices.Parts.Task13_End_Date - today
        else:
            Task13_delta = None
        if devices.Parts.Task14_End_Date:
            Task14_delta = devices.Parts.Task14_End_Date - today
        else:
            Task14_delta = None
        if devices.Parts.Task15_End_Date:
            Task15_delta = devices.Parts.Task15_End_Date - today
        else:
            Task15_delta = None
        if devices.Parts.Task16_End_Date:
            Task16_delta = devices.Parts.Task16_End_Date - today
        else:
            Task16_delta = None
        if devices.Parts.Task17_End_Date:
            Task17_delta = devices.Parts.Task17_End_Date - today
        else:
            Task17_delta = None
        if devices.Parts.Task18_End_Date:
            Task18_delta = devices.Parts.Task18_End_Date - today
        else:
            Task18_delta = None
        if devices.Parts.Task19_End_Date:
            Task19_delta = devices.Parts.Task19_End_Date - today
        else:
            Task19_delta = None
        if devices.Parts.Task20_End_Date:
            Task20_delta = devices.Parts.Task20_End_Date - today
        else:
            Task20_delta = None

        if Task1_delta and Task1_delta < timedelta(devices.Parts.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not devices.Parts.Task1_complete_date:
            devices.Parts.Task1_warning = True
            devices.Parts.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(devices.Parts.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not devices.Parts.Task2_complete_date:
            devices.Parts.Task2_warning = True
            devices.Parts.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(devices.Parts.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not devices.Parts.Task3_complete_date:
            devices.Parts.Task3_warning = True
            devices.Parts.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(devices.Parts.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not devices.Parts.Task4_complete_date:
            devices.Parts.Task4_warning = True
            devices.Parts.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(devices.Parts.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not devices.Parts.Task5_complete_date:
            devices.Parts.Task5_warning = True
            devices.Parts.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(devices.Parts.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not devices.Parts.Task6_complete_date:
            devices.Parts.Task6_warning = True
            devices.Parts.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(devices.Parts.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not devices.Parts.Task7_complete_date:
            devices.Parts.Task7_warning = True
            devices.Parts.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(devices.Parts.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not devices.Parts.Task8_complete_date:
            devices.Parts.Task8_warning = True
            devices.Parts.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(devices.Parts.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not devices.Parts.Task9_complete_date:
            devices.Parts.Task9_warning = True
            devices.Parts.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(devices.Parts.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not devices.Parts.Task10_complete_date:
            devices.Parts.Task10_warning = True
            devices.Parts.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(devices.Parts.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not devices.Parts.Task11_complete_date:
            devices.Parts.Task11_warning = True
            devices.Parts.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(devices.Parts.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not devices.Parts.Task12_complete_date:
            devices.Parts.Task12_warning = True
            devices.Parts.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(devices.Parts.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not devices.Parts.Task13_complete_date:
            devices.Parts.Task13_warning = True
            devices.Parts.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(devices.Parts.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not devices.Parts.Task14_complete_date:
            devices.Parts.Task14_warning = True
            devices.Parts.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(devices.Parts.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not devices.Parts.Task15_complete_date:
            devices.Parts.Task15_warning = True
            devices.Parts.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(devices.Parts.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not devices.Parts.Task16_complete_date:
            devices.Parts.Task16_warning = True
            devices.Parts.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(devices.Parts.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not devices.Parts.Task17_complete_date:
            devices.Parts.Task17_warning = True
            devices.Parts.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(devices.Parts.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not devices.Parts.Task18_complete_date:
            devices.Parts.Task18_warning = True
            devices.Parts.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(devices.Parts.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not devices.Parts.Task19_complete_date:
            devices.Parts.Task19_warning = True
            devices.Parts.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(devices.Parts.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not devices.Parts.Task20_complete_date:
            devices.Parts.Task20_warning = True
            devices.Parts.Status = 'At Risk'

        if devices.Parts.Task1_End_Date and Task1_delta < timedelta(0) and not devices.Parts.Task1_complete_date:
            devices.Parts.Task1_alert = True
            devices.Parts.Status = 'Delayed'
        if devices.Parts.Task2_End_Date and Task2_delta < timedelta(0) and not devices.Parts.Task2_complete_date:
            devices.Parts.Task2_alert = True
            devices.Parts.Status = 'Delayed'
        if devices.Parts.Task3_End_Date and Task3_delta < timedelta(0) and not devices.Parts.Task3_complete_date:
            devices.Parts.Task3_alert = True
            devices.Parts.Status = 'Delayed'
        if devices.Parts.Task4_End_Date and Task4_delta < timedelta(0) and not devices.Parts.Task4_complete_date:
            devices.Parts.Task4_alert = True
            devices.Parts.Status = 'Delayed'
        if devices.Parts.Task5_End_Date and Task5_delta < timedelta(0) and not devices.Parts.Task5_complete_date:
            devices.Parts.Task5_alert = True
            devices.Parts.Status = 'Delayed'
        if devices.Parts.Task6_End_Date and Task6_delta < timedelta(0) and not devices.Parts.Task6_complete_date:
            devices.Parts.Task6_alert = True
            devices.Parts.Status = 'Delayed'
        if devices.Parts.Task7_End_Date and Task7_delta < timedelta(0) and not devices.Parts.Task7_complete_date:
            devices.Parts.Task7_alert = True
            devices.Parts.Status = 'Delayed'
        if devices.Parts.Task8_End_Date and Task8_delta < timedelta(0)and not devices.Parts.Task8_complete_date:
            devices.Parts.Task8_alert = True
            devices.Parts.Status = 'Delayed'
        if devices.Parts.Task9_End_Date and Task9_delta < timedelta(0)and not devices.Parts.Task9_complete_date:
            devices.Parts.Task9_alert = True
            devices.Parts.Status = 'Delayed'
        if devices.Parts.Task10_End_Date and Task10_delta < timedelta(0) and not devices.Parts.Task10_complete_date:
            devices.Parts.Task10_alert = True
            devices.Parts.Status = 'Delayed'
        if devices.Parts.Task11_End_Date and Task11_delta < timedelta(0) and not devices.Parts.Task11_complete_date:
            devices.Parts.Task11_alert = True
            devices.Parts.Status = 'Delayed'
        if devices.Parts.Task12_End_Date and Task12_delta < timedelta(0) and not devices.Parts.Task12_complete_date:
            devices.Parts.Task12_alert = True
            devices.Parts.Status = 'Delayed'
        if devices.Parts.Task13_End_Date and Task13_delta < timedelta(0) and not devices.Parts.Task13_complete_date:
            devices.Parts.Task13_alert = True
            devices.Parts.Status = 'Delayed'
        if devices.Parts.Task14_End_Date and Task14_delta < timedelta(0) and not devices.Parts.Task14_complete_date:
            devices.Parts.Task14_alert = True
            devices.Parts.Status = 'Delayed'
        if devices.Parts.Task15_End_Date and Task15_delta < timedelta(0) and not devices.Parts.Task15_complete_date:
            devices.Parts.Task15_alert = True
            devices.Parts.Status = 'Delayed'
        if devices.Parts.Task16_End_Date and Task16_delta < timedelta(0) and not devices.Parts.Task16_complete_date:
            devices.Parts.Task16_alert = True
            devices.Parts.Status = 'Delayed'
        if devices.Parts.Task17_End_Date and Task17_delta < timedelta(0)and not devices.Parts.Task17_complete_date:
            devices.Parts.Task17_alert = True
            devices.Parts.Status = 'Delayed'
        if devices.Parts.Task18_End_Date and Task18_delta < timedelta(0)and not devices.Parts.Task18_complete_date:
            devices.Parts.Task18_alert = True
            devices.Parts.Status = 'Delayed'
        if devices.Parts.Task19_End_Date and Task19_delta < timedelta(0)and not devices.Parts.Task19_complete_date:
            devices.Parts.Task19_alert = True
            devices.Parts.Status = 'Delayed'
        if devices.Parts.Task20_End_Date and Task20_delta < timedelta(0)and not devices.Parts.Task20_complete_date:
            devices.Parts.Task20_alert = True
            devices.Parts.Status = 'Delayed'

        devices.Parts.completed = int(percent)
        devices.Parts.save()
        posts1 = devices.Parts.task1statusparts_set.all().order_by('-created')
        posts2 = devices.Parts.task2statusparts_set.all().order_by('-created')
        posts3 = devices.Parts.task3statusparts_set.all().order_by('-created')
        posts4 = devices.Parts.task4statusparts_set.all().order_by('-created')
        posts5 = devices.Parts.task5statusparts_set.all().order_by('-created')
        posts6 = devices.Parts.task6statusparts_set.all().order_by('-created')
        posts7 = devices.Parts.task7statusparts_set.all().order_by('-created')
        posts8 = devices.Parts.task8statusparts_set.all().order_by('-created')
        posts9 = devices.Parts.task9statusparts_set.all().order_by('-created')
        posts10 = devices.Parts.task10statusparts_set.all().order_by('-created')
        posts11 = devices.Parts.task11statusparts_set.all().order_by('-created')
        posts12 = devices.Parts.task12statusparts_set.all().order_by('-created')
        posts13 = devices.Parts.task13statusparts_set.all().order_by('-created')
        posts14 = devices.Parts.task14statusparts_set.all().order_by('-created')
        posts15 = devices.Parts.task15statusparts_set.all().order_by('-created')
        posts16 = devices.Parts.task16statusparts_set.all().order_by('-created')
        posts17 = devices.Parts.task17statusparts_set.all().order_by('-created')
        posts18 = devices.Parts.task18statusparts_set.all().order_by('-created')
        posts19 = devices.Parts.task19statusparts_set.all().order_by('-created')
        posts20 = devices.Parts.task20statusparts_set.all().order_by('-created')

        args = {'devices': devices, 'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5,
                'form6': form6,
                'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12,
                'form13': form13,
                'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17, 'form18': form18,
                'form19': form19,
                'form20': form20, 'posts1': posts1, 'posts2': posts2, 'posts3': posts3, 'posts4': posts4,
                'posts5': posts5, 'posts6': posts6,
                'posts7': posts7, 'posts8': posts8, 'posts9': posts9, 'posts10': posts10, 'posts11': posts11,
                'posts12': posts12, 'posts13': posts13,
                'posts14': posts14, 'posts15': posts15, 'posts16': posts16, 'posts17': posts17, 'posts18': posts18,
                'posts19': posts19,
                'posts20': posts20, 'Task1_vc_dateform': Task1_vc_dateform, 'Task2_vc_dateform': Task2_vc_dateform,
                'Task3_vc_dateform': Task3_vc_dateform, 'Task4_vc_dateform': Task4_vc_dateform,
                'Task5_vc_dateform': Task5_vc_dateform, 'Task6_vc_dateform': Task6_vc_dateform,
                'Task7_vc_dateform': Task7_vc_dateform, 'Task8_vc_dateform': Task8_vc_dateform,
                'Task9_vc_dateform': Task9_vc_dateform, 'Task10_vc_dateform': Task10_vc_dateform,
                'Task11_vc_dateform': Task11_vc_dateform, 'Task12_vc_dateform': Task12_vc_dateform,
                'Task13_vc_dateform': Task13_vc_dateform, 'Task14_vc_dateform': Task14_vc_dateform,
                'Task15_vc_dateform': Task15_vc_dateform, 'Task16_vc_dateform': Task16_vc_dateform,
                'Task17_vc_dateform': Task17_vc_dateform, 'Task18_vc_dateform': Task18_vc_dateform,
                'Task19_vc_dateform': Task19_vc_dateform, 'Task20_vc_dateform': Task20_vc_dateform,
                'Task1_delta': Task1_delta, 'Task7_delta': Task7_delta, 'Task12_delta': Task12_delta,
                'Task17_delta': Task17_delta,
                'Task2_delta': Task2_delta, 'Task8_delta': Task8_delta, 'Task13_delta': Task13_delta,
                'Task3_delta': Task3_delta, 'Task9_delta': Task9_delta, 'Task14_delta': Task14_delta,
                'Task18_delta': Task18_delta,
                'Task4_delta': Task4_delta, 'Task10_delta': Task10_delta, 'Task15_delta': Task15_delta,
                'Task19_delta': Task19_delta,
                'Task5_delta': Task5_delta, 'Task11_delta': Task11_delta, 'Task16_delta': Task16_delta,
                'Task20_delta': Task20_delta,
                'Task6_delta': Task6_delta,
                }
        return render(request, self.template_name, args)

    def post(self, request, pk):

        form1 = Task1_p_form(request.POST)
        form2 = Task2_p_form(request.POST)
        form3 = Task3_p_form(request.POST)
        form4 = Task4_p_form(request.POST)
        form5 = Task5_p_form(request.POST)
        form6 = Task6_p_form(request.POST)
        form7 = Task7_p_form(request.POST)
        form8 = Task8_p_form(request.POST)
        form9 = Task9_p_form(request.POST)
        form10 = Task10_p_form(request.POST)
        form11 = Task11_p_form(request.POST)
        form12 = Task12_p_form(request.POST)
        form13 = Task13_p_form(request.POST)
        form14 = Task14_p_form(request.POST)
        form15 = Task15_p_form(request.POST)
        form16 = Task16_p_form(request.POST)
        form17 = Task17_p_form(request.POST)
        form18 = Task18_p_form(request.POST)
        form19 = Task19_p_form(request.POST)
        form20 = Task20_p_form(request.POST)
        devices = Device.objects.get(pk=pk)

        Task1_vc_dateform = Task1_p_date_form(request.POST, instance=devices.Parts)
        Task2_vc_dateform = Task2_p_date_form(request.POST, instance=devices.Parts)
        Task3_vc_dateform = Task3_p_date_form(request.POST, instance=devices.Parts)
        Task4_vc_dateform = Task4_p_date_form(request.POST, instance=devices.Parts)
        Task5_vc_dateform = Task5_p_date_form(request.POST, instance=devices.Parts)
        Task6_vc_dateform = Task6_p_date_form(request.POST, instance=devices.Parts)
        Task7_vc_dateform = Task7_p_date_form(request.POST, instance=devices.Parts)
        Task8_vc_dateform = Task8_p_date_form(request.POST, instance=devices.Parts)
        Task9_vc_dateform = Task9_p_date_form(request.POST, instance=devices.Parts)
        Task10_vc_dateform = Task10_p_date_form(request.POST, instance=devices.Parts)
        Task11_vc_dateform = Task11_p_date_form(request.POST, instance=devices.Parts)
        Task12_vc_dateform = Task12_p_date_form(request.POST, instance=devices.Parts)
        Task13_vc_dateform = Task13_p_date_form(request.POST, instance=devices.Parts)
        Task14_vc_dateform = Task14_p_date_form(request.POST, instance=devices.Parts)
        Task15_vc_dateform = Task15_p_date_form(request.POST, instance=devices.Parts)
        Task16_vc_dateform = Task16_p_date_form(request.POST, instance=devices.Parts)
        Task17_vc_dateform = Task17_p_date_form(request.POST, instance=devices.Parts)
        Task18_vc_dateform = Task18_p_date_form(request.POST, instance=devices.Parts)
        Task19_vc_dateform = Task19_p_date_form(request.POST, instance=devices.Parts)
        Task20_vc_dateform = Task20_p_date_form(request.POST, instance=devices.Parts)

        if 'Task1Submit' in request.POST:
            if form1.is_valid() and Task1_vc_dateform.is_valid():
                post = form1.save(commit=False)
                post.user = request.user
                post.Parts = devices.Parts
                Task1_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/parts')
            else:
                return redirect('/login/summary/' + pk + '/parts')
        elif 'Task2Submit' in request.POST:
            if form2.is_valid() and Task2_vc_dateform.is_valid():
                post = form2.save(commit=False)
                post.user = request.user
                post.Parts = devices.Parts
                Task2_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/parts')
            else:
                return redirect('/login/summary/' + pk + '/parts')
        elif 'Task3Submit' in request.POST:
            if form3.is_valid() and Task3_vc_dateform.is_valid():
                post = form3.save(commit=False)
                post.user = request.user
                post.Parts = devices.Parts
                Task3_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/parts')
            else:
                return redirect('/login/summary/' + pk + '/parts')
        elif 'Task4Submit' in request.POST:
            if form4.is_valid() and Task4_vc_dateform.is_valid():
                post = form4.save(commit=False)
                post.user = request.user
                post.Parts = devices.Parts
                Task4_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/parts')
            else:
                return redirect('/login/summary/' + pk + '/parts')
        elif 'Task5Submit' in request.POST:
            if form5.is_valid() and Task5_vc_dateform.is_valid():
                post = form5.save(commit=False)
                post.user = request.user
                post.Parts = devices.Parts
                Task5_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/parts')
            else:
                return redirect('/login/summary/' + pk + '/parts')
        elif 'Task6Submit' in request.POST:
            if form6.is_valid() and Task6_vc_dateform.is_valid():
                post = form6.save(commit=False)
                post.user = request.user
                post.Parts = devices.Parts
                Task6_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/parts')
            else:
                return redirect('/login/summary/' + pk + '/parts')
        elif 'Task7Submit' in request.POST:
            if form7.is_valid() and Task7_vc_dateform.is_valid():
                post = form7.save(commit=False)
                post.user = request.user
                post.Parts = devices.Parts
                Task7_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/parts')
            else:
                return redirect('/login/summary/' + pk + '/parts')
        elif 'Task8Submit' in request.POST:
            if form8.is_valid() and Task8_vc_dateform.is_valid():
                post = form8.save(commit=False)
                post.user = request.user
                post.Parts = devices.Parts
                Task8_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/parts')
            else:
                return redirect('/login/summary/' + pk + '/parts')
        elif 'Task9Submit' in request.POST:
            if form9.is_valid() and Task9_vc_dateform.is_valid():
                post = form9.save(commit=False)
                post.user = request.user
                post.Parts = devices.Parts
                Task9_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/parts')
            else:
                return redirect('/login/summary/' + pk + '/parts')
        elif 'Task10Submit' in request.POST:
            if form10.is_valid() and Task10_vc_dateform.is_valid():
                post = form10.save(commit=False)
                post.user = request.user
                post.Parts = devices.Parts
                Task10_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/parts')
            else:
                return redirect('/login/summary/' + pk + '/parts')
        elif 'Task11Submit' in request.POST:
            if form11.is_valid() and Task11_vc_dateform.is_valid():
                post = form11.save(commit=False)
                post.user = request.user
                post.Parts = devices.Parts
                Task11_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/parts')
            else:
                return redirect('/login/summary/' + pk + '/parts')
        elif 'Task12Submit' in request.POST:
            if form12.is_valid() and Task12_vc_dateform.is_valid():
                post = form12.save(commit=False)
                post.user = request.user
                post.Parts = devices.Parts
                Task12_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/parts')
            else:
                return redirect('/login/summary/' + pk + '/parts')
        elif 'Task13Submit' in request.POST:
            if form13.is_valid() and Task13_vc_dateform.is_valid():
                post = form13.save(commit=False)
                post.user = request.user
                post.Parts = devices.Parts
                Task13_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/parts')
            else:
                return redirect('/login/summary/' + pk + '/parts')
        elif 'Task14Submit' in request.POST:
            if form14.is_valid() and Task14_vc_dateform.is_valid():
                post = form14.save(commit=False)
                post.user = request.user
                post.Parts = devices.Parts
                Task14_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/parts')
            else:
                return redirect('/login/summary/' + pk + '/parts')
        elif 'Task15Submit' in request.POST:
            if form15.is_valid() and Task15_vc_dateform.is_valid():
                post = form15.save(commit=False)
                post.user = request.user
                post.Parts = devices.Parts
                Task15_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/parts')
            else:
                return redirect('/login/summary/' + pk + '/parts')
        elif 'Task16Submit' in request.POST:
            if form16.is_valid() and Task16_vc_dateform.is_valid():
                post = form16.save(commit=False)
                post.user = request.user
                post.Parts = devices.Parts
                Task16_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/parts')
            else:
                return redirect('/login/summary/' + pk + '/parts')
        elif 'Task17Submit' in request.POST:
            if form17.is_valid() and Task17_vc_dateform.is_valid():
                post = form17.save(commit=False)
                post.user = request.user
                post.Parts = devices.Parts
                Task17_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/parts')
            else:
                return redirect('/login/summary/' + pk + '/parts')
        elif 'Task18Submit' in request.POST:
            if form18.is_valid() and Task18_vc_dateform.is_valid():
                post = form18.save(commit=False)
                post.user = request.user
                post.Parts = devices.Parts
                Task18_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/parts')
            else:
                return redirect('/login/summary/' + pk + '/parts')
        elif 'Task19Submit' in request.POST:
            if form19.is_valid() and Task19_vc_dateform.is_valid():
                post = form19.save(commit=False)
                post.user = request.user
                post.Parts = devices.Parts
                Task19_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/parts')
            else:
                return redirect('/login/summary/' + pk + '/parts')
        elif 'Task20Submit' in request.POST:
            if form20.is_valid() and Task20_vc_dateform.is_valid():
                post = form20.save(commit=False)
                post.user = request.user
                post.Parts = devices.Parts
                Task20_vc_dateform.save()
                post.save()
                return redirect('/login/summary/' + pk + '/parts')
            else:
                return redirect('/login/summary/' + pk + '/parts')