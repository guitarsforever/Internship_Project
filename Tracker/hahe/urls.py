from django.conf.urls import url, include
from . import views
from hahe.views import (
ProductView, IntermediateView, DetailView, AddDeviceView, ExcelView, DetailExcelView, HomepageView, DeviceSummaryView,
HomepageHAView, HomepageHEView, DeviceSummaryHAView, DeviceSummaryHEView
)

urlpatterns = [
    url(r'^$', ProductView.as_view(), name='haheproduct'),
    url(r'^homepage/$', HomepageView.as_view(), name='haheHomepage'),
    url(r'^homepage/HA/$', HomepageHAView.as_view(), name='haheHomepageHA'),
    url(r'^homepage/HE/$', HomepageHEView.as_view(), name='haheHomepageHE'),
    url(r'^homepage/(?P<pk>\d+)/$', DeviceSummaryView.as_view(), name='DeviceSummary'),
    url(r'^homepage/HA/(?P<pk>\d+)/$', DeviceSummaryHAView.as_view(), name='DeviceSummaryHA'),
    url(r'^homepage/HE/(?P<pk>\d+)/$', DeviceSummaryHEView.as_view(), name='DeviceSummaryHE'),
    url(r'^(?P<pk>\d+)/$', IntermediateView.as_view(), name='haheintermediate'),
    url(r'^teams/(?P<id>\d+)/$', DetailView.as_view(), name='hahedetail'),
    url(r'^defaulttemplate/$', AddDeviceView.as_view(), name='haheAddDevice'),
    url(r'^excel/$', ExcelView.as_view(), name='haheExcel'),
    url(r'^(?P<pk>\d+)/detailexcel/$', DetailExcelView.as_view(), name='haheDetailExcel'),
]
