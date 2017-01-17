from rest_framework import serializers

from staff.models import Department, Employee

# COMMON_FIELDS contains fields which may exist on all serializers.
COMMON_FIELDS = ('id', 'created_at', 'updated_at')


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Department
        fields = COMMON_FIELDS + ('name',)


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = COMMON_FIELDS + ('name', 'email', 'department')
