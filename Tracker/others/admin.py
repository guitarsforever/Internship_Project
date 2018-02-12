# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from others.models import (
Product, Team, Task, TaskStat,category
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


class ProductAdmin(admin.ModelAdmin):
    inlines = [TeamAdmi]


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskStat)
admin.site.register(category)