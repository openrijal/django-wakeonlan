# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Client

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ClientInline(admin.TabularInline):
    model = Client
    can_delete = False
    verbose_name_plural = 'Clients'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ClientInline, )
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'classes': ('collapse',),
            'fields': ('first_name', 'last_name', 'email'),
        }),
        ('Permissions', {
            'classes': ('collapse',),
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {
            'classes': ('collapse',),
            'fields': ('last_login', 'date_joined'),
        }),
    )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
