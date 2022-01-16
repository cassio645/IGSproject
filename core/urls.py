
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from myapp.api.viewsets import EmployeeApiView

router = routers.DefaultRouter()
router.register("", EmployeeApiView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('myapp.urls')),
    path('employee/', include(router.urls)),
]
