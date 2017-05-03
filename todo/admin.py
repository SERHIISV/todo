# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from todo.models import Casino, Todo


@admin.register(Casino)
class CasinoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'created_at', 'modified_at')


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc', 'created_at', 'date')
