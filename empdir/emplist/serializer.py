from rest_framework import serializers
from .models.department import Department
from .models.employee import Employee


class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=50)
    second_name = serializers.CharField(max_length=50)
    patronymic = serializers.CharField(max_length=50)
    position = serializers.CharField(max_length=200)
    tel_number = serializers.CharField(max_length=12)
    birth_date = serializers.DateField()
    email = serializers.EmailField(max_length=254)
    photo = serializers.ImageField()
    department = serializers.StringRelatedField()

    def create(self, validated_data):
        dep = Department.objects.get(dep_name=validated_data.department)
        validated_data.department = dep
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.second_name = validated_data.get('second_name', instance.second_name)
        instance.patronymic = validated_data.get('patronymic_name', instance.patronymic)
        instance.position = validated_data.get('position_name', instance.position)
        instance.tel_number = validated_data.get('tel_number_name', instance.tel_number)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.email = validated_data.get('email', instance.email)
        instance.photo = validated_data.get('photo', instance.photo)
        dep_name = validated_data.get('department', instance.department)
        dep = Department.objects.get(dep_name=dep_name)
        instance.department = dep
        instance.save()
