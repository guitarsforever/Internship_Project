# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mobile.models import (
SpecialProduct, Team, Task, TaskStatus,DefaultDevice, DefaultTeam,DefaultTask,Announcements
)

class TeamAdmi(admin.StackedInline):
    model = Team
    extra = 0

class TaskAdmi(admin.StackedInline):
    model = Task
    extra = 0

class TaskAdmin(admin.ModelAdmin):
    list_display = ['TaskName','get_team','get_product']
    search_fields = ['TaskName', 'team__TeamName', 'team__Product__Name']

    def get_product(self,obj):
        return obj.team.Product.Name
    get_product.admin_order_field = "Product"
    get_product.short_description = 'Related Product Name'

    def get_team(self,obj):
        return obj.team.TeamName
    get_team.admin_order_field = "team"
    get_team.short_description = 'Related Team Name'

class TeamAdmin(admin.ModelAdmin):
    inlines = [TaskAdmi]
    list_display = ['TeamName','get_product']
    search_fields = ['TeamName', 'Product__Name']

    def get_product(self,obj):
        return obj.Product.Name
    get_product.admin_order_field = "Product"
    get_product.short_description = 'Related Product Name'


class SpecialProductAdmin(admin.ModelAdmin):
    inlines = [TeamAdmi]


class DefaultTeamAdmi(admin.StackedInline):
    model = DefaultTeam
    extra = 0

class DefaultTaskAdmi(admin.StackedInline):
    model = DefaultTask
    extra = 0

class DefaultDeviceAdmin(admin.ModelAdmin):
    inlines = [DefaultTeamAdmi]

class DefaultTeamAdmin(admin.ModelAdmin):
    inlines = [DefaultTaskAdmi]
    list_display = ['Name','get_product']
    search_fields = ['Name', 'Device__Name']

    def get_product(self,obj):
        return obj.Device.Name
    get_product.admin_order_field = "Device"
    get_product.short_description = 'Related Product Name'

class DefaultTaskAdmin(admin.ModelAdmin):
    list_display = ['Name','get_team','get_product']
    search_fields = ['Name', 'Team__Name', 'Team__Device__Name']

    def get_product(self,obj):
        return obj.Team.Device.Name
    get_product.admin_order_field = "Device"
    get_product.short_description = 'Related Product Name'

    def get_team(self,obj):
        return obj.Team.Name
    get_team.admin_order_field = "Team"
    get_team.short_description = 'Related Team Name'

# Register your models here.
admin.site.register(SpecialProduct, SpecialProductAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Announcements)
admin.site.register(TaskStatus)
admin.site.register(DefaultDevice,DefaultDeviceAdmin)
admin.site.register(DefaultTeam,DefaultTeamAdmin)
admin.site.register(DefaultTask, DefaultTaskAdmin)
