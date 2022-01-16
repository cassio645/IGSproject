from django.urls import path

from . import views

app_name = "employee"
urlpatterns = [ 
    path("", views.EmployeeList.as_view(), name='list')
]