from django.conf.urls import url, include
from . import views
from mobile.views import (
ProductView, IntermediateView, DetailView, AddDeviceView, ExcelView, DetailExcelView
)

urlpatterns = [
    url(r'^$', ProductView.as_view(), name='specialproduct'),
    url(r'^(?P<pk>\d+)/$', IntermediateView.as_view(), name='specialintermediate'),
    url(r'^teams/(?P<id>\d+)/$', DetailView.as_view(), name='specialdetail'),
    url(r'^defaulttemplate/$', AddDeviceView.as_view(), name='SpecialAddDevice'),
    url(r'^excel/$', ExcelView.as_view(), name='SpecialExcel'),
    url(r'^(?P<pk>\d+)/detailexcel/$', DetailExcelView.as_view(), name='specialDetailExcel'),
]
