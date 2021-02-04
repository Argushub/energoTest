from django.contrib import admin
from .models.employee import Employee
from .models.department import Department


admin.site.register(Employee)
admin.site.register(Department)
