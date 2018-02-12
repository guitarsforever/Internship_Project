from django.conf.urls import url, include
from . import views
from general.views import (
ProductView, IntermediateView, DetailView, AddDeviceView, ExcelView, DetailExcelView,HomepageView,DeviceSummaryView
)

urlpatterns = [
    url(r'^$', ProductView.as_view(), name='generalproduct'),
    url(r'^(?P<pk>\d+)/$', IntermediateView.as_view(), name='generalintermediate'),
    url(r'^teams/(?P<id>\d+)/$', DetailView.as_view(), name='generaldetail'),
    url(r'^defaulttemplate/$', AddDeviceView.as_view(), name='generalAddDevice'),
    url(r'^excel/$', ExcelView.as_view(), name='generalExcel'),
    url(r'^(?P<pk>\d+)/detailexcel/$', DetailExcelView.as_view(), name='generalDetailExcel'),
    url(r'^homepage/$', HomepageView.as_view(), name='generalHomepage'),
    url(r'^homepage/(?P<pk>\d+)/$', DeviceSummaryView.as_view(), name='generalDeviceSummary'),
]
