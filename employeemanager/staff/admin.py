from django.contrib import admin
from staff.models import Department, Employee

class DepartmentAdmin(admin.ModelAdmin):
    # fields to be displayed on search box
    search_fields = ('name',)

    # columns to be displayed on listing view
    list_display = ('name', 'created_at', 'updated_at')

class EmployeeAdmin(admin.ModelAdmin):
    # fields to be displayed on search box
    search_fields = ('name', 'email')

    # columns to be displayed on listing view
    list_display = ('name', 'email', 'department', 'created_at', 'updated_at')

    # replaces the select box by a search field
    raw_id_fields = ('department',)

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
