from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from ..models.employee import Employee
from ..serializer import EmployeeSerializer


class EmployeeView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        employee = request.data.get('employee')
        serializer = EmployeeSerializer(data=employee)
        if serializer.is_valid(raise_exception=True):
            employee_saved = serializer.save()
        return Response({'success': "Employee {} {} {} created successfully".format(employee_saved.first_name,
                                                                                    employee_saved.second_name,
                                                                                    employee_saved.patrinymic)})

    def put(self, request, pk):
        saved_employee = get_object_or_404(Employee.objects.all(), pk=pk)
        data = request.data.get('employees')
        serializer = EmployeeSerializer(instance=saved_employee, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            employee_saved = serializer.save()

        return Response({
            'success': "Employee {} {} {} update successfully".format(employee_saved.first_name,
                                                                      employee_saved.second_name,
                                                                      employee_saved.patrinymic)
        })

    def delete(self, request, pk):
        employee = get_object_or_404(Employee.objects.all(), pk=pk)
        employee.delete()
        return Response({
            'success': "Employee with id {} was deleted".format(pk)
        }, status=204)
