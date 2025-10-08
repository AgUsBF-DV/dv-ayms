from django.contrib import admin
from .models import Role, Employee, Customer


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'visible', 'createdAt', 'updatedAt')
    search_fields = ('name',)
    list_filter = ('visible', 'createdAt')
    ordering = ('name',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'firstName', 'lastName', 'role', 'isActive', 'visible')
    search_fields = ('username', 'email', 'firstName', 'lastName')
    list_filter = ('role', 'isActive', 'visible', 'date_joined')
    ordering = ('lastName', 'firstName')
    filter_horizontal = ('groups', 'user_permissions')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'email', 'visible', 'createdAt')
    search_fields = ('firstName', 'lastName', 'email')
    list_filter = ('visible', 'createdAt')
    ordering = ('lastName', 'firstName')
