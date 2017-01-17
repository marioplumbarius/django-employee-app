from django.conf.urls import url, include
from rest_framework import routers

from staff import views

router = routers.DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'employees', views.EmployeeViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls))
]
