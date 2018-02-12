from django.contrib import admin
from login.models import (
    UserProfile, Device, ProductReadiness,
     videocontent, Task1StatusVideoContent, Task2StatusVideoContent,
    Task3StatusVideoContent, Task4StatusVideoContent, Task5StatusVideoContent ,Task6StatusVideoContent ,
    Task7StatusVideoContent, Task8StatusVideoContent, Task9StatusVideoContent ,Task10StatusVideoContent ,
    Task11StatusVideoContent, Task12StatusVideoContent, Task13StatusVideoContent ,Task14StatusVideoContent ,
    Task15StatusVideoContent, Task16StatusVideoContent, Task17StatusVideoContent ,Task18StatusVideoContent ,
    Task19StatusVideoContent, Task20StatusVideoContent, ExtraTasks_VideoContent, ExtraTaskStatusVideoContent,
    digitalcontent, callcentertraining, callcenteropertaions, productsupport, warehouse, fieldservice, techsupport,
    servicemarketing, servicetraining, parts, Task1StatusCallCenterTraining, Task1StatusProductReadiness, Announcements,
    test, reference, DeviceHistory, DashboardControlDevice, ProductReadinessHistory, VideoContentHistory, DigitalContentHistory,
    CallCenterTrainingHistory, CallCenterOperationsHistory, ProductSupportHistory, WarehouseHistory, FieldServiceHistory,
    TechSupportHistory, ServiceMarketingHistory, ServiceTrainingHistory, PartsHistory

)

admin.site.site_header = 'Samsung Pre-Launch Tool Administration'


class DeviceHistoryAdmin(admin.ModelAdmin):
    list_display = ['get_product','Completed','Created' ]
    search_fields = ['device__Name', 'Created']

    def get_product(self,obj):
        return obj.device.Name
    get_product.admin_order_field = "Product"
    get_product.short_description = 'Related Product Name'

class DashboardControlDeviceAdmin(admin.ModelAdmin):
    list_display = ['get_product']
    search_fields = ['Device__Name']

    def get_product(self,obj):
        return obj.Device.Name
    get_product.admin_order_field = "Product"
    get_product.short_description = 'Related Product Name'


# Register your models here.
# admin.site.register(DashboardControlDevice, DashboardControlDeviceAdmin)
# admin.site.register(DeviceHistory, DeviceHistoryAdmin)
# admin.site.register(UserProfile)
# admin.site.register(Device)
# admin.site.register(ProductReadiness)
# admin.site.register(Announcements)
# admin.site.register(reference)
# admin.site.register(videocontent)
# admin.site.register(ExtraTasks_VideoContent)
# admin.site.register(ExtraTaskStatusVideoContent)
#
# admin.site.register(digitalcontent)
#
# admin.site.register(callcentertraining)
#
# admin.site.register(callcenteropertaions)
#
# admin.site.register(productsupport)
#
# admin.site.register(warehouse)
#
# admin.site.register(fieldservice)
#
# admin.site.register(techsupport)
#
# admin.site.register(servicemarketing)
#
# admin.site.register(servicetraining)
#
# admin.site.register(parts)
#
# admin.site.register(ProductReadinessHistory)
#
# admin.site.register(VideoContentHistory)
#
# admin.site.register(DigitalContentHistory)
#
# admin.site.register(CallCenterTrainingHistory)
#
# admin.site.register(CallCenterOperationsHistory)
#
# admin.site.register(WarehouseHistory)
#
# admin.site.register(FieldServiceHistory)
#
# admin.site.register(TechSupportHistory)
#
# admin.site.register(ServiceMarketingHistory)
#
# admin.site.register(ServiceTrainingHistory)
#
# admin.site.register(PartsHistory)