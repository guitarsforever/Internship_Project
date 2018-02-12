from django.conf.urls import url, include
from . import views
from others.views import (
ProductView, IntermediateView, DetailView, ExcelView, DetailExcelView
)

urlpatterns = [
    url(r'^$', ProductView.as_view(), name='othersproduct'),
    url(r'^(?P<pk>\d+)/$', IntermediateView.as_view(), name='othersintermediate'),
    url(r'^teams/(?P<id>\d+)/$', DetailView.as_view(), name='othersdetail'),
    url(r'^excel/$', ExcelView.as_view(), name='othersExcel'),
    url(r'^(?P<pk>\d+)/detailexcel/$', DetailExcelView.as_view(), name='othersDetailExcel'),
]