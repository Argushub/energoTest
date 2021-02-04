from django.urls import path

from .views.employees import EmployeeView


app_name = "employees"

urlpatterns = [
    path('employees/', EmployeeView.as_view()),
    path('emloyees/<int:pk>', EmployeeView.as_view())
]
