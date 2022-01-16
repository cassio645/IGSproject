from rest_framework import viewsets
from myapp.models import Employee

from .serializer import EmployeeSerializer


class EmployeeApiView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer