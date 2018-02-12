from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)
from django.views.generic import ListView, DetailView
from login.models import Device
from login.views import (
    ProductReadinessView, IntermediateView, VideoContentView,DigitalContentView, CallCenterTrainingView,CallCenterOperationsView,
ProductSupportView, WarehouseView, FieldServiceView, TechSupportView, ServiceTrainingView, ServiceMarketingView,PartsView,
ProductView, DefaultSettingView, ExcelView,ExcelDetailView, HomepageView,DeviceSummaryView,HomepageHAView,HomepageHEView,
DeviceSummaryHAView,DeviceSummaryHEView, DeviceSummaryPRView,DeviceSummaryVCView, DeviceSummaryDCView,
DeviceSummaryCCTView,DeviceSummaryCCOView, DeviceSummaryWView, DeviceSummaryFSView, DeviceSummaryTSView, DeviceSummarySMView,
DeviceSummarySTView, DeviceSummaryPView
)

from django.contrib.auth.decorators import login_required

def required(wrapping_functions,patterns_rslt):
    '''
    Used to require 1..n decorators in any view returned by a url tree

    Usage:
      urlpatterns = required(func,patterns(...))
      urlpatterns = required((func,func,func),patterns(...))

    Note:
      Use functools.partial to pass keyword params to the required
      decorators. If you need to pass args you will have to write a
      wrapper function.

    Example:
      from functools import partial

      urlpatterns = required(
          partial(login_required,login_url='/accounts/login/'),
          patterns(...)
      )
    '''
    if not hasattr(wrapping_functions,'__iter__'):
        wrapping_functions = (wrapping_functions,)

    return [
        _wrap_instance__resolve(wrapping_functions,instance)
        for instance in patterns_rslt
    ]
def _wrap_instance__resolve(wrapping_functions,instance):
    if not hasattr(instance,'resolve'): return instance
    resolve = getattr(instance,'resolve')

    def _wrap_func_in_returned_resolver_match(*args,**kwargs):
        rslt = resolve(*args,**kwargs)

        if not hasattr(rslt,'func'):return rslt
        f = getattr(rslt,'func')

        for _f in reversed(wrapping_functions):
            # @decorate the function from inner to outter
            f = _f(f)

        setattr(rslt,'func',f)

        return rslt

    setattr(instance,'resolve',_wrap_func_in_returned_resolver_match)

    return instance

urlpatterns = [
    url(r'^$', views.home),
    url(r'^auth/$', login, {'template_name': 'login/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'login/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', password_reset, name='reset_password'),
    url(r'^excel/$', ExcelView.as_view(), name='excel'),
    url(r'^excel/(?P<pk>\d+)/$', ExcelDetailView.as_view(), name='excel'),
    url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^defaultsetting/$', DefaultSettingView.as_view(), name='defaultsetting'),
    url(r'^homepage/$', HomepageView.as_view(), name='Homepage'),
    url(r'^homepage/HA/$', HomepageHAView.as_view(), name='HomepageHA'),
    url(r'^homepage/HE/$', HomepageHEView.as_view(), name='HomepageHE'),
    url(r'^homepage/(?P<pk>\d+)/$', DeviceSummaryView.as_view(), name='DeviceSummary'),
    url(r'^homepage/HA/(?P<pk>\d+)/$', DeviceSummaryHAView.as_view(), name='DeviceSummaryHA'),
    url(r'^homepage/HE/(?P<pk>\d+)/$', DeviceSummaryHEView.as_view(), name='DeviceSummaryHE'),
    url(r'^reset-password/complete/$', password_reset_complete, name='password_reset_complete'),
    # url(r'^summary/$', ListView.as_view(queryset=Device.objects.all().order_by("LaunchDate"),
    #                                     template_name = "login/summary.html")),
    url(r'^summary/$', ProductView.as_view(), name='product'),
    url(r'^summary/(?P<pk>\d+)/$', IntermediateView.as_view(), name='Intermediate'),
    url(r'^summary/(?P<pk>\d+)/productreadiness/$', ProductReadinessView.as_view(), name='ProductReadiness'),
    url(r'^summary/(?P<pk>\d+)/videocontent/$', VideoContentView.as_view(), name='videocontent'),
    url(r'^summary/(?P<pk>\d+)/digitalcontent/$', DigitalContentView.as_view(), name='digitalcontent'),
    url(r'^summary/(?P<pk>\d+)/callcentertraining/$', CallCenterTrainingView.as_view(), name='callcentertraining'),
    url(r'^summary/(?P<pk>\d+)/callcenteroperations/$', CallCenterOperationsView.as_view(), name='callcenteroperations'),
    url(r'^summary/(?P<pk>\d+)/productsupport/$', ProductSupportView.as_view(), name='productsupport'),
    url(r'^summary/(?P<pk>\d+)/warehouse/$', WarehouseView.as_view(), name='warehouse'),
    url(r'^summary/(?P<pk>\d+)/fieldservice/$', FieldServiceView.as_view(), name='fieldservice'),
    url(r'^summary/(?P<pk>\d+)/techsupport/$', TechSupportView.as_view(), name='techsupport'),
    url(r'^summary/(?P<pk>\d+)/servicemarketing/$', ServiceMarketingView.as_view(), name='servicemarketing'),
    url(r'^summary/(?P<pk>\d+)/servicetraining/$', ServiceTrainingView.as_view(),
        name='servicetraining'),
    url(r'^summary/(?P<pk>\d+)/parts/$', PartsView.as_view(), name='parts'),
    url(r'^homepage/(?P<pk>\d+)/productreadiness/$', DeviceSummaryPRView.as_view(), name='DeviceSummaryPR'),
    url(r'^homepage/(?P<pk>\d+)/videocontent/$', DeviceSummaryVCView.as_view(), name='DeviceSummaryVC'),
    url(r'^homepage/(?P<pk>\d+)/digitalcontent/$', DeviceSummaryDCView.as_view(), name='DeviceSummaryDC'),
    url(r'^homepage/(?P<pk>\d+)/callcentertraining/$', DeviceSummaryCCTView.as_view(), name='DeviceSummaryCCT'),
    url(r'^homepage/(?P<pk>\d+)/callcenteroperations/$', DeviceSummaryCCOView.as_view(), name='DeviceSummaryCCO'),
    url(r'^homepage/(?P<pk>\d+)/warehouse/$', DeviceSummaryWView.as_view(), name='DeviceSummaryW'),
    url(r'^homepage/(?P<pk>\d+)/fieldservice/$', DeviceSummaryFSView.as_view(), name='DeviceSummaryFS'),
    url(r'^homepage/(?P<pk>\d+)/techsupport/$', DeviceSummaryTSView.as_view(), name='DeviceSummaryTS'),
    url(r'^homepage/(?P<pk>\d+)/servicemarketing/$', DeviceSummarySMView.as_view(), name='DeviceSummarySM'),
    url(r'^homepage/(?P<pk>\d+)/servicetraining/$', DeviceSummarySTView.as_view(), name='DeviceSummaryST'),
    url(r'^homepage/(?P<pk>\d+)/parts/$', DeviceSummaryPView.as_view(), name='DeviceSummaryP'),

]
