from django.views.generic import ListView
from .models import Employee

class EmployeeList(ListView):
    model = Employee
    context_object_name = 'list_employees'

    def get_queryset(self):
        return Employee.objects.all() 