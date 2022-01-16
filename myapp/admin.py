from django.contrib import admin
from .models import Employee, Department

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department')

admin.site.register(Department)
admin.site.register(Employee, EmployeeAdmin)